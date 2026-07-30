import os
import re

files = [
    'index.html',
    'portfolio.html',
    'quem-somos.html',
    'solucoes.html',
    'contato.html',
    'eventos.html',
    'solucoes/manual-do-verdadeiro-papai-noel.html',
    'trabalhe-conosco.html'
]

gtag_snippet = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DQ41K14CVV"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-DQ41K14CVV');
</script>
"""

def add_gtag(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already added
    if 'G-DQ41K14CVV' in content:
        print(f"GTM already present in {filepath}")
        return

    # Find the <head> tag and insert right after it
    # <head> could have attributes or be just <head>
    # We use regex to insert the snippet after the opening <head> tag
    new_content = re.sub(r'(<head[^>]*>)', r'\1' + gtag_snippet, content, count=1, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Added GTM to {filepath}")

for f in files:
    add_gtag(f)

print("All done.")
