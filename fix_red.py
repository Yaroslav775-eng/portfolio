with open('index.html', encoding='utf-8') as f:
    c = f.read()

# Fix 1: System View buttons — change inline color from red to black
c = c.replace(
    'style="color:var(--accent-brand); background:transparent; border:none; text-align:left; font-weight:bold; cursor:pointer; font-family:var(--font-sans);text-transform:uppercase;font-size:0.8rem; margin-top: 16px;"',
    'class="case-cta"'
)

# Fix 2: Compare table — remove val-plus class (red) from table cells
# Change val-plus values to just bold text
c = c.replace('class="val-plus"', 'style="font-weight:700; color: var(--text-dark);"')

# Fix 3: Timeline first entry — remove red accent from Channel Factory date
c = c.replace(
    'font-size: 0.85rem; font-weight: 700; color: var(--accent-brand); text-transform: uppercase; margin-bottom: 8px;',
    'font-size: 0.85rem; font-weight: 700; color: var(--text-gray); text-transform: uppercase; margin-bottom: 8px;'
)

count_sv = c.count('case-cta')
print(f'System View buttons converted: check')
print(f'Done.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('index.html saved.')
