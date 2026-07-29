import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all id and class attributes of divs, sections, or articles that end with -section
sections = re.findall(r'<div[^>]*class=["\']([^"\']*section[^"\']*)["\']', content)
sections += re.findall(r'<section[^>]*class=["\']([^"\']*section[^"\']*)["\']', content)

print("Unique Section Classes Found:")
for s in sorted(set(sections)):
    print(s)
