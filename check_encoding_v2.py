encodings = ['utf-8', 'windows-1251', 'latin-1', 'utf-16']
files = ['index.html', 'ua.html', 'ru_hidden.html']

for f in files:
    found = False
    for enc in encodings:
        try:
            with open(f, 'r', encoding=enc) as buf:
                buf.read()
            print(f"{f}: {enc}")
            found = True
            break
        except Exception:
            continue
    if not found:
        print(f"{f}: UNKNOWN")
