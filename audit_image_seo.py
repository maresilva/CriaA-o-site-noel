import os
import glob
import re
from bs4 import BeautifulSoup
import json
from collections import defaultdict

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

images_data = []
og_images = []
backgrounds = []

generic_alts = ['image', 'imagem', 'foto', 'foto de', 'imagem de', 'logo', 'banner', 'picture', 'pic']
bad_filenames = re.compile(r'^(img|image|foto|pic|banner|final|captura|whatsapp|untitled)\b', re.IGNORECASE)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Open Graph Image
    og_img = soup.find('meta', property='og:image')
    if og_img:
        og_images.append({
            'page': filepath,
            'content': og_img.get('content', '')
        })
        
    # IMG Tags
    for img in soup.find_all('img'):
        src = img.get('src', '')
        alt = img.get('alt')
        title = img.get('title', '')
        classes = img.get('class', [])
        
        filename = os.path.basename(src)
        
        # Determine context/function
        context = 'geral'
        if img.find_parent('a'):
            context = 'link/funcional'
        if 'logo' in src.lower() or 'logo' in str(classes).lower():
            context = 'logo'
        if 'portfolio' in src.lower() or 'portfolio' in filepath.lower():
            context = 'portfolio'
        if 'clientes' in src.lower():
            context = 'cliente'
            
        is_decorative = False
        if alt == "" or 'decor' in str(classes).lower() or 'icon' in src.lower():
            is_decorative = True
            
        problems = []
        if alt is None:
            problems.append('Sem alt')
        elif alt == "" and not is_decorative:
            problems.append('Alt vazio em imagem potencial')
        elif alt != None:
            alt_lower = alt.lower()
            if any(alt_lower.startswith(x) for x in generic_alts) or alt_lower in generic_alts:
                problems.append('Alt genérico ou com "foto de"')
            
        if bad_filenames.search(filename) or len(filename) > 60 or '%' in filename:
            problems.append('Nome de arquivo inadequado')
            
        images_data.append({
            'page': filepath,
            'src': src,
            'filename': filename,
            'alt': alt if alt is not None else "[NULL]",
            'title': title,
            'context': context,
            'decorative': is_decorative,
            'problems': problems
        })
        
    # CSS Backgrounds (inline and simple classes)
    for tag in soup.find_all(style=True):
        style = tag['style']
        bg_match = re.search(r'background-image:\s*url\([\'"]?([^\'"\)]+)[\'"]?\)', style, re.IGNORECASE)
        if bg_match:
            backgrounds.append({
                'page': filepath,
                'tag': tag.name,
                'src': bg_match.group(1)
            })

# Analytics
total_images = len(images_data)
no_alt = [img for img in images_data if '[NULL]' in img['alt']]
empty_alt = [img for img in images_data if img['alt'] == '']
bad_alt = [img for img in images_data if 'Alt genérico ou com "foto de"' in img['problems']]
bad_names = [img for img in images_data if 'Nome de arquivo inadequado' in img['problems']]

alt_counts = defaultdict(int)
for img in images_data:
    if img['alt'] not in ['[NULL]', '']:
        alt_counts[img['alt']] += 1
duplicated_alts = {k: v for k, v in alt_counts.items() if v > 1}

print("=== IMAGE SEO AUDIT ===")
print(f"Total Imagens Analisadas: {total_images}")
print(f"Imagens sem Alt: {len(no_alt)}")
print(f"Imagens com Alt Vazio: {len(empty_alt)}")
print(f"Imagens com Alt Genérico/Ruim: {len(bad_alt)}")
print(f"Arquivos com nomes inadequados: {len(bad_names)}")
print(f"Backgrounds encontrados: {len(backgrounds)}")

print("\n--- Exemplos Nomes Inadequados ---")
for img in bad_names[:10]:
    print(f"- {img['filename']} (em {img['page']})")
    
print("\n--- Exemplos Alts Repetidos ---")
for k, v in list(duplicated_alts.items())[:10]:
    print(f"- {k}: {v} vezes")
    
print("\n--- OG Images ---")
for og in og_images[:5]:
    print(f"- {og['page']}: {og['content']}")
    
with open('image_seo_audit_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total': total_images,
        'images': images_data,
        'backgrounds': backgrounds,
        'og_images': og_images
    }, f, indent=2, ensure_ascii=False)
