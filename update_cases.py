import os
import re

# Regex patterns to find correct injection points
cases_grid_regex = re.compile(r'<div class="cases-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
modals_regex = re.compile(r'<div style="display: none;">.*?</div>\s*<!-- MODAL POPUP HTML -->', re.DOTALL)

def replace_in_file(filepath, grid_content, modals_content, read_encoding='utf-8'):
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        return
    
    print(f"Updating {filepath} (Read Encoding: {read_encoding})...")
    try:
        with open(filepath, 'r', encoding=read_encoding) as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Retrying {filepath} with windows-1251...")
        with open(filepath, 'r', encoding='windows-1251') as f:
            content = f.read()

    new_grid = grid_content + "\n        </div>\n    </section>"
    content = cases_grid_regex.sub(new_grid, content)
    
    new_modals = modals_content + "\n    <!-- MODAL POPUP HTML -->"
    content = modals_regex.sub(new_modals, content)

    # Always write as UTF-8 for consistency
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# --- TAG GENERATOR ---
def get_tag(text):
    return f'<span class="case-tag">{text}</span>'

# --- PERFORMANCE LOGIC VISUALIZER (CSS BASED) ---
def gen_perf_visual(type="growth", label="Scale"):
    if type == "growth":
        return f"""
            <div style="margin: 32px 0; padding: 24px; background: #f9f9f9; border: 1px solid #000;">
                <span class="section-label" style="margin-bottom: 12px; display:block;">Performance Logic: {label}</span>
                <div style="display: flex; align-items: flex-end; gap: 8px; height: 60px;">
                    <div style="flex: 1; background: #eee; height: 30%;"></div>
                    <div style="flex: 1; background: #ccc; height: 45%;"></div>
                    <div style="flex: 1; background: #999; height: 65%;"></div>
                    <div style="flex: 1; background: #000; height: 100%;"></div>
                </div>
                <p style="font-size: 0.8rem; margin-top: 12px; font-weight: bold; text-transform: uppercase;">Systematic Ramp-up (90 Day Optimization Cycle)</p>
            </div>
        """
    elif type == "funnel":
        return f"""
            <div style="margin: 32px 0; padding: 24px; background: #f9f9f9; border: 1px solid #000;">
                <span class="section-label" style="margin-bottom: 12px; display:block;">PMax & Search Architecture</span>
                <div style="height: 12px; background: #eee; width: 100%; margin-bottom: 4px; position: relative;"><div style="background: #000; width: 100%; height: 100%;"></div></div>
                <div style="height: 12px; background: #eee; width: 100%; margin-bottom: 4px; position: relative;"><div style="background: #000; width: 65%; height: 100%;"></div></div>
                <div style="height: 12px; background: #eee; width: 100%; margin-bottom: 4px; position: relative;"><div style="background: #C00000; width: 25%; height: 100%;"></div></div>
                <p style="font-size: 0.8rem; margin-top: 12px; font-weight: bold; text-transform: uppercase;">Demand Capture Layers: Brand / Category / PMax</p>
            </div>
        """
    return ""

# --- GRID CARD GEN ---
def gen_grid_card(title, tag_text, teaser, m1_val, m1_lbl, m2_val, m2_lbl, case_id, btn_text):
    return f"""
                <div class="case-card" onclick="openModal('case-{case_id}')">
                    <div class="case-title">{title}{get_tag(tag_text)}</div>
                    <p class="case-teaser">{teaser}</p>
                    <div class="metrics-chips">
                        <span class="chip chip-accent"><strong>{m1_val}</strong> {m1_lbl}</span>
                        <span class="chip"><strong>{m2_val}</strong> {m2_lbl}</span>
                    </div>
                    <button class="btn-text" style="color:var(--accent-brand); background:transparent; border:none; text-align:left; font-weight:bold; cursor:pointer; font-family:var(--font-sans);text-transform:uppercase;font-size:0.8rem; margin-top: 16px;">{btn_text} <span>&rarr;</span></button>
                </div>"""

# --- MODAL GEN ---
def gen_modal(title, goal, arch_title, arch_desc, perf_type, perf_label, exec_title, exec_list, results_title, m1_val, m1_lbl, m2_val, m2_lbl, m3_val, m3_lbl, case_id):
    exec_items = "".join([f"<li>{item}</li>" for item in exec_list])
    visual = gen_perf_visual(perf_type, perf_label)
    return f"""
        <div id="data-case-{case_id}">
            <h2 style="margin-bottom: 8px;">{title}</h2>
            <div class="highlight-box">Goal: {goal}</div>
            <h4 style="color:var(--text-dark); border-bottom: 2px solid var(--accent-muted); padding-bottom: 8px; margin-top: 32px; margin-bottom: 16px;">{arch_title}</h4>
            <p><strong>{arch_desc}</strong></p>
            {visual}
            <h4 style="color:var(--text-dark); border-bottom: 2px solid var(--accent-muted); padding-bottom: 8px; margin-top: 32px; margin-bottom: 16px;">{exec_title}</h4>
            <ul>{exec_items}</ul>
            <h4 style="color:var(--text-dark); border-bottom: 2px solid var(--accent-muted); padding-bottom: 8px; margin-top: 32px; margin-bottom: 16px;">{results_title}</h4>
            <div class="modal-metrics-grid">
                <div class="modal-metric"><span class="modal-metric-val">{m1_val}</span><span class="modal-metric-lbl">{m1_lbl}</span></div>
                <div class="modal-metric"><span class="modal-metric-val">{m2_val}</span><span class="modal-metric-lbl">{m2_lbl}</span></div>
                <div class="modal-metric"><span class="modal-metric-val">{m3_val}</span><span class="modal-metric-lbl">{m3_lbl}</span></div>
            </div>
        </div>"""

# --- ENGLISH ---
en_cards = [
    ("E-commerce: Pet Supplies", "Architecture", "Replaced chaotic catalog spend with a structured demand capture layers. Isolated high-value Search from broad Shopping for predictable ROI.", "4,068", "Clicks", "819k", "Value (UAH)", 1, "System View"),
    ("E-commerce: BBQ Grills", "Scaling", "Priority-driven category scaling. Optimized inventory exposure using PMax for reach and Search for capturing high-margin intent.", "€157.6k", "Value", "1,693", "Conv.", 2, "System View"),
    ("B2B: Logistics", "LeadGen", "Isolated B2B intent from generic volume. Built a transparent lead-gen system with brand isolation and DSA gap filling.", "€10.3k", "Spend", "1,090", "Conv.", 3, "System View"),
    ("E-commerce: Electronics", "Technical", "Tiered inventory scaling. Strengthened PMax visibility for top-performing product groups while preserving branded Search control.", "€51.6k", "Value", "1,178", "Conv.", 4, "System View"),
    ("Local Services: Repair", "Efficiency", "Hyper-local radius strategy. Defended CPA in an overheated niche via precision zone targeting and mobile call-centric funnels.", "€12", "Avg. CPA", "850", "Calls", 5, "System View"),
    ("Industrial B2B: Tools", "Strategy", "Supply-chain intent filtering. Rigorous keyword exclusion logic to eliminate retail noise and capture professional buyers.", "320", "Leads", "€45", "CPA", 6, "System View")
]
en_grid = '<div class="cases-grid">' + "".join([gen_grid_card(*c) for c in en_cards])
en_modals = '<div style="display: none;">' + \
    gen_modal("E-commerce: Pet Supplies", "Transform a chaotic account into a transparent system prioritizing confirmed profit.", "Strategic Architecture", "Distributed roles: Search (High-Intent), Shopping (Catalog exposure), PMax (Calculated expansion). Segmented Dogs/Cats into isolated campaigns.", "funnel", "Search + PMax Integration", "Technical Execution", ["Audit revealed broad Shopping was overspending. Shifted budget to Search Layers.", "Isolated Brand demand from generic PMax noise.", "Point-wise management for key categories (Dogs vs. Cats) instead of flat assortment."], "Performance Results (Jan-Apr 2023 - Search)", "4,068", "Clicks", "819,247", "Value (UAH)", "420", "Conversions", 1) + \
    gen_modal("E-commerce: BBQ Grills", "Scale priority categories during seasonal peak.", "Strategic Architecture", "Priority-Driven Allocation: High-margin focus in PMax.", "growth", "Scaling Velocity", "Technical Execution", ["Reorganized inventory by margin groups.", "DSA layers for seasonal queries.", "Enhanced GA4 tracking accuracy."], "Performance Results", "6.1M", "Impressions", "€157.6k", "Sales Value", "1,693", "Conversions", 2) + \
    gen_modal("B2B: Logistics", "Cleanliness of B2B intent and lead flow stabilization.", "Strategic Architecture", "B2B Intent Filter: Rigorous negative keyword logic.", "funnel", "B2B Lead Funnel", "Technical Execution", ["Brand traffic isolation.", "DSA for long-tail service queries.", "Streamlined lead funneling."], "Performance Results", "1.9M", "Impressions", "€10.3k", "Ad Spend", "1,090", "Inquiries", 3) + \
    gen_modal("E-commerce: Electronics", "Maximize manageability across large SKU set.", "Strategic Architecture", "Tiered Performance Strategy: Grouped by ROAS performance.", "growth", "Inventory Growth", "Technical Execution", ["Segmented priority segments.", "Robust Search for top-sellers.", "Remarketing for high-value carts."], "Performance Results", "4.3M", "Impressions", "€51.6k", "Sales Value", "1,178", "Conversions", 4) + \
    gen_modal("Local Services: Repair", "Defend target CPA in hyper-competitive local auction.", "Strategic Architecture", "Hyper-Local Radius Strategy: Precision zone targeting.", "funnel", "Geo-Targeting Logic", "Technical Execution", ["Call-Only mobile campaigns.", "Aggressive negative keyword exclusion.", "Bid optimization for peak hours."], "Performance Results", "€12", "Avg. CPA", "€10.2k", "Ad Spend", "850", "Phone Calls", 5) + \
    gen_modal("Industrial B2B: Tools", "Establish supply-chain focused funnel for wholesale.", "Strategic Architecture", "Supply-Chain Intent Focus: Wholesale & Industrial clusters.", "funnel", "Quality Filtering", "Technical Execution", ["Professional term isolation.", "Remarketing on technical price lists.", "B2B form mission tracking."], "Performance Results", "320", "Qualified Leads", "€45", "Target CPA", "€14.4k", "Ad Spend", 6) + \
    "</div>"

# --- RUSSIAN ---
ru_cards = [
    ("E-commerce: зоотовары", "Архитектура", "Трансформировали хаотичные траты в систему управления спросом. Изолировали прибыльный Search от широкого Shopping для стабилизации ROAS.", "4 068", "Кликов", "819k", "Value (грн)", 1, "Системный Вид"),
    ("E-commerce: товары для гриля", "Масштабирование", "Масштабирование категорий на основе приоритетов. Оптимизировали охват инвентаря: PMax для емкости и Search для маржинального спроса.", "€157.6k", "Value", "1,693", "Конв.", 2, "Системный Вид"),
    ("B2B: Логистика", "Лидогенерация", "Изолировали B2B-интент от общего объема. Построили прозрачную систему лидогенерации с изоляцией бренда и DSA-наполнением.", "€10.3k", "Расход", "1,090", "Конв.", 3, "Системный Вид"),
    ("E-commerce: электротовары", "Технический", "Многоуровневое масштабирование инвентаря. Усилили видимость PMax для топовых групп при контроле брендового поиска.", "€51.6k", "Value", "1,178", "Конв.", 4, "Системный Вид"),
    ("Услуги: Ремонт техники", "Эффективность", "Гиперлокальная радиусная стратегия. Защитили CPA в перегретой нише через точечный гео-таргетинг и Сall-центричную воронку.", "€12", "Avg. CPA", "850", "Звонков", 5, "Системный Вид"),
    ("Industrial B2B: Обородувание", "Стратегия", "Supply-chain фильтрация интента. Жесткая логика исключения розничного шума для захвата профессиональных покупателей.", "320", "Лидов", "€45", "CPA", 6, "Системный Вид")
]
ru_grid = '<div class="cases-grid">' + "".join([gen_grid_card(*c) for c in ru_cards])
ru_modals = '<div style="display: none;">' + \
    gen_modal("E-commerce: зоотовары", "Пересобрать архитектуру аккаунта для приоритета подтвержденного результата над широким охватом каталога.", "Стратегическая архитектура", "Распределение ролей: Search (сформированный спрос), Shopping (каталог), PMax (масштабирование). Изоляция категорий «Собаки/Кошки» для точечного управления.", "funnel", "Интеграция Search + PMax", "Техническая реализация", ["Анализ выявил перерасход в широком Shopping. Бюджет переведен в Search-слои.", "Изоляция бренда от общего шума архитектуры.", "Точечное управление приоритетами (Собаки/Кошки) вместо работы со всей массой ассортимента."], "Результаты (Янв-Апр 2023 - Search)", "4 068", "Кликов", "819 247", "Value (грн)", "420", "Конверсий", 1) + \
    gen_modal("E-commerce: товары для гриля", "Масштабировать приоритетные категории в пик сезона.", "Стратегическая архитектура", "Приоритетное масштабирование: Фокус на маржу в PMax.", "growth", "Динамика роста", "Техническая реализация", ["Пересборка под маржинальные группы.", "DSA для сезонного спроса.", "Уточнение отслеживания событий."], "Результаты", "6.1 млн", "Показов", "€157.6k", "Value", "1,693", "Конверсии", 2) + \
    gen_modal("B2B: Логистика", "Отсечь розничный (B2C) шум и стабилизировать заявки.", "Стратегическая архитектура", "B2B-фильтр интента: Глибокая логика минус-слов.", "funnel", "B2B Лид-воронка", "Техническая реализация", ["Изоляция бренда.", "DSA для низкочастотных услуг.", "Оптимизация воронки лида."], "Результаты", "1.9 млн", "Показов", "€10.3k", "Расход", "1,090", "B2B Лидов", 3) + \
    gen_modal("E-commerce: электротовары", "Повысить управляемость на большом массиве SKU.", "Стратегическая архитектура", "ROAS-стратегия: Группировка товаров по эффективности.", "growth", "Масштабирование SKU", "Техническая реализация", ["Выделиление приоритетов.", "PMax + Search для топов.", "Ремаркетинг для корзин."], "Результаты", "4.3 млн", "Показов", "€51.6k", "Value", "1,178", "Конверсий", 4) + \
    gen_modal("Услуги: Ремонт бытовой техники", "Защитить CPA в перегретых локальных аукционах.", "Стратегическая архитектура", "Радиусная стратегия: Точный гео-таргетинг.", "funnel", "Логика Гео-таргетинга", "Техническая реализация", ["Call-Only кампании.", "Агрессивные минус-слова.", "Оптимизация по часам пик."], "Результаты", "€12", "Avg. CPA", "€10.2k", "Расход", "850", "Звонков", 5) + \
    gen_modal("Industrial B2B: Обородувание", "Создать воронку под цепочки поставок.", "Стратегическая архитектура", "Supply-Chain фокус: Оптовые и индустриальные кластеры.", "funnel", "Фильтрация качества", "Техническая реализация", ["Изоляция профи-запросов.", "Ремаркетинг на прайс-листы.", "Отслеживание B2B-форм."], "Результаты", "320", "Квал. лидов", "€45", "Target CPA", "€14.4k", "Расход", 6) + \
    "</div>"

# --- UKRAINIAN ---
ua_cards = [
    ("E-commerce: зоотовари", "Архітектура", "Трансформували хаотичні витрати в систему управління попитом. Ізолювали прибутковий Search від широкого Shopping для стабілізації ROAS.", "4 068", "Кліків", "819k", "Value (грн)", 1, "Системний Вигляд"),
    ("E-commerce: товари для гриля", "Масштабування", "Масштабування категорій на основі пріоритетів. Оптимізували охоплення інвентарю: PMax для ємності та Search для маржинального попиту.", "€157.6k", "Value", "1,693", "Конв.", 2, "Системний Вигляд"),
    ("B2B: Логістика", "Лідогенерація", "Ізолювали B2B-інтент від загального обсягу. Побудували прозову систему лідогенерації з ізоляцією бренду та DSA-наповненням.", "€10.3k", "Витрати", "1,090", "Конв.", 3, "Системний Вигляд"),
    ("E-commerce: електротовари", "Технічний", "Багаторівневе масштабування інвентарю. Посилили видимість PMax для топових груп при контролі брендового пошуку.", "€51.6k", "Value", "1,178", "Конв.", 4, "Системний Вигляд"),
    ("Послуги: Ремонт техніки", "Ефективність", "Гіперлокальна радіусна стратегія. Захистили CPA у перегрітій ніші через точковий гео-таргетинг та Сall-центричну воронку.", "€12", "Avg. CPA", "850", "Дзвінків", 5, "Системний Вигляд"),
    ("Industrial B2B: Обладнання", "Стратегія", "Supply-chain фільтрація інтенту. Жорстка логіка виключення роздрібного шуму для захоплення лише професійних покупців.", "320", "Лідів", "€45", "CPA", 6, "Системний Вигляд")
]
ua_grid = '<div class="cases-grid">' + "".join([gen_grid_card(*c) for c in ua_cards])
ua_modals = '<div style="display: none;">' + \
    gen_modal("E-commerce: зоотовари", "Трансформувати хаотичний акаунт у прозору систему пріоритезації підтвердженого прибутку.", "Стратегічна архітектура", "Розподіл ролей: Search (Гарячий попит), Shopping (Каталог), PMax (Масштабування). Сегментація Собаки/Коти в ізольовані кампанії.", "funnel", "Інтеграція Search + PMax", "Технічна реалізація", ["Аналіз виявив перевитрати у широкому Shopping. Бюджет переведений у Search-шари.", "Ізоляція брендового попиту для запобігання розмиттю маржі.", "Точкове управління категоріями (Собаки/Коти) замість роботи з усією масою асортименту."], "Результати (Січ-Квіт 2023 - Search)", "4 068", "Кліків", "819 247", "Value (грн)", "420", "Конверсій", 1) + \
    gen_modal("E-commerce: товари для гриля", "Масштабувати пріоритетні категорії у пік сезону.", "Стратегічна архитектура", "Пріоритетне масштабування: Фокус на маржу в PMax.", "growth", "Динаміка росту", "Технічна реалізація", ["Перезбирання під маржинальні групи.", "DSA для сезонного попиту.", "Уточнення відстеження подій."], "Результати", "6.1 млн", "Показів", "€157.6k", "Value", "1,693", "Конверсії", 2) + \
    gen_modal("B2B: Логістика", "Відсікти роздрібний (B2C) шум та стабілізувати заявки.", "Стратегічна архітектура", "B2B-фільтр інтенту: Глибока логіка мінус-слів.", "funnel", "B2B Лід-воронка", "Технічна реалізація", ["Ізоляція бренду.", "DSA для низькочастотних послус.", "Оптимізація воронки ліда."], "Результати", "1.9 млн", "Показів", "€10.3k", "Витрати", "1,090", "B2B Лідів", 3) + \
    gen_modal("E-commerce: електротовари", "Підвищити керованість на великому масиві SKU.", "Стратегічна архітектура", "ROAS-стратегія: Групування товарів за ефективністю.", "growth", "Масштабування SKU", "Технічна реалізація", ["Виділення пріоритетів.", "PMax + Search для топів.", "Ремаркетинг для кошиків."], "Результати", "4.3 млн", "Показів", "€51.6k", "Value", "1,178", "Конверсій", 4) + \
    gen_modal("Послуги: Ремонт побутової техніки", "Захистити CPA у перегрітих локальних аукціонах.", "Стратегічна архітектура", "Радіусна стратегія: Точний гео-таргетинг.", "funnel", "Логіка Гео-таргетингу", "Технічна реалізація", ["Call-Only кампанії.", "Агрессивні мінус-слова.", "Оптимізація за годинами пік."], "Результати", "€12", "Avg. CPA", "€10.2k", "Витрати", "850", "Дзвінків", 5) + \
    gen_modal("Industrial B2B: Обладнання", "Створити воронку під ланцюжки поставок.", "Стратегічна архітектура", "Supply-Chain фокус: Оптові та індустріальні кластеры.", "funnel", "Фільтрація якості", "Технічна реалізація", ["Ізоляція профі-запутів.", "Ремаркетинг на прайс-листи.", "Відстеження B2B-форм."], "Результати", "320", "Квал. лідів", "€45", "Target CPA", "€14.4k", "Витрати", 6) + \
    "</div>"

# --- EXECUTION ---
replace_in_file('c:/Users/User/Кейсы/index.html', en_grid, en_modals, read_encoding='utf-8')
replace_in_file('c:/Users/User/Кейсы/ru_hidden.html', ru_grid, ru_modals, read_encoding='utf-8')
replace_in_file('c:/Users/User/Кейсы/ua.html', ua_grid, ua_modals, read_encoding='utf-8')

print("All language versions updated successfully with visual anchors.")
