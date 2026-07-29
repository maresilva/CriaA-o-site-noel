import re

pages = [
    'quem-somos.html', 'solucoes.html', 'portfolio.html', 
    'eventos.html', 'contato.html', 'trabalhe-conosco.html'
]

results = {}

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for section classes
        sections = re.findall(r'<section[^>]*class=["\']([^"\']+)["\'][^>]*>', content)
        sections += re.findall(r'<div[^>]*class=["\']([^"\']*section[^"\']*)["\'][^>]*>', content)
        
        unique_classes = set()
        for cls_string in sections:
            for cls in cls_string.split():
                if 'section' in cls:
                    unique_classes.add(cls)
                    
        results[page] = sorted(unique_classes)
    except Exception as e:
        results[page] = str(e)

for page, classes in results.items():
    print(f"--- {page} ---")
    for cls in classes:
        print(cls)
