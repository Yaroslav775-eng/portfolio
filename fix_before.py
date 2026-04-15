with open('index.html', encoding='utf-8') as f:
    c = f.read()

old_style = 'style="font-size: 0.8rem; color: var(--accent-brand); font-family: var(--font-sans); font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.04em;"'
new_class = 'class="case-before"'

count = c.count(old_style)
c = c.replace(old_style, new_class)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print(f'Replaced {count} occurrences of Before inline style -> .case-before class')
