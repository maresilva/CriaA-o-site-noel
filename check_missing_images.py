import os
from bs4 import BeautifulSoup
import re

files = ['index.html', 'solucoes.html']

for filepath in files:
    print(f"\n--- Checking {filepath} ---")
    if not os.path.exists(filepath):
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
            
    soup = BeautifulSoup(content, 'html.parser')
    
    # Check <img> src
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith('http') and not src.startswith('data:'):
            # Check if file exists
            if not os.path.exists(src):
                print(f"[MISSING IMG TAG] {src}")
                
    # Check background-image
    styles = re.findall(r'url\([\'"]?(.*?)[\'"]?\)', content)
    for src in styles:
        if src and not src.startswith('http') and not src.startswith('data:'):
            # If the path is relative to css file it might fail this naive check, 
            # but inline styles are relative to html
            if not os.path.exists(src):
                print(f"[MISSING BG-IMAGE] {src}")

