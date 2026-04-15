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
    '&#10003; Available for New Projects &middot; Google Ads Specialist',
    '&#10003; Відкритий до нових проектів &middot; Спеціаліст Google Ads'
)
c = c.replace(
    '&#10003; Open to Opportunities &middot; Google Ads Specialist',
    '&#10003; Відкритий до пропозицій &middot; Спеціаліст Google Ads'
)
c = c.replace(
    'Iaroslav Zhakun &mdash; Google Ads Specialist',
    'Ярослав Жакун &mdash; Спеціаліст Google Ads'
)
c = c.replace(
    'I turn ad budgets into predictable, measurable revenue',
    'Перетворюю рекламні бюджети на передбачуваний, вимірюваний дохід'
)
c = c.replace(
    'Google Ads Specialist &mdash; helping businesses get more from their ad budget',
    'Спеціаліст Google Ads &mdash; допомагаю бізнесу отримувати більше від рекламного бюджету'
)
c = c.replace(
    'I work with agencies and direct clients. I take an account, build a system, and report in business numbers &mdash; not clicks and CTR. No hand-holding needed.',
    'Працюю з агенціями та прямими клієнтами. Беру акаунт, будую систему, звітую бізнес-цифрами &mdash; не кліками та CTR. Без необхідності постійного контролю.'
)
c = c.replace(
    'I manage Google Ads campaigns for e-commerce and lead generation. My focus is always on your result: steady sales growth, controlled costs, and reports you can actually understand.',
    'Веду рекламні кампанії для інтернет-магазинів та генерації лідів. Мій пріоритет — ваш результат: стабільне зростання продажів, контроль над витратами та зрозуміла звітність.'
)
c = c.replace('>See Case Results &darr;<', '>Переглянути кейси &darr;<')
c = c.replace('>Message on Telegram &rarr;<', '>Написати в Telegram &rarr;<')
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

# "Before" lines for each case
c = c.replace(
    'Before: ROAS stuck at 150%, budget burning with no clarity',
    'До: ROAS застряг на 150%, бюджет горів без розуміння'
)
c = c.replace(
    'Before: 400+ SKUs in one flat campaign, peak season wasted',
    'До: 400+ SKU в одній плоскій кампанії, пік сезону змарновано'
)
c = c.replace(
    'Before: volume fine, quality catastrophic &mdash; wrong audience calling',
    'До: об\'єм є, якість катастрофічна &mdash; телефонує не та аудиторія'
)
c = c.replace(
    'Before: thousands of SKUs, equal budget, zero priority logic',
    'До: тисячі SKU, рівний бюджет, нульова логіка пріоритетів'
)
c = c.replace(
    'Before: &euro;350+ CPA, paying for clicks from 3 cities away',
    'До: &euro;350+ CPA, оплата кліків від людей за три міста'
)
c = c.replace(
    'Before: leads coming in, but all from wrong audience',
    'До: ліди є, але всі від неправильної аудиторії'
)

# Case teasers (new versions after content plan)
c = c.replace(
    'Rebuilt the account around a single rule: one campaign, one job. Isolated Search, Shopping and PMax into separate demand layers for predictable ROI.',
    'Перебудували акаунт навколо одного правила: одна кампанія, одне завдання. Ізолювали Search, Shopping та PMax у окремі шари попиту для передбачуваного ROI.'
)
c = c.replace(
    'Rebuilt around margin tiers. Premium grills got dedicated PMax. DSA caught long-tail seasonal intent. GA4 reconfigured for accurate purchase value.',
    'Перебудували навколо маржинальних рівнів. Преміум-грилі отримали виділені PMax. DSA ловив довгохвостовий сезонний інтент. GA4 переналаштовано для точної вартості покупки.'
)
c = c.replace(
    'Treated keywords as a traffic filter, not a driver. Negative keyword audit eliminated consumer queries. DSA surfaced real B2B service intent.',
    'Ставилися до ключових слів як до фільтра трафіку, а не джерела. Аудит мінус-слів усунув споживчі запити. DSA виявив реальний B2B-інтент.'
)
c = c.replace(
    'Divided catalog into 3 performance tiers. PMax to priority segments. Branded Search walled off from PMax cannibalization.',
    'Розділили каталог на 3 рівні ефективності. PMax — на пріоритетні сегменти. Брендовий Search захищено від канібалізації PMax.'
)
c = c.replace(
    'Precision radius strategy: tight geo zones, Call-Only campaigns, complete negative keyword rebuild. Bids adjusted to peak booking windows.',
    'Точна радіусна стратегія: жорсткі гео-зони, Call-Only кампанії, повне перебудування мінус-слів. Ставки налаштовано на пікові вікна бронювань.'
)
c = c.replace(
    'Rebuilt around supply-chain intent. Identified language of professional buyers. Remarketing to spec-page visitors. B2B forms tracked as micro-conversions.',
    'Перебудували навколо supply-chain інтенту. Визначили мову профійних закупників. Ремаркетинг на відвідувачів сторінок специфікацій. Форми B2B відстежено як мікро-конверсії.'
)

# Old teasers (kept as fallback)
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
# Job titles (kept partially in EN as industry standard, but localize what makes sense)
c = c.replace(
    '>AdOps Manager для міжнародних брендів | YouTube Ads<',
    '>AdOps Manager для міжнародних брендів | YouTube Ads<'
)
c = c.replace('>PPC Specialist<', '>PPC-спеціаліст<')
c = c.replace('>Performance Marketing Lead / Media Buyer<', '>Керівник Performance Marketing / Media Buyer<')
c = c.replace('>E-commerce Manager<', '>E-commerce Менеджер<')
c = c.replace('Brand Safety', 'Brand Safety (безпека бренду)')
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
# DUAL-AUDIENCE BLOCK
# =============================================
c = c.replace('&#9642; For Agencies', '&#9642; Для агентств')
c = c.replace('>Need a specialist who runs accounts independently?<', '>Потрібен спеціаліст, який веде акаунти самостійно?<')
c = c.replace('&#10003;&nbsp; I take accounts without hand-holding &mdash; audit in week one', '&#10003;&nbsp; Беру акаунти без онбордингу &mdash; аудит у перший тиждень')
c = c.replace('&#10003;&nbsp; Client-ready reports in business language, not CTR', '&#10003;&nbsp; Звіти для клієнта бізнес-мовою, не CTR')
c = c.replace('&#10003;&nbsp; Managed $5k &ndash; $50k+/mo budgets independently', '&#10003;&nbsp; Самостійно керував бюджетами $5k &ndash; $50k+/міс')
c = c.replace('&#10003;&nbsp; Communicate at ROI level, not interface metrics', '&#10003;&nbsp; Комунікую на рівні ROI, а не інтерфейсних метрик')
c = c.replace('>Discuss Collaboration &rarr;<', '>Обговорити співпрацю &rarr;<')
c = c.replace('&#9642; For Direct Clients', '&#9642; Для прямих клієнтів')
c = c.replace('>Spending on ads but unclear where the money goes?<', '>Витрачаєте на рекламу, але незрозуміло куди йдуть гроші?<')
c = c.replace('&#10003;&nbsp; I explain everything without technical jargon', '&#10003;&nbsp; Пояснюю все без технічного жаргону')
c = c.replace('&#10003;&nbsp; Start with a free audit &mdash; you see the state before paying', '&#10003;&nbsp; Починаємо з безкоштовного аудиту &mdash; бачите стан до оплати')
c = c.replace('&#10003;&nbsp; Fixed accountability &mdash; I own the result, not just the tasks', '&#10003;&nbsp; Фіксована відповідальність &mdash; я відповідаю за результат, не тільки задачі')
c = c.replace('&#10003;&nbsp; You always know what&rsquo;s happening and why', '&#10003;&nbsp; Ви завжди знаєте, що відбувається і чому')
c = c.replace('>Request a Free Audit &rarr;<', '>Запросити безкоштовний аудит &rarr;<')

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

# =============================================
# QUICK CTA BLOCK (new EN strings)
# =============================================
c = c.replace('>Want results like these?<', '>Хочете такі ж результати?<')
c = c.replace(">Let's discuss your project. Free. No commitment.<", '>Обговоримо ваш проект — безкоштовно. Без зобов\u2019язань.<')
c = c.replace('>Message on Telegram &rarr;<', '>Написати в Telegram &rarr;<')

# COMPARISON TABLE HEADING
c = c.replace('>The System Advantage<', '>Системна перевага<')
c = c.replace('>Standard Specialist vs. System-Driven Approach<', '>Звичайний спеціаліст vs. Системний підхід<')
c = c.replace(
    'Why a "System-Driven" approach outperforms traditional media buying by focusing on the infrastructure of growth.',
    'Чому системний підхід перевершує традиційну закупку медіа, зосередившись на інфраструктурі зростання.'
)

# =============================================
# CASE MODALS — all 6 case study modal texts
# =============================================

# --- CASE 1: Pet Supplies ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">E-commerce: Pet Supplies</h2>',
    '<h2 style="margin-bottom: 8px;">E-commerce: Зоотовари</h2>'
)
c = c.replace(
    'The account had dozens of campaigns running simultaneously, but nobody could explain which ones actually generated profit — and which ones were quietly eating the budget. The client was spending at scale, but flying blind.',
    'В акаунті одночасно працювали десятки кампаній, але ніхто не міг пояснити, які з них реально генерують прибуток — а які тихо спалюють бюджет. Клієнт витрачав на масштабі, але наосліп.'
)
c = c.replace(
    'We restructured the account from scratch around a single principle: <strong>every campaign has one job.</strong> Search captured people ready to buy. Shopping handled catalog visibility. PMax handled incremental reach — but only after being fenced off from the brand terms that were inflating its numbers.',
    'Ми реструктурували акаунт з нуля навколо одного принципу: <strong>кожна кампанія має одне завдання.</strong> Search захоплював людей, готових купити. Shopping відповідав за видимість каталогу. PMax — за інкрементне охоплення, але лише після ізоляції від брендових запитів, які роздували цифри.'
)
c = c.replace(
    'We then split Dogs and Cats into separate campaign clusters, so budget could follow real demand patterns instead of being averaged across the whole assortment.',
    'Потім ми розділили категорії Собак і Котів на окремі кластери кампаній, щоб бюджет слідував реальним патернам попиту, а не усереднювався по всьому асортименту.'
)
c = c.replace('>Account Architecture<', '>Архітектура акаунту<')
c = c.replace(
    'Once each layer knew its role, optimization became predictable. ROAS stabilized, CPA dropped to a level that made scaling straightforward rather than risky.',
    'Коли кожен шар знав свою роль, оптимізація стала передбачуваною. ROAS стабілізувався, CPA впав до рівня, що зробив масштабування простим, а не ризикованим.'
)

# --- CASE 2: BBQ Grills ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">E-commerce: BBQ Grills</h2>',
    '<h2 style="margin-bottom: 8px;">E-commerce: Товари для гриля</h2>'
)
c = c.replace(
    'The client entered peak BBQ season with a single flat Shopping campaign covering 400+ SKUs. Budget was spread equally across premium grills and low-margin accessories — meaning the best products never got the investment they deserved.',
    'Клієнт зайшов у пік BBQ-сезону з однією плоскою Shopping-кампанією на 400+ SKU. Бюджет розподілявся рівномірно між преміум-грилями та низькомаржинальними аксесуарами — найкращі товари ніколи не отримували вкладень, яких заслуговували.'
)
c = c.replace(
    'We rebuilt the account around <strong>margin tiers</strong>. High-value grills got dedicated PMax campaigns optimized for revenue. Supporting accessories ran on lower-priority Shopping, ensuring they didn\'t compete for the same budget.',
    'Ми перебудували акаунт навколо <strong>маржинальних рівнів</strong>. Дорогі грилі отримали виділені PMax-кампанії, оптимізовані під виручку. Аксесуари працювали на Shopping з нижчим пріоритетом, щоб не конкурувати за той самий бюджет.'
)
c = c.replace(
    'DSA campaigns caught the long-tail seasonal queries that standard keyword research always misses — things people actually type when they\'re ready to buy. GA4 tracking was reconfigured to capture purchase value accurately, so the bidding algorithm was working from clean data.',
    'DSA-кампанії ловили довгохвостові сезонні запити, які стандартне дослідження ключових слів завжди пропускає — те, що люди реально пишуть, коли готові купити. Трекінг GA4 переналаштували для точного захоплення вартості покупки, щоб алгоритм ставок працював з чистими даними.'
)
c = c.replace('>Revenue Trajectory (Seasonal Window)<', '>Динаміка виручки (сезонне вікно)<')
c = c.replace('>Month-over-month growth during optimization<', '>Зростання місяць до місяця під час оптимізації<')
c = c.replace(
    'The peak season produced €157.6k in tracked sales from €23.2k in spend — with the highest ROAS on premium products where it mattered most.',
    'Пік сезону дав €157.6k відстежених продажів з €23.2k витрат — з найвищим ROAS на преміум-товарах там, де це мало найбільше значення.'
)

# --- CASE 3: Logistics ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">B2B: Logistics</h2>',
    '<h2 style="margin-bottom: 8px;">B2B: Логістика</h2>'
)
c = c.replace(
    'The company was getting clicks and form submissions — but most of them were from individuals and small operators, not the commercial clients their sales team could actually close. Volume looked fine on paper, quality was a disaster.',
    'Компанія отримувала кліки та заявки — але більшість від приватних осіб та дрібних операторів, а не від комерційних клієнтів, яких відділ продажів міг реально закрити. На папері — об\'єм є, по факту — якість катастрофічна.'
)
c = c.replace(
    'We treated the keyword strategy as a <strong>traffic filter</strong>, not a traffic driver. An extensive negative keyword audit removed all consumer-intent queries from the account. Brand terms were isolated into their own campaign so PMax couldn\'t claim credit for organic demand.',
    'Ми поставилися до стратегії ключових слів як до <strong>фільтра трафіку</strong>, а не джерела трафіку. Масштабний аудит мінус-слів видалив усі споживчі запити з акаунту. Брендові терміни ізолювали в окрему кампанію, щоб PMax не привласнював органічний попит.'
)
c = c.replace(
    'DSA campaigns then surfaced the long-tail B2B service queries that manual keyword research consistently misses — handling, express freight, volume pricing — feeding the forms with people who actually needed a logistics partner.',
    'DSA-кампанії потім виявили довгохвостові B2B-запити, які ручне дослідження постійно пропускає — перевалка, експрес-вантаж, оптові тарифи — подаючи у форми людей, яким дійсно потрібен логістичний партнер.'
)
c = c.replace('>Lead Funnel Architecture<', '>Архітектура лід-воронки<')
c = c.replace(
    '1,090 qualified business inquiries at €11.5 per lead. The sales team stopped complaining about lead quality.',
    '1,090 кваліфікованих бізнес-запитів по €11.5 за лід. Відділ продажів перестав скаржитися на якість лідів.'
)
c = c.replace('>Cost Per Lead<', '>Вартість ліда<')

# --- CASE 4: Electronics ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">E-commerce: Electronics</h2>',
    '<h2 style="margin-bottom: 8px;">E-commerce: Електроніка</h2>'
)
c = c.replace(
    'A large electronics retailer with thousands of SKUs was running budget across the entire catalog equally — no priority logic, no margin weighting. High-ticket items with strong demand were getting the same budget as slow-moving stock nobody searched for.',
    'Великий ритейлер електроніки з тисячами SKU розподіляв бюджет по всьому каталогу рівномірно — без логіки пріоритетів, без врахування маржинальності. Дорогі товари з сильним попитом отримували той самий бюджет, що й неходові позиції.'
)
c = c.replace(
    'We conducted an inventory audit and divided the product catalog into <strong>three performance tiers</strong> — priority products (high margin, high demand), standard products, and brand defense. Each tier got its own campaign type and budget logic.',
    'Ми провели аудит інвентарю і розділили каталог на <strong>три рівні ефективності</strong> — пріоритетні товари (висока маржа, високий попит), стандартні товари та захист бренду. Кожен рівень отримав свій тип кампанії та бюджетну логіку.'
)
c = c.replace(
    'PMax was pointed at priority segments with custom audience signals from past purchases. Standard products ran Smart Shopping with conservative targets. Brand terms were walled off to prevent PMax from cannibalizing organic conversions.',
    'PMax спрямували на пріоритетні сегменти з кастомними аудиторними сигналами з минулих покупок. Стандартні товари працювали на Smart Shopping з консервативними цілями. Брендові терміни огородили, щоб PMax не канібалізував органічні конверсії.'
)
c = c.replace('>Inventory Priority Architecture<', '>Архітектура пріоритетів інвентарю<')
c = c.replace('>Budget allocation follows margin priority<', '>Розподіл бюджету за маржинальним пріоритетом<')
c = c.replace(
    '€51.6k in revenue from €7.9k spend over 90 days — with the business finally able to see which product groups were driving growth and adjust inventory decisions accordingly.',
    '€51.6k виручки з €7.9k витрат за 90 днів — і бізнес нарешті побачив, які групи товарів рухають зростання, та скоригував рішення щодо інвентарю.'
)

# --- CASE 5: Repair ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">Local Services: Repair</h2>',
    '<h2 style="margin-bottom: 8px;">Послуги: Ремонт</h2>'
)
c = c.replace(
    'A repair service was paying €350+ per booked job through Google Ads, with CPA climbing every month. The local auction was overheated and the broad match strategy meant they were paying for clicks from people three cities away.',
    'Сервіс ремонту платив €350+ за кожне замовлення через Google Ads, і CPA зростав щомісяця. Локальний аукціон перегрівся, а стратегія широкої відповідності означала оплату кліків від людей за три міста.'
)
c = c.replace(
    'We switched to a <strong>precision radius strategy</strong>: tight geographic zones, Call-Only campaigns targeting mobile users during working hours, and a complete negative keyword rebuild to eliminate irrelevant searches. Bid adjustments were set to maximize exposure during the peak booking windows we identified from conversion data.',
    'Перейшли на <strong>точну радіусну стратегію</strong>: жорсткі географічні зони, Call-Only кампанії на мобільних користувачів у робочі години та повне перебудування мінус-слів. Коригування ставок налаштували на максимальне охоплення у пікові вікна бронювання, виявлені з даних конверсій.'
)
c = c.replace('>Local Intent Capture Layers<', '>Шари захоплення локального інтенту<')
c = c.replace('>Radius Zones / Call-Only Mobile / Hour-of-Day Bidding<', '>Радіусні зони / Call-Only мобайл / Ставки по годинах<')
c = c.replace(
    'CPA dropped from €350 to €12. 850 booked calls from €10.2k in spend. The campaign stabilized and the client stopped questioning whether Google Ads was worth running.',
    'CPA впав з €350 до €12. 850 забронйованих дзвінків з €10.2k витрат. Кампанія стабілізувалась, і клієнт перестав сумніватися, чи варто взагалі запускати Google Ads.'
)

# --- CASE 6: Industrial B2B ---
c = c.replace(
    '<h2 style="margin-bottom: 8px;">Industrial B2B: Tools &amp; Equipment</h2>',
    '<h2 style="margin-bottom: 8px;">Промисловий B2B: Інструменти та обладнання</h2>'
)
c = c.replace(
    'A wholesale tools supplier was generating leads — but the leads came from end consumers, not the procurement managers and contractors they needed to reach. Retail noise was drowning out serious buyers.',
    'Оптовий постачальник інструментів генерував ліди — але вони надходили від кінцевих споживачів, а не закупників та підрядників. Роздрібний шум заглушував серйозних покупців.'
)
c = c.replace(
    'The entire campaign was rebuilt around <strong>supply-chain search intent</strong>. We identified the language professional buyers actually use — wholesale pricing, bulk orders, technical specifications — and built keyword clusters around those terms exclusively.',
    'Всю кампанію перебудували навколо <strong>supply-chain пошукового інтенту</strong>. Ми визначили мову, якою реально користуються профійні закупники — оптові ціни, великі замовлення, технічні специфікації — і побудували кластери ключових слів виключно навколо цих термінів.'
)
c = c.replace(
    'Remarketing campaigns targeted users who had visited pricing or specification pages — a strong signal of procurement intent. B2B form submissions were tracked as micro-conversions so the algorithm could learn what a good lead looked like.',
    'Ремаркетинг-кампанії цілились на користувачів, які відвідували сторінки цін або специфікацій — сильний сигнал закупівельного інтенту. Форми B2B відстежувались як мікро-конверсії, щоб алгоритм навчався розпізнавати якісний лід.'
)
c = c.replace('>B2B Intent Filter Architecture<', '>Архітектура фільтрації B2B-інтенту<')
c = c.replace('>Procurement Search / Spec-Page Remarketing / Form Tracking<', '>Закупівельний пошук / Ремаркетинг / Трекінг форм<')
c = c.replace(
    '320 qualified wholesale inquiries at a controlled €45 CPA. The sales pipeline went from cluttered to manageable.',
    '320 кваліфікованих оптових запитів при контрольованому CPA €45. Воронка продажів перетворилася з захаращеної на керовану.'
)
c = c.replace('>Target CPA<', '>Цільовий CPA<')

# Common modal labels
c = c.replace('>What We Did<', '>Що ми зробили<')
c = c.replace('>The Outcome<', '>Результат<')

# =============================================
# QUIZ (modal form)
# =============================================
c = c.replace('>Discovery Framework<', '>Процес знайомства<')
c = c.replace('>Phase 1: Scope &amp; Territory<', '>Фаза 1: Масштаб і охоплення<')
c = c.replace('>Define the basic parameters of the audit.<', '>Визначте основні параметри аудиту.<')
c = c.replace('>Website URL<', '>URL вебсайту<')
c = c.replace('>Advertising Region(s)<', '>Регіон(и) реклами<')
c = c.replace('placeholder="e.g. US, UK, EU-wide"', 'placeholder="наприклад Україна, ЄС, Греція"')
c = c.replace('>Target KPIs (ROAS, CPA, Leads)<', '>Цільові KPI (ROAS, CPA, Ліди)<')
c = c.replace('placeholder="e.g. 500% ROAS or Target CPA €15"', 'placeholder="наприклад 500% ROAS або цільовий CPA €15"')
c = c.replace('>Next Phase &rarr;<', '>Наступна фаза &rarr;<')
c = c.replace('>Phase 2: The Challenge<', '>Фаза 2: Виклик<')
c = c.replace('>Detail the specific bottlenecks we are investigating.<', '>Опишіть конкретні вузькі місця, які ми досліджуємо.<')
c = c.replace('>Main problems or wishes<', '>Основні проблеми або побажання<')
c = c.replace('placeholder="What is breaking? What do you want to achieve?"', 'placeholder="Що не працює? Чого хочете досягти?"')
c = c.replace('>Main Competitors<', '>Основні конкуренти<')
c = c.replace('placeholder="Who are we fighting in the auction?"', 'placeholder="З ким воюємо на аукціоні?"')
c = c.replace('>Phase 3: Data Access<', '>Фаза 3: Доступ до даних<')
c = c.replace('>Can you provide Read-Only access to Google Ads, Analytics, and Merchant Center?<', '>Чи можете надати Read-Only доступ до Google Ads, Analytics та Merchant Center?<')
c = c.replace('>Yes, ready to provide access<', '>Так, готовий надати доступ<')
c = c.replace('>Yes, but need an NDA first<', '>Так, але спочатку потрібен NDA<')
c = c.replace('>Hard to provide access right now<', '>Зараз важко надати доступ<')
c = c.replace('>Audit Framework Prepared<', '>Фрейм аудиту підготовлено<')
c = c.replace('>The necessary pre-flight details have been captured. Click below to securely transfer your data to my personal inbox.<', '>Необхідні деталі зібрано. Натисніть нижче, щоб безпечно передати дані до мого поштового ящика.<')
c = c.replace('>Transmit Data via Email<', '>Надіслати дані електронною поштою<')
c = c.replace('>&larr; Back<', '>&larr; Назад<')

with open('ua.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('UA translation complete. Size:', len(c), 'chars')

