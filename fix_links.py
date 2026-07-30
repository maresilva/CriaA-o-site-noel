import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        continue
        
    original_content = content
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        # Skip truncated <link> or <noscript> lines
        if stripped.startswith('<link') and stripped.endswith("this.media='all'\""):
            continue
        if stripped.startswith('<noscript><link') and stripped.endswith("this.media='all'\""):
            continue
            
        # Clean up the surviving <link> lines that have the print/onload hack
        if '<link' in line and 'rel="stylesheet"' in line and 'media="print"' in line:
            # Replace media="print" onload="..." with media="all"
            line = re.sub(r'media="print"\s*onload=["\'].*?["\']', 'media="all"', line)
            
        new_lines.append(line)
        
    content = '\n'.join(new_lines)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
