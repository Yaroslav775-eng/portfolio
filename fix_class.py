with open('index.html', encoding='utf-8') as f:
    c = f.read()

# Fix double class attribute - merge btn-text and case-cta into one
c = c.replace('class="btn-text" class="case-cta"', 'class="btn-text case-cta"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

count = c.count('class="btn-text case-cta"')
print(f'Fixed {count} double class attributes')
