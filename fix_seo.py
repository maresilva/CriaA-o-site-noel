import os
import re

def fix_file(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 1. Main tag: replace <div id="Content"> with <main id="Content"> and its closing tag
    # We can do this with regex, assuming standard structure.
    # Actually, a safer way to add <main> if <div id="Content"> exists:
    content = re.sub(r'<div([^>]*id=["\']Content["\'][^>]*)>', r'<main\1>', content)
    # The closing tag of #Content is hard to find with regex. Let's just find the last </div> before Footer and change it.
    # This is tricky with regex.
    pass

