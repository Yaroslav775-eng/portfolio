import os

# Original detected encoding was windows-1251
# But the meta tag says UTF-8. 
# We need to read it as windows-1251 and save as utf-8 to be consistent with the meta tag.

try:
    with open('ua.html', 'r', encoding='windows-1251') as f:
        content = f.read()
    
    # Save as UTF-8
    with open('ua.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("ua.html converted to UTF-8 successfully.")
except Exception as e:
    print(f"Error converting ua.html: {e}")
