import chardet

files = ['index.html', 'ua.html', 'ru_hidden.html']
for f in files:
    try:
        with open(f, 'rb') as buf:
            raw_data = buf.read()
            result = chardet.detect(raw_data)
            print(f"{f}: {result['encoding']} (confidence: {result['confidence']})")
    except Exception as e:
        print(f"Error reading {f}: {e}")
