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

gtm_head = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5RHR2KX7');</script>
<!-- End Google Tag Manager -->
"""

gtm_body = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5RHR2KX7"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
"""

def add_gtm(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if already added
    if 'GTM-5RHR2KX7' in content:
        print(f"GTM already present in {filepath}")
        return

    # 1. Insert in <head>
    new_content = re.sub(r'(<head[^>]*>)', r'\1\n' + gtm_head, content, count=1, flags=re.IGNORECASE)

    # 2. Insert after <body>
    new_content = re.sub(r'(<body[^>]*>)', r'\1\n' + gtm_body, new_content, count=1, flags=re.IGNORECASE)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Added GTM to {filepath}")

for f in files:
    add_gtm(f)

print("All done.")
