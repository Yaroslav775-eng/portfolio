# Full Ukrainian translation script for ua.html
# Copies index.html -> ua.html and applies all Ukrainian translations

import shutil

shutil.copy('index.html', 'ua.html')

with open('ua.html', 'r', encoding='utf-8') as f:
    c = f.read()

# =============================================
# NAV
# =============================================
c = c.replace(
    '<span style="color: #fff; text-decoration: underline;">EN</span>',
    '<a href="index.html" style="color: #888; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#888\'">EN</a>'
)
c = c.replace(
    '<a href="ua.html" style="color: #888; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#888\'">UA</a>',
    '<span style="color: #fff; text-decoration: underline;">UA</span>'
)
# Phone: GR -> UA
c = c.replace('tel:+306974395895" title="Greek Number"', 'tel:+380505580953" title="Ukrainian Number"')
c = c.replace('\U0001f1ec\U0001f1f7</span> +30 697 439 58 95', '\U0001f1fa\U0001f1e6</span> +38 050 558 09 53')
# CTA button
c = c.replace("Let's Talk &rarr;", "Зв\u2019язатися &rarr;")
# CV link
c = c.replace('href="cv_eng.html"', 'href="cv_ua.html"')

# =============================================
# META / HEAD
# =============================================
c = c.replace('<html lang="en">', '<html lang="uk">')
c = c.replace(
    '<title>Google Ads Specialist | Iaroslav Zhakun</title>',
    '<title>Спеціаліст Google Ads | Ярослав Жакун</title>'
)
c = c.replace(
    'content="Google Ads Specialist. I manage Google Ads campaigns for e-commerce and lead generation. Steady sales growth and controlled costs."',
    'content="Спеціаліст Google Ads. Веду рекламні кампанії для інтернет-магазинів та генерації лідів. Стабільне зростання продажів та контроль над витратами."'
)
c = c.replace(
    'canonical" href="https://yaroslav775-eng.github.io/portfolio/"',
    'canonical" href="https://yaroslav775-eng.github.io/portfolio/ua.html"'
)
c = c.replace('og:locale" content="en_US"', 'og:locale" content="uk_UA"')
c = c.replace(
    'property="og:title" content="Iaroslav Zhakun | Google Ads Specialist"',
    'property="og:title" content="Ярослав Жакун | Фахівець з Google Ads"'
)
c = c.replace(
    'property="og:description" content="Reducing your advertising costs and increasing revenue. Marketing experience since 2013."',
    'property="og:description" content="Зменшую ваші витрати на рекламу та збільшую доходи. Досвід у маркетингу з 2013 року."'
)

# =============================================
# HERO
# =============================================
c = c.replace(
    '&#10003; Open to Opportunities &middot; Google Ads Specialist',
    '&#10003; Відкритий до пропозицій &middot; Спеціаліст Google Ads'
)
c = c.replace(
    'Iaroslav Zhakun &mdash; Google Ads Specialist',
    'Ярослав Жакун &mdash; Спеціаліст Google Ads'
)
c = c.replace(
    'Google Ads Specialist &mdash; helping businesses get more from their ad budget',
    'Спеціаліст Google Ads &mdash; допомагаю бізнесу отримувати більше від рекламного бюджету'
)
c = c.replace(
    'I manage Google Ads campaigns for e-commerce and lead generation. My focus is always on your result: steady sales growth, controlled costs, and reports you can actually understand.',
    'Веду рекламні кампанії для інтернет-магазинів та генерації лідів. Мій пріоритет — ваш результат: стабільне зростання продажів, контроль над витратами та зрозуміла звітність.'
)
c = c.replace('>View My CV<', '>Переглянути CV<')
c = c.replace('>See Results<', '>Переглянути результати<')

# Stats
c = c.replace('>Marketing Experience<', '>Досвід у маркетингу<')
c = c.replace('>Launched from Scratch<', '>Проектів з нуля<')
c = c.replace('>Monthly Budgets Managed<', '>Місячні бюджети під управлінням<')
c = c.replace('>Active Projects Cap<', '>Паралельних проектів<')

# =============================================
# CASES
# =============================================
c = c.replace('>Track Record &amp; Proof<', '>Досвід та Результати<')
c = c.replace('>Selected Case Studies<', '>Вибрані кейси<')

# Case titles and teasers
c = c.replace(
    '>E-commerce: Pet Supplies<span class="case-tag">Architecture</span>',
    '>E-commerce: Зоотовари<span class="case-tag">Архітектура</span>'
)
c = c.replace(
    'Replaced chaotic catalog spend with structured demand capture layers. Isolated high-value Search from broad Shopping for predictable ROI.',
    'Замінили хаотичні витрати на структуровані шари захоплення попиту. Ізолювали пошук від Shopping для передбачуваного ROI.'
)
c = c.replace(
    '>E-commerce: BBQ Grills<span class="case-tag">Scaling</span>',
    '>E-commerce: Товари для гриля<span class="case-tag">Масштабування</span>'
)
c = c.replace(
    'Priority-driven category scaling. Optimized inventory exposure using PMax for reach and Search for capturing high-margin intent.',
    'Масштабування категорій на основі пріоритетів. Оптимізували охоплення через PMax та захоплення маржинального попиту через Search.'
)
c = c.replace(
    '>B2B: Logistics<span class="case-tag">LeadGen</span>',
    '>B2B: Логістика<span class="case-tag">Лідогенерація</span>'
)
c = c.replace(
    'Isolated B2B intent from generic volume. Built a transparent lead-gen system with brand isolation and DSA gap filling.',
    'Ізолювали B2B-намір від загального трафіку. Побудували прозору систему лідогенерації з ізоляцією бренду та DSA.'
)
c = c.replace(
    '>E-commerce: Electronics<span class="case-tag">Technical</span>',
    '>E-commerce: Електроніка<span class="case-tag">Технічний</span>'
)
c = c.replace(
    'Tiered inventory scaling. Strengthened PMax visibility for top-performing product groups while preserving branded Search control.',
    'Багаторівневе масштабування інвентарю. Підсилили PMax для топ-груп зі збереженням контролю брендового Search.'
)
c = c.replace(
    '>Local Services: Repair<span class="case-tag">Efficiency</span>',
    '>Послуги: Ремонт<span class="case-tag">Ефективність</span>'
)
c = c.replace(
    'Hyper-local radius strategy. Defended CPA in an overheated niche via precision zone targeting and mobile call-centric funnels.',
    'Гіперлокальна радіусна стратегія. Захистили CPA в перегрітій ніші через точний гео-таргетинг та Call-Only воронки.'
)
c = c.replace(
    '>Industrial B2B: Tools<span class="case-tag">Strategy</span>',
    '>Industrial B2B: Обладнання<span class="case-tag">Стратегія</span>'
)
c = c.replace(
    'Supply-chain intent filtering. Rigorous keyword exclusion logic to eliminate retail noise and capture professional buyers.',
    'Фільтрація supply-chain інтенту. Жорстка логіка мінус-слів для відсіювання роздрібного шуму та захоплення закупників.'
)
c = c.replace('>System View <span>', '>Системний огляд <span>')

# =============================================
# COMPARISON TABLE
# =============================================
c = c.replace('>Strategic Value<', '>Стратегічна цінність<')
c = c.replace('>Ad Management vs. Ad Architecture<', '>Управління рекламою vs. Архітектура реклами<')
c = c.replace(
    'Why a "System-Driven" approach outperforms traditional media buying by focusing on the infrastructure of growth.',
    'Чому системний підхід перевершує традіційну закупку медіа, зосередившись на інфраструктурі зростання.'
)
c = c.replace('>Feature<', '>Параметр<')
c = c.replace('>Standard Management<', '>Стандартне управління<')
c = c.replace('>Systematic Architecture<', '>Системна архітектура<')
c = c.replace('>Primary Goal<', '>Головна мета<')
c = c.replace('>Maximize traffic volume<', '>Максимум трафіку<')
c = c.replace('>Maximize incremental profit<', '>Максимум інкрементального прибутку<')
c = c.replace('>"Black Box" automation<', '>«Чорна скринька» автоматизація<')
c = c.replace('>Strategic steering &amp; brand isolation<', '>Стратегічне управління та ізоляція бренду<')
c = c.replace('>Tracking<', '>Трекінг<')
c = c.replace('>Surface-level conversions<', '>Поверхневі конверсії<')
c = c.replace('>Scaling<', '>Масштабування<')
c = c.replace('>Raising bids by "feel"<', '>Підвищення ставок «на відчуття»<')
c = c.replace('>Data-backed ROAS tiering<', '>ROAS-тайєрінг на основі даних<')
c = c.replace('>Communication<', '>Комунікація<')
c = c.replace('>Interface metrics (CTR/CPC)<', '>Інтерфейсні метрики (CTR/CPC)<')
c = c.replace('>Business metrics (ROI / POAS / CAC)<', '>Бізнес-метрики (ROI / POAS / CAC)<')

# =============================================
# CREDENTIALS
# =============================================
c = c.replace('>Professional Resume<', '>Професійне резюме<')
c = c.replace('>Background &amp; Credentials<', '>Досвід та кваліфікація<')
c = c.replace(
    'Iaroslav Zhakun — Google Ads Specialist with a background as an Economist-Manager. I began my career in digital marketing in 2013, specializing deeply in Google Ads architecture and performance optimization since 2017. Over the past decade, I have successfully managed over 80 projects across B2C E-commerce and B2B lead generation sectors.',
    'Ярослав Жакун — спеціаліст Google Ads з базовою освітою економіста-менеджера. Почав кар\'єру в digital-маркетингу у 2013 році, з 2017-го глибоко спеціалізуюся на архітектурі Google Ads та performance-оптимізації. За десятиліття успішно вів понад 80 проектів у B2C E-commerce та B2B лідогенерації.'
)
c = c.replace('>Connect on Telegram<', '>Написати в Telegram<')
c = c.replace('>View Full Resume →<', '>Переглянути повне CV →<')
c = c.replace('>Management &amp; Strategy — The Open University (UK)<', '>Management &amp; Strategy — The Open University (UK)<')
c = c.replace('>Search, Shopping &amp; Performance Max Architecture<', '>Search, Shopping &amp; Performance Max Архітектура<')
c = c.replace('>Systematic Product Thinking — Skillsetter.io<', '>Системне продуктове мислення — Skillsetter.io<')
c = c.replace('>Higher Education<', '>Вища освіта<')
c = c.replace('>Manager-Economist — Kherson State University<', '>Менеджер-економіст — Херсонський державний університет<')
c = c.replace('>Tech Stack &amp; Tools<', '>Технічний стек та інструменти<')

# =============================================
# EXPERIENCE TIMELINE
# =============================================
c = c.replace('>Professional Experience<', '>Професійний досвід<')
c = c.replace('>Career Journey<', '>Кар\'єрний шлях<')
c = c.replace(
    '>AdOps Manager for International Brands | YouTube Ads<',
    '>AdOps Manager для міжнародних брендів | YouTube Ads<'
)
c = c.replace(
    'Supported QA and AdOps processes for international YouTube and Google Ads campaigns. Focused on Brand Safety standards and programmatic advertising workflows using Salesforce and Ads Editor.',
    'Підтримував QA та AdOps процеси для міжнародних кампаній YouTube та Google Ads. Фокус на стандартах Brand Safety та програматичних рекламних процесах через Salesforce та Ads Editor.'
)
c = c.replace(
    'Managed and optimized Performance Max and Google Shopping campaigns for e-commerce. Configured GA4, GTM, and Merchant Center for deep tracking and UX/CRO analysis.',
    'Керував та оптимізував кампанії Performance Max та Google Shopping для e-commerce. Налаштовував GA4, GTM та Merchant Center для глибокого трекінгу та UX/CRO аналізу.'
)
c = c.replace('>2015 – Present<', '>2015 – дотепер<')
c = c.replace(
    '>Performance Marketing Lead / Media Buyer<',
    '>Performance Marketing Lead / Media Buyer<'
)
c = c.replace(
    'Led performance marketing for 50+ projects from scratch. Managed portfolios with monthly budgets of $50k+, consistently reducing inefficient spend by 30%.',
    'Вів performance-маркетинг для 50+ проектів з нуля. Управляв портфелями з місячними бюджетами $50k+, стабільно скорочуючи неефективні витрати на 30%.'
)
c = c.replace('>E-commerce Manager<', '>E-commerce Manager<')
c = c.replace(
    'Developed and implemented e-commerce growth strategies for a global brand. Increased annual sales among assigned clients by 15% through data-driven initiatives.',
    'Розробляв та впроваджував стратегії зростання e-commerce для глобального бренду. Збільшив річні продажі серед закріплених клієнтів на 15% завдяки data-driven ініціативам.'
)
c = c.replace(
    '>View Detailed Education &amp; Case History in Full CV →<',
    '>Переглянути повну освіту та кейси в CV →<'
)

# =============================================
# METHODOLOGY
# =============================================
c = c.replace('>Map the Situation<', '>Аналіз ситуації<')
c = c.replace(
    'GTM audit and demand landscape mapping. Identifying where commercial intent lives and where branded traffic hides.',
    'GTM-аудит та картування попиту. Визначаємо, де живе комерційний намір і де ховається брендовий трафік.'
)
c = c.replace('>Build the System<', '>Побудова системи<')
c = c.replace(
    'Strict separation of demand types. Eliminating intent overlaps and building a transparent, manageable architecture.',
    'Жорстке розділення типів попиту. Усуваємо перетини намірів і будуємо прозору, керовану архітектуру.'
)
c = c.replace('>Scale with Control<', '>Масштабування з контролем<')
c = c.replace(
    'Incrementality testing and budget expansion based on unit economics and margin-level profitability.',
    'Тестування інкрементальності та розширення бюджету на основі юніт-економіки та маржинальної прибутковості.'
)
c = c.replace('>Strategic Approach<', '>Стратегічний підхід<')
c = c.replace(
    '"Automated systems like Performance Max require strategic steering to protect margins. By isolating branded intent and integrating offline conversion signals, we force the algorithm to deliver incremental growth rather than just cannibalizing existing demand."',
    '«Автоматизовані системи на кшталт Performance Max потребують стратегічного управління для захисту маржі. Ізолюючи брендовий намір та інтегруючи офлайн-конверсії, ми змушуємо алгоритм приносити інкрементальне зростання, а не просто канібалізувати наявний попит.»'
)

# =============================================
# EXPERTISE / CAPABILITIES
# =============================================
c = c.replace('>Expertise Map<', '>Карта експертизи<')
c = c.replace('>Beyond the Ads Interface<', '>Поза межами рекламного кабінету<')
c = c.replace('>E-com &amp; Feed Strategy<', '>E-com та стратегія фідів<')
c = c.replace(
    'Engineering complex Google Merchant Center setups with Custom Labels and margin-based bidding to ensure profitability at scale.',
    'Налаштування складних Google Merchant Center з Custom Labels та ставками на основі маржі для масштабованої прибутковості.'
)
c = c.replace('>Technical Infrastructure<', '>Технічна інфраструктура<')
c = c.replace(
    'Implementing deterministic tracking via GTM and GA4: micro-conversions, server-side tagging, and CRM data integration.',
    'Впровадження детерміністичного трекінгу через GTM та GA4: мікро-конверсії, server-side теггінг та інтеграція CRM-даних.'
)
c = c.replace('>B2B Lead Acquisition<', '>B2B залучення лідів<')
c = c.replace(
    'Designing high-intent Search structures for long sales cycles: precision negative keyword libraries and lead quality filtering.',
    'Проектування Search-структур для довгих циклів продажів: точні бібліотеки мінус-слів та фільтрація якості лідів.'
)
c = c.replace('>Reporting &amp; Data Science<', '>Звітність та аналітика<')
c = c.replace(
    'Building Looker Studio dashboards focused on business-level KPIs: Blended CAC, Net Margin, and channel incrementality.',
    'Побудова Looker Studio дашбордів з фокусом на бізнес-KPI: Blended CAC, Net Margin та інкрементальність каналу.'
)

# Adjacent capabilities
c = c.replace('>Adjacent Capabilities<', '>Суміжні компетенції<')
c = c.replace('>Go-To-Market Strategy<', '>Go-To-Market стратегія<')
c = c.replace(
    'Market analysis, competitive positioning and full-funnel architecture planning before campaign launch.',
    'Аналіз ринку, конкурентне позиціонування та планування повної воронки перед запуском кампаній.'
)
c = c.replace('>LLM &amp; API Automation<', '>LLM та API автоматизація<')
c = c.replace(
    'Python scripts &amp; LLM-driven flows for offline conversion uploads &amp; automated campaign steering.',
    'Python-скрипти та LLM-потоки для завантаження офлайн-конверсій та автоматизованого управління кампаніями.'
)
c = c.replace('>Local SEO (Map-Pack)<', '>Local SEO (Map-Pack)<')
c = c.replace(
    'Syncing Google Business Profile with strict paid search boundaries to monopolize high-intent local traffic.',
    'Синхронізація Google Business Profile із межами платного пошуку для монополізації локального трафіку з високим наміром.'
)
c = c.replace('>Project Management<', '>Управління проектами<')
c = c.replace(
    'Acting as the central node between developers, designers and C-level to launch campaigns without delays.',
    'Виступаю центральним вузлом між розробниками, дизайнерами та C-level для запуску кампаній без затримок.'
)

# =============================================
# EMPLOYER FIT / WHAT I BRING
# =============================================
c = c.replace('>Area of Responsibility<', '>Зона відповідальності<')
c = c.replace('>What I Bring to the Team<', '>Що я привношу в команду<')
c = c.replace(
    '<strong>Transparent Analytics:</strong> I set up precise tracking (GA4, GTM) and attribution to ensure data-driven decisions.',
    '<strong>Прозора аналітика:</strong> Налаштовую точний трекінг (GA4, GTM) та атрибуцію для прийняття рішень на основі даних.'
)
c = c.replace(
    '<strong>Controlled Scaling:</strong> Transitioning ad accounts from chaotic spending to predictable, ROI-positive budget expansion.',
    '<strong>Контрольоване масштабування:</strong> Переводжу рекламні акаунти від хаотичних витрат до передбачуваного, ROI-позитивного розширення бюджету.'
)
c = c.replace(
    '<strong>Cross-functionality:</strong> Proficient in drafting technical specs for developers, designers, and data analysts.',
    '<strong>Крос-функціональність:</strong> Складаю технічні завдання для розробників, дизайнерів та аналітиків даних.'
)
c = c.replace(
    '<strong>Clear Reporting:</strong> Building Looker Studio dashboards that make complex performance metrics accessible to C-level management.',
    '<strong>Зрозуміла звітність:</strong> Будую Looker Studio дашборди, що роблять складні метрики доступними для C-level керівництва.'
)
c = c.replace('>Working Formats<', '>Формати роботи<')
c = c.replace('>Who I am Looking For<', '>Кого я шукаю<')
c = c.replace(
    '<strong>In-house Teams:</strong> E-commerce projects (B2C) with broad catalogs or B2B companies with complex sales cycles.',
    '<strong>In-house команди:</strong> E-commerce проекти (B2C) з широкими каталогами або B2B компанії зі складними циклами продажів.'
)
c = c.replace(
    '<strong>Performance Agencies:</strong> Ready to join a strong team to manage a dedicated pool of clients.',
    '<strong>Performance-агенції:</strong> Готовий приєднатися до сильної команди для роботи з пулом клієнтів.'
)
c = c.replace(
    '<strong>Startups:</strong> Needing a dedicated specialist to take full ownership of Paid Search acquisition.',
    '<strong>Стартапи:</strong> Яким потрібен виділений спеціаліст для повного контролю над Paid Search залученням.'
)
c = c.replace(
    '<strong>Goal:</strong> Long-term collaboration where I can deeply embed myself into the product and its metrics.',
    '<strong>Мета:</strong> Довгострокова співпраця, де я можу глибоко зануритися в продукт та його метрики.'
)

# =============================================
# DISCOVERY / CTA
# =============================================
c = c.replace('>Next Step<', '>Наступний крок<')
c = c.replace(
    '>Looking for a System-Driven PPC Specialist?<',
    '>Шукаєте системного PPC-спеціаліста?<'
)
c = c.replace(
    'I am open to new opportunities and ready to join your team (Full-time / Part-time / Project basis).',
    'Відкритий до нових можливостей та готовий приєднатися до вашої команди (Full-time / Part-time / Проектна основа).'
)
c = c.replace(
    'My goal is to take ownership of your Paid Search acquisition, build a transparent system, and communicate with the business solely through the lens of concrete numbers and ROI.',
    'Моя мета — взяти відповідальність за ваш Paid Search, побудувати прозору систему та спілкуватися з бізнесом виключно мовою конкретних цифр та ROI.'
)
c = c.replace('>Schedule an Interview<', '>Призначити зустріч<')
c = c.replace(
    'Message me on Telegram or by email to arrange an introductory call and discuss your current marketing challenges.',
    'Напишіть мені в Telegram або на email, щоб домовитися про знайомчий дзвінок та обговорити ваші поточні маркетингові виклики.'
)
c = c.replace('>Message on Telegram<', '>Написати в Telegram<')

# Final CTA section
c = c.replace('>Next Steps<', '>Наступні кроки<')
c = c.replace(">Let's Start a Professional Dialogue<", '>Розпочнемо професійний діалог<')
c = c.replace(
    "I am open to exploring how my systematic approach can complement your team. Let's discuss your current challenges and potential synergies.",
    'Відкритий до розмови про те, як мій системний підхід може доповнити вашу команду. Давайте обговоримо ваші поточні завдання та можливі точки дотику.'
)
c = c.replace('>Email me<', '>Написати на email<')

# Footer
c = c.replace(
    '&copy; 2026 Iaroslav Zhakun. All rights reserved.',
    '&copy; 2026 Ярослав Жакун. Всі права захищено.'
)

# =============================================
# MODALS (case study text inside modal)
# =============================================
c = c.replace('>Goal: Transform a chaotic account into a transparent system prioritizing confirmed profit.<',
    '>Мета: Трансформувати хаотичний акаунт у прозору систему з пріоритетом підтвердженого прибутку.<')
c = c.replace('>Strategic Architecture<', '>Стратегічна архітектура<')
c = c.replace('>Technical Execution<', '>Технічна реалізація<')
c = c.replace('>Performance Results (Scale)<', '>Результати (Масштаб)<')
c = c.replace('>Performance Results<', '>Результати<')
c = c.replace('>Avg. CPA<', '>Середній CPA<')
c = c.replace('>Conversions<', '>Конверсій<')
c = c.replace('>Sales Value<', '>Виручка<')
c = c.replace('>Qualified Leads<', '>Квал. лідів<')
c = c.replace('>Ad Spend<', '>Витрати на рекламу<')
c = c.replace('>Booked Calls<', '>Дзвінків<')

with open('ua.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('UA translation complete. Size:', len(c), 'chars')
