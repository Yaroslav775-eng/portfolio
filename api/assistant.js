const OPENAI_RESPONSES_URL = 'https://api.openai.com/v1/responses';

const SYSTEM_PROMPT = [
  'You are PPC Fit Check Assistant on Iaroslav Zhakun portfolio website.',
  'Help visitors understand Google Ads, PPC funnels, budget, ROAS, hiring fit, audits and collaboration.',
  'Use the same language as the visitor context: English for en, Ukrainian for uk, Russian if the visitor writes Russian.',
  'Be practical, concise and honest. Do not promise guaranteed results.',
  'Use the calculator context when available. If key numbers are missing, ask for the smallest useful next input.',
  'End with one clear next step. Keep answers under 150 words.'
].join(' ');

const DEFAULT_ALLOWED_ORIGINS = [
  'https://yaroslav775-eng.github.io',
  'http://localhost:3000',
  'http://localhost:5173',
  'http://127.0.0.1:5500'
];

function getAllowedOrigins() {
  const configured = (process.env.ALLOWED_ORIGINS || '')
    .split(',')
    .map((origin) => origin.trim())
    .filter(Boolean);
  const vercelOrigin = process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : '';
  return new Set([...DEFAULT_ALLOWED_ORIGINS, ...configured, vercelOrigin].filter(Boolean));
}

function isAllowedOrigin(origin) {
  if (!origin) {
    return true;
  }
  if (getAllowedOrigins().has(origin)) {
    return true;
  }
  try {
    const host = new URL(origin).hostname;
    return process.env.ALLOW_VERCEL_PREVIEWS === 'true' && host.endsWith('.vercel.app');
  } catch (err) {
    return false;
  }
}

function setCors(req, res) {
  const origin = req.headers.origin;
  if (origin && isAllowedOrigin(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  res.setHeader('Vary', 'Origin');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

async function readJson(req) {
  if (req.body) {
    return typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  }

  const chunks = [];
  for await (const chunk of req) {
    chunks.push(Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk));
  }

  const raw = Buffer.concat(chunks).toString('utf8');
  return raw ? JSON.parse(raw) : {};
}

function text(value, maxLength = 700) {
  return String(value || '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, maxLength);
}

function cleanObject(value, depth = 0) {
  if (!value || typeof value !== 'object' || depth > 4) {
    return value;
  }

  if (Array.isArray(value)) {
    return value.slice(0, 20).map((item) => cleanObject(item, depth + 1));
  }

  return Object.fromEntries(
    Object.entries(value)
      .slice(0, 40)
      .map(([key, item]) => [
        text(key, 80),
        typeof item === 'string' ? text(item, 500) : cleanObject(item, depth + 1)
      ])
  );
}

function extractAnswer(data) {
  if (typeof data.output_text === 'string' && data.output_text.trim()) {
    return data.output_text.trim();
  }

  const parts = [];
  for (const item of data.output || []) {
    for (const content of item.content || []) {
      if (typeof content.text === 'string') {
        parts.push(content.text);
      }
    }
  }

  return parts.join('\n').trim();
}

module.exports = async function handler(req, res) {
  setCors(req, res);

  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  if (!isAllowedOrigin(req.headers.origin)) {
    return res.status(403).json({ error: 'Origin is not allowed' });
  }

  if (!process.env.OPENAI_API_KEY) {
    return res.status(500).json({ error: 'OPENAI_API_KEY is not configured' });
  }

  let body;
  try {
    body = await readJson(req);
  } catch (err) {
    return res.status(400).json({ error: 'Invalid JSON body' });
  }

  const message = text(body.message, 1000);
  const context = cleanObject(body.context || {});

  if (!message) {
    return res.status(400).json({ error: 'Message is required' });
  }

  const model = process.env.OPENAI_MODEL || 'gpt-5.5';
  const payload = {
    model,
    instructions: SYSTEM_PROMPT,
    input: [
      'Visitor question:',
      message,
      '',
      'Portfolio calculator context:',
      JSON.stringify(context, null, 2)
    ].join('\n'),
    max_output_tokens: Number(process.env.OPENAI_MAX_OUTPUT_TOKENS || 420)
  };

  if (model.startsWith('gpt-5')) {
    payload.reasoning = { effort: process.env.OPENAI_REASONING_EFFORT || 'low' };
    payload.text = { verbosity: process.env.OPENAI_TEXT_VERBOSITY || 'low' };
  }

  try {
    const openaiResponse = await fetch(OPENAI_RESPONSES_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const data = await openaiResponse.json().catch(() => ({}));
    if (!openaiResponse.ok) {
      const detail = data.error && data.error.message ? data.error.message : 'OpenAI request failed';
      return res.status(openaiResponse.status).json({ error: detail });
    }

    const answer = extractAnswer(data);
    if (!answer) {
      return res.status(502).json({ error: 'OpenAI returned an empty answer' });
    }

    return res.status(200).json({ answer });
  } catch (err) {
    return res.status(500).json({ error: 'Assistant request failed' });
  }
};
