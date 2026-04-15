import os
import re

# Regex patterns to find correct injection points
# Looking for the cases-grid container and the modals storage div
cases_grid_regex = re.compile(r'<div class="cases-grid">.*?</div>\s*</div>\s*</section>', re.DOTALL)
modals_regex = re.compile(r'<div style="display: none;">.*?</div>\s*<!-- JS Logic -->', re.DOTALL)

def replace_in_file(filepath, grid_content, modals_content, read_encoding='utf-8'):
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        return
    
    print(f"Updating {filepath}...")
    try:
        with open(filepath, 'r', encoding=read_encoding) as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Update Grid
    new_grid = grid_content + "\n        </div>\n    </section>"
    content = cases_grid_regex.sub(new_grid, content)
    
    # Update Modals
    new_modals = modals_content + "\n    <!-- JS Logic -->"
    content = modals_regex.sub(new_modals, content)

    # Always write as UTF-8
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# --- GRID CARD GEN ---
def gen_grid_card(category, title, m_val, m_lbl, btn_text, case_id):
    return f"""
                <div class="case-card reveal-on-scroll" onclick="openModal('case-{case_id}')">
                    <span class="case-meta">{category}</span>
                    <h3 class="case-title">{title}</h3>
                    <div class="case-result-box">
                        <strong>{m_val}</strong>
                        <span>{m_lbl}</span>
                    </div>
                    <div class="case-cta">{btn_text} <span>&rarr;</span></div>
                </div>"""

# --- MODAL GEN ---
def gen_modal(title, highlight, outcome_label, metrics, case_id):
    metric_items = "".join([f'<div class="modal-metric"><span class="modal-metric-val">{m[0]}</span><span class="modal-metric-lbl">{m[1]}</span></div>' for m in metrics])
    return f"""
        <div id="data-case-{case_id}">
            <h2>{title}</h2>
            <div class="highlight-box">{highlight}</div>
            <h4>{outcome_label}</h4>
            <div class="modal-metrics-grid">
                {metric_items}
            </div>
        </div>"""

# --- ENGLISH DATA ---
en_cards_data = [
    ("E-commerce / Architecture", "Pet Supplies: Scalable Search & PMax Ecosystem", "800–1200% ROAS", "Consistent monthly performance with €4.35 CPA.", "System View", 1),
    ("E-commerce / Scaling", "BBQ Grills: Seasonal Demand Capture", "679% ROAS", "High-margin product focus during peak window.", "System View", 2),
    ("B2B / Lead Generation", "Logistics: Intent Filtering & DSA Layers", "€11.5 CPL", "1,090 qualified business leads in 90 days.", "System View", 3),
    ("E-commerce / Technical", "Electronics: Multi-Tier Inventory Scaling", "653% ROAS", "Dynamic budget allocation based on product margin.", "System View", 4),
    ("Local Services / Efficiency", "Repair: Hyper-Local Radius Strategy", "€12 CPA", "850 booked jobs via mobile call-only funnels.", "System View", 5),
    ("Industrial B2B / Strategy", "Industrial Tools: Supply-Chain Intent Filter", "320 Leads", "Removing retail noise to capture wholesale buyers.", "System View", 6)
]

en_modals_data = [
    (1, "E-commerce: Pet Supplies", "Replaced chaotic catalog spend with structured demand capture layers. Isolated high-value Search from broad Shopping for predictable ROI.", "The Outcome", [("800–1200%", "ROAS"), ("€4.35", "Avg. CPA"), ("34.9k", "Conversions")]),
    (2, "E-commerce: BBQ Grills", "Priority-driven category scaling. Optimized inventory exposure using PMax for reach and Search for capturing high-margin intent.", "The Outcome", [("679%", "ROAS"), ("€13.7", "Avg. CPA"), ("€157.6k", "Sales Value")]),
    (3, "B2B: Logistics", "The company was getting clicks—but from individuals, not commercial clients. We built a traffic filter using rigorous negative keywords and DSA long-tail capture.", "The Outcome", [("€11.5", "Cost Per Lead"), ("1,090", "Qualified Leads"), ("€10.3k", "Ad Spend")]),
    (4, "E-commerce: Electronics", "Divided parts of the catalog into performance tiers. High-margin items got priority PMax budget while slow-stock items moved to conservative Shopping.", "The Outcome", [("653%", "ROAS"), ("€6.7", "Avg. CPA"), ("€51.6k", "Sales Value")]),
    (5, "Local Services: Repair", "Switched to a precision radius strategy: tight geo-zones, Call-Only mobile ads during working hours, and high-intensity bidding on local clusters.", "The Outcome", [("€12", "Avg. CPA"), ("850", "Booked Calls"), ("€10.2k", "Ad Spend")]),
    (6, "Industrial B2B: Tools", "Supply-chain search intent focus. Identified the language pro buyers use (wholesale, bulk, specs) and filtered out retail queries entirely.", "The Outcome", [("320", "Qualified Leads"), ("€45", "Target CPA"), ("€14.4k", "Ad Spend")])
]

# --- UKRAINIAN DATA ---
ua_cards_data = [
    ("E-commerce / Архітектура", "Зоотовари: Масштабована екосистема Search & PMax", "800–1200% ROAS", "Стабільна щомісячна ефективність із CPA €4.35.", "Системний огляд", 1),
    ("E-commerce / Масштабування", "Товари для гриля: Захоплення сезонного попиту", "679% ROAS", "Фокус на високомаржинальних товарах у пік сезону.", "Системний огляд", 2),
    ("B2B / Лідогенерація", "Логістика: Фільтрація інтенту та DSA-шари", "€11.5 CPL", "1,090 кваліфікованих бізнес-лідів за 90 днів.", "Системний огляд", 3),
    ("E-commerce / Технічний", "Електроніка: Багаторівневе масштабування інвентарю", "653% ROAS", "Динамічний розподіл бюджету на основі маржі.", "Системний огляд", 4),
    ("Послуги / Ефективність", "Ремонт: Гіперлокальна радіусна стратегія", "€12 CPA", "850 заброньованих робіт через Call-Only воронки.", "Системний огляд", 5),
    ("Industrial B2B / Стратегія", "Обладнання: Supply-Chain фільтр інтенту", "320 Лідів", "Видалення роздрібного шуму для захоплення опту.", "Системний огляд", 6)
]

ua_modals_data = [
    (1, "E-commerce: Зоотовари", "Трансформували хаотичні витрати каталогу в системні шари захоплення попиту. Відокремили прибутковий Search від Shopping для стабілізації ROI.", "Результат", [("800–1200%", "ROAS"), ("€4.35", "Середній CPA"), ("34.9k", "Конверсій")]),
    (2, "E-commerce: Товари для гриля", "Пріоритетне масштабування категорій. Оптимізували охоплення інвентарю: PMax для ємності та Search для маржинального попиту.", "Результат", [("679%", "ROAS"), ("€13.7", "Середній CPA"), ("€157.6k", "Виручка")]),
    (3, "B2B: Логістика", "Компанія отримувала кліки від приватних осіб, а не комерційних клієнтів. Ми побудували фільтр трафіку через мінус-слова та DSA-захоплення довгих хвостів.", "Результат", [("€11.5", "Ціна ліда"), ("1,090", "Кваліф. лідів"), ("€10.3k", "Витрати")]),
    (4, "E-commerce: Електроніка", "Розділили каталог на рівні ефективності. Високомаржинальні товари отримали пріоритетний PMax-бюджет, залежалі залишки перейшли в Shopping.", "Результат", [("653%", "ROAS"), ("€6.7", "Середній CPA"), ("€51.6k", "Виручка")]),
    (5, "Послуги: Ремонт техінки", "Перейшли на точну радіусну стратегію: щільні гео-зони, Call-Only мобільна реклама в робочий час та жорсткі ставки на локальні кластери.", "Результат", [("€12", "Середній CPA"), ("850", "Дзвінків"), ("€10.2k", "Витрати")]),
    (6, "Industrial B2B: Інструменти", "Фокус на пошукових намірах ланцюжків поставок. Визначили мову професійних закупників (опт, bulk, специфікації) та відфільтрували роздріб.", "Результат", [("320", "Квал. лідів"), ("€45", "Target CPA"), ("€14.4k", "Витрати")])
]

# --- GENERATION ---
en_grid_html = '<div class="cases-grid">' + "".join([gen_grid_card(*c) for c in en_cards_data])
en_modals_html = '<div style="display: none;">' + "".join([gen_modal(m[1], m[2], m[3], m[4], m[0]) for m in en_modals_data]) + '</div>'

ua_grid_html = '<div class="cases-grid">' + "".join([gen_grid_card(*c) for c in ua_cards_data])
ua_modals_html = '<div style="display: none;">' + "".join([gen_modal(m[1], m[2], m[3], m[4], m[0]) for m in ua_modals_data]) + '</div>'

# --- RUN ---
replace_in_file('c:/Users/User/Кейсы/index.html', en_grid_html, en_modals_html)
replace_in_file('c:/Users/User/Кейсы/ua.html', ua_grid_html, ua_modals_html)

print("Portfolio successfully updated with Entrepreneur-Ready Case Studies.")
