import json

translations = {
    # Headers and Metatags
    'Senior Google Ads Strategist': 'Senior Google Ads-Стратег',
    'Architecting Predictable <i>Demand Systems.</i>': 'Створення Прогнозованих <i>Систем Попиту.</i>',
    'Google Ads is a matrix of buyer intent, not just a collection of campaigns. As a Senior Strategist, I transition complex accounts from chaotic spending into highly structured systems—executing hands-on within the ads manager to scale both Bootstrapped profitability and VC-backed market share.': 'Google Ads — це матриця купівельного наміру, а не просто набір кампаній. Як Senior-Стратег, я переводжу складні акаунти від хаотичних витрат до чітко структурованих систем — працюючи безпосередньо в рекламному кабінеті для масштабування прибутку та захоплення частки ринку.',
    'Schedule Interview': 'Призначити Інтерв\'ю',
    'Connect on LinkedIn': 'Зв\'язатися в LinkedIn',
    'Comfortable scaling budgets<br><b>from €10k to €50k+/mo</b>': 'Досвід масштабування бюджетів<br><b>від €10k до €50k+/міс</b>',
    'Translating high-level strategy to CPL/ROAS': 'Переведення високорівневої стратегії в реальні CPL/ROAS',
    'Logistics & Availability:': 'Логістика та Доступність:',
    
    # Tech Stack
    'Technology Stack': 'Технологічний Стек',
    
    # Career Impact
    'Career Ad Spend Managed': 'Управління бюджетами за кар\'єру',
    'Tracked Client Revenue': 'Відстежений дохід клієнтів',
    'Google Ads Specialization': 'Спеціалізація в Google Ads',
    'SKUs Optimised (GMC)': 'Оптимізованих SKU (GMC)',
    
    # Track Record
    'Track Record & Proof': 'Досвід та Докази',
    'Selected Case Studies': 'Вибрані Кейси',
    'Read Full Case Study': 'Читати Повний Кейс',
    
    # Teasers
    'Resolved heavy intent mixing where generic and branded terms collided. Built a rigorous Search to Shopping pipeline, establishing a transparent baseline for scale.': 'Вирішено проблему змішування намірів, коли базові та брендові запити конфліктували. Побудовано сувору воронку Search to Shopping, що створило прозору базу для масштабування.',
    
    'Aggressive seasonal scaling challenge. Segmented catalog by business margin, forcing PMax algorithms away from brand cannibalization into net-new territory.': 'Агресивне сезонне масштабування. Сегментовано каталог за маржинальністю бізнесу, примусово вивівши алгоритми PMax з канібалізації бренду на нові території.',
    
    'Protected budget from B2C "junk" leads common in logistics. Engineered high-intent manual B2B search architectures resulting in qualified contract leads.': 'Захист бюджету від B2C сміття, типового в логістиці. Створено високоінтентні ручні B2B пошукові архітектури, що принесли кваліфіковані ліди.',
    
    'Managed an immense 10k+ SKU catalog with massive margin variance. Stopped blanket catalog spending, isolating budget directly to high-margin priority SKUs.': 'Управління каталогом на 10k+ SKU з величезною різницею в маржинальності. Зупинено розмиті витрати, бюджет ізольовано суворо під високомаржинальні пріоритетні товари.',
    
    # Professional Summary
    'Professional Summary': 'Професійне Резюме',
    'Who I Am (And Who I\'m Not)': 'Хто я (І ким я не є)',
    'I am a Technical PPC Specialist with deep hands-on experience building, auditing, and optimizing complex Google Ads architectures. I focus strictly on pure performance execution: granular campaign structure, feed management (GMC), deterministic conversion tracking (GTM/GA4), and data-driven scaling.': 'Я — технічний PPC Specialist із глибоким практичним досвідом побудови, аудиту та оптимізації складних архітектур Google Ads. Моя увага зосереджена виключно на чистому performance: гранулярна структура кампаній, управління фідами (GMC), трекінг конверсій (GTM/GA4) та масштабування на основі даних.',
    'Having launched over 50 projects from scratch and managed €50,000+ in monthly budgets across E-commerce and B2B, I maintain a clear boundary in my work: <b>I am an analytical executor and strategist, not a salesperson or account manager.</b> I partner with agencies and brands who need someone living inside the data, driving actual business metrics.': 'Запустивши понад 50 проектів з нуля та керуючи місячними бюджетами від €50,000+ в E-commerce та B2B, я тримаю чітку межу у своїй роботі: <b>я аналітичний виконавець і стратег, а не продавець чи акаунт-менеджер.</b> Я співпрацюю з агенціями та брендами, яким потрібна людина, яка живе всередині даних і впливає на реальні бізнес-метрики.',
    'View Full LinkedIn Profile': 'Переглянути повний профіль LinkedIn',
    
    # Value Prop
    'My Value Proposition': 'Моя Ціннісна Пропозиція',
    'The "Demand Mapping" Methodology': 'Методологія "Мапування Попиту"',
    '1. Mapping the Demand': '1. Мапування Попиту',
    'Before spending a dollar, I audit the exact state of your account\'s intent. I locate where the "hot" commercial demand lies, where branded traffic is hidden, and what campaigns are merely spending without incremental return.': 'Перед тим як витратити хоча б долар, я проводжу аудит інтент-матриці вашого акаунта. Я знаходжу, де лежить "гарячий" комерційний попит, де прихований бренд-трафік і які кампанії просто спалюють бюджет без інкрементального повернення.',
    
    '2. Intent Isolation': '2. Ізоляція Інтенту',
    'I restructure algorithms (like PMax) and Search campaigns to ensure they never overlap. By completely isolating branded intent from net-new acquisition, we secure your true margins from cannibalization.': 'Я реструктуризую алгоритми (наприклад PMax) і Пошукові кампанії, щоб вони ніколи не перетиналися. Повністю ізолюючи брендовий намір від залучення нових клієнтів, ми захищаємо вашу маржу від канібалізації.',
    
    '3. Surgical Scaling': '3. Хірургічне Масштабування',
    'Instead of aggressively inflating budgets and hoping for the best, I execute strictly inside the Ads Manager where unit economics allow. Growth is achieved by manually amplifying the most profitable segments of your Demand Map.': 'Замість агресивного роздування бюджетів і надії на краще, я працюю суто там, де це дозволяє юніт-економіка. Зростання досягається шляхом ручного підсилення найприбутковіших сегментів вашої Мапи Попиту.',
    
    'My Perspective on the Modern Ads Auction': 'Мій погляд на сучасний рекламний аукціон',
    '"Performance Max is a black box that steals margin if you don’t strictly control its inputs. By isolating branded intent and feeding the algorithm offline conversions, we force Google to bring net-new revenue—not just grade its own homework."': '«Performance Max — це чорна скринька, яка з\'їдає маржу, якщо ви жорстко не контролюєте її ввідні дані. Ізолюючи брендовий трафік і згодовуючи алгоритму офлайн-конверсії, ми змушуємо Google приносити суто новий дохід, а не просто виписувати п\'ятірки самому собі.»',
    
    # Cross Channel
    'T-Shaped Expertise': 'T-Shaped Експертиза',
    'Beyond the Ads Interface': 'Поза межами інтерфейсу Ads',
    
    'Go-To-Market Strategy': 'Go-To-Market Стратегія',
    'Deep competitive analysis, market positioning, and full funnel architecture planning to ensure campaigns have a foundation to succeed.': 'Глибокий конкурентний аналіз, позиціонування на ринку та планування архітектури повної воронки, щоб забезпечити фундамент для успіху кампаній.',
    
    'LLM & API Development': 'LLM та API Розробка',
    'Deploying custom LLM integrations, Python API scripts, and low-code backends (Make/Zapier) to automate workflows and offline conversions.': 'Впровадження кастомних LLM-інтеграцій, Python API-скриптів та low-code рішень (Make/Zapier) для автоматизації процесів та офлайн-конверсій.',
    
    'Local SEO Dominance': 'Домінування в Local SEO',
    'Aligning strict paid search boundaries with organic Google Business Profile strategies to monopolize high-intent map-pack traffic.': 'Синхронізація жорстких кордонів платного пошуку зі стратегіями Google Business Profile для повної монополізації високоінтентного трафіку на картах.',
    
    'Project Management': 'Управління Проектами',
    'Acting as the centralized node between tech, creative, and C-level stakeholders so campaigns launch on time and without bottlenecks.': 'Виступаю центральним вузлом між технічними, креативними та C-level стейкхолдерами, забезпечуючи вчасний запуск кампаній без затримок.',
    
    # Credentials
    'Foundation': 'Фундамент',
    'Credentials & Education': 'Сертифікації та Освіта',
    'Education & Professional Training': 'Освіта та Професійна Підготовка',
    
    # Employer fit
    'Execution Reality': 'Реальність Виконання',
    'Bringing System to Chaos': 'Систематизація Хаосу',
    
    'Clarity Restored': 'Відновлення Ясності',
    'Many brands have active ad accounts, yet lack a sense of systemic control. I eliminate the "black box" feeling by providing total transparency into exactly where every dollar goes and what phase of the funnel it influences.': 'Багато брендів мають активні рекламні акаунти, але не відчувають системного контролю. Я ліквідовую відчуття «чорної скриньки», забезпечуючи повну прозорість — щоб ви бачили, куди йде кожен долар і на який етап воронки він впливає.',
    
    'Deep Analytical Autonomy': 'Глибока Аналітична Автономія',
    'I merge into data immediately. I\'ve audited 30+ enterprise accounts, resolving GA4 tracking discrepancies, fixing Merchant Center feeds, and executing complex scripts without requiring micromanagement.': 'Я занурююся в дані одразу. Провів аудит понад 30+ enterprise акаунтів, вирішуючи розбіжності відстеження GA4, налаштовуючи фіди Merchant Center та впроваджуючи складні скрипти без необхідності в мікроменеджменті.',
    
    'Executive-Level Communication': 'Спілкування на рівні C-Suite',
    'I don\'t report on "Clicks" or "Impressions". I translate the entire Demand System into the language of the C-Suite: Blended CAC, Net Margin, Incrementality, and LTV. Pure business metrics.': 'Я не звітую про «Кліки» чи «Покази». Я перекладаю всю Систему Попиту на мову топ-менеджменту: Blended CAC, Net Margin, Інкрементальність та LTV. Лише конкретні бізнес-метрики.',
    
    'The Breaking Points': 'Точки Ламання',
    'When to bring me in': 'Коли варто залучати мене',
    
    '1. The Scaling Plateau': '1. Плато Масштабування',
    'Whenever you try to push the daily budget up by 20%, CPA spirals out of control and margins collapse. You need someone to structurally unlock the next phase of growth.': 'Тільки-но ви намагаєтесь підняти щоденний бюджет на 20%, CPA виходить з-під контролю, а маржа обвалюється. Вам потрібна людина, яка структурно розблокує наступну фазу росту.',
    
    '2. The Reporting Mismatch': '2. Розбіжність Звітності',
    'The Google Ads interface shows fantastic green numbers, but your bank account or Shopify dashboard says otherwise. You need an incrementality audit to stop the bleeding.': 'Інтерфейс Google Ads показує фантастичні зелені цифри, але ваш банківський рахунок або дашборд Shopify стверджують протилежне. Вам потрібен аудит інкрементальності, щоб зупинити цю втрату.',
    
    '3. Lack of Strategic Ownership': '3. Брак Стратегічного Володіння',
    'You are tired of checking up on agencies. You need an embedded Senior Strategist who owns the channel end-to-end, communicates purely in business metrics, and manages the agency/vendor resources themselves.': 'Ви втомилися контролювати агенції. Вам потрібен in-house Senior Strategist, який повністю контролює канал, спілкується виключно мовою бізнес-метрик і сам керує ресурсами агентств/підрядників.',
    
    # Discovery Quiz Setup
    'Discovery Engagement': 'Дискавері Процес',
    'The Budget Leakage Audit': 'Аудит Витоку Бюджету',
    'Most accounts suffer from hidden "leaks" where budget is quietly burned on underperforming layers—whether that\'s irrelevant audiences, unprofitable SKUs, or algorithm cannibalization.': 'Більшість акаунтів страждають від прихованих «протікань», де бюджет тихо згоряє на неефективних рівнях — будь то нерелевантні аудиторії, збиткові SKU або канібалізація алгоритмами.',
    'Before committing to a long-term engagement, I conduct a deep, analytical audit of your account. I manually analyze your campaign structures to find the "bad layers" that are dragging down your ROAS. We isolate and cut out these inefficiencies to stop the bleeding, and heavily reinvest the remaining budget into proven, high-intent audiences.': 'Перед тим як брати довгострокові зобов\'язання, я проводжу глибокий аналітичний аудит вашого акаунта. Я вручну аналізую структури кампаній, щоб знайти ті «пробиті рівні», які тягнуть ваш ROAS донизу. Ми ізолюємо та вирізаємо ці неефективності, зупиняючи втрати, і агресивно реінвестуємо вивільнений бюджет у перевірені високоінтентні сегменти.',
    'Request Technical Audit': 'Запросити Технічний Аудит',
    'Submit your Website URL and current monthly spend': 'Залиште URL сайту та поточний місячний бюджет',
    'Provide Read-Only Google Ads Access': 'Надайте доступ Read-Only до Google Ads',
    'I analyze performance layers to locate your budget leaks': 'Я аналізую рівні performance, щоб знайти витоки вашого бюджету',
    'Launch Discovery Quiz': 'Запустити Дискавері Квиз',
    '* Reserved for accounts currently spending €10,000+/mo.': '* Тільки для акаунтів з бюджетом від €10,000+/міс.',
    
    'Next Steps': 'Наступні Кроки',
    'Let\'s discuss how I can impact your numbers.': 'Давайте обговоримо, як я можу вплинути на ваші цифри.',
    'I am currently open to remote roles where I can take immediate ownership of aggressive growth targets. Let\'s schedule an interview to see if my skill set aligns with your open position.': 'Наразі я відкритий до remote позицій, де можу миттєво взяти на себе відповідальність за агресивні цілі зростання. Давайте призначимо інтерв\'ю.',
    'All rights reserved.': 'Всі права захищено.',
    '* Client names anonymized due to strict NDAs. Metrics have been translated to EUR for standardization. I am happy to elaborate on campaign structures securely during an interview.': '* Імена клієнтів анонімізовано через суворі NDA. Метрики переведені в EUR для стандартизації. З радістю розповім детальніше про архітектуру кампаній на інтерв\'ю.',

    # Header logic (EN | UA | RU) -> Active state shift
    '<span style="color: #fff; text-decoration: underline;">EN</span>': '<a href="index.html" style="color: #888; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#888\'">EN</a>',
    '<a href="ua.html" style="color: #888; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#888\'">UA</a>': '<span style="color: #fff; text-decoration: underline;">UA</span>',
    
    # Title Tag
    '<title>Iaroslav Zhakun | Senior Google Ads Strategist</title>': '<title>Ярослав Жакун | Senior Google Ads Strategist</title>'
}

with open('ua.html', 'r', encoding='utf-8') as f:
    text = f.read()

for k, v in translations.items():
    text = text.replace(k, v)

with open('ua.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('UA Done')
