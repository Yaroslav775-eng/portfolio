import os
import shutil
import glob
import subprocess
import sys

# Проверяем наличие библиотеки markdown или устанавливаем её
try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "--quiet"])
    import markdown

desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
out_dir = os.path.join(desktop, 'Готовые_Кейсы_HTML')
os.makedirs(out_dir, exist_ok=True)

md_files = glob.glob(r'C:\Users\User\Кейсы\*.md')

html_template = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f4f7f6;
        }}
        .container {{
            background: #fff;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.05);
        }}
        h1, h2, h3, h4 {{
            color: #2c3e50;
            margin-top: 1.5em;
        }}
        h1 {{
            font-size: 2.2em;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 10px;
            margin-top: 0;
        }}
        code {{
            background: #f1f2f6;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: 'Consolas', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: #2f3640;
            color: #f5f6fa;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }}
        pre code {{
            background: transparent;
            color: inherit;
            padding: 0;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 8px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            border: 1px solid #ddd;
            text-align: left;
        }}
        th {{
            background-color: #f8f9fa;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 0;
            padding-left: 16px;
            color: #666;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

for md_path in md_files:
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    html_content = markdown.markdown(text, extensions=['extra', 'tables'])
    filename = os.path.basename(md_path)
    title = filename.replace('.md', '')
    
    final_html = html_template.format(title=title, content=html_content)
    
    out_path = os.path.join(out_dir, title + '.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

# Также копируем отчет Utec на рабочий стол, если вы имели в виду его
utec_report = r"c:\Users\User\OneDrive\Документы\Антигравити проверка форм Ютек\utec_audit\report.html"
if os.path.exists(utec_report):
    try:
        shutil.copy2(utec_report, os.path.join(desktop, 'utec_report.html'))
    except Exception as e:
        print(f"Не удалось скопировать отчет Utec: {e}")

print("✅ Все файлы успешно сохранены на Рабочий Стол!")
