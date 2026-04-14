import sys

with open('ua.html', 'r', encoding='windows-1251') as f:
    lines = f.readlines()
    for line in lines[250:300]: # Check a section with cases
        print(line, end='')
