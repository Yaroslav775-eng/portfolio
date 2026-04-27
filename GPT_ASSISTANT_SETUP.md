# GPT Assistant Setup

The portfolio now contains a real OpenAI backend endpoint at `api/assistant.js`.

The OpenAI key must never be added to `index.html`, `ua.html`, or any public frontend file. Keep it only in the hosting provider environment variables.

## Option A: Host the whole site on Vercel

1. Import this GitHub repository into Vercel.
2. Add the environment variable `OPENAI_API_KEY`.
3. Optional environment variables:
   - `OPENAI_MODEL` default: `gpt-5.5`
   - `OPENAI_MAX_OUTPUT_TOKENS` default: `420`
   - `OPENAI_REASONING_EFFORT` default: `low`
   - `OPENAI_TEXT_VERBOSITY` default: `low`
4. Deploy.

When the site is opened on the Vercel domain, the frontend calls `/api/assistant` automatically.

## Option B: Keep GitHub Pages and use Vercel only for API

1. Deploy this repo or a small copy containing `api/assistant.js` to Vercel.
2. Add `OPENAI_API_KEY` in Vercel.
3. Copy the deployed endpoint URL, for example:
   `https://your-vercel-app.vercel.app/api/assistant`
4. Put that URL into `assistant-config.js`:

```js
window.IAROSLAV_ASSISTANT_API_URL = 'https://your-vercel-app.vercel.app/api/assistant';
```

5. Commit and push `assistant-config.js`.

The GitHub Pages site will then send assistant requests to the Vercel API endpoint.

## Security Notes

- `api/assistant.js` allows requests from `https://yaroslav775-eng.github.io` by default.
- To add more allowed domains, set `ALLOWED_ORIGINS` in Vercel as a comma-separated list.
- To allow Vercel preview deployments, set `ALLOW_VERCEL_PREVIEWS=true`.
