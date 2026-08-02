import os
import glob
import re
from bs4 import BeautifulSoup

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

BASE_URL = 'https://www.criaacao.com'

# Mapping for specific pages to OG Images
og_mapping = {
    'solucoes/shopping-centers.html': f'{BASE_URL}/assets/images/gallery/Acoes-Tematicas-e1720275059494-criaacao-entretenimento.png',
    'solucoes/empresas-e-corporativo.html': f'{BASE_URL}/assets/images/backgrounds/background-768x543-criaacao-entretenimento.png',
    'solucoes/escolas.html': f'{BASE_URL}/assets/images/gallery/Brindes-e1720275106833-criaacao-entretenimento.png',
    'solucoes/hospitais.html': f'{BASE_URL}/assets/images/gallery/Duendes-e1720275042996-criaacao-entretenimento.png',
    'solucoes.html': f'{BASE_URL}/assets/images/gallery/Plataforma-360o-e1720275137989-criaacao-entretenimento.png'
}

def process_img_tag(img_tag_orig):
    img_tag = img_tag_orig
    
    # Extract src
    src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
    if not src_match:
        return img_tag_orig
        
    src = src_match.group(1).lower()
    
    # Extract current alt
    alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
    current_alt = alt_match.group(1) if alt_match else None
    
    new_alt = None
    
    # Rule 1: Logos
    if 'logo-criaacao' in src or 'logo-1' in src:
        new_alt = "CriaAção Entretenimento"
        
    # Rule 2: Decorative icons
    elif 'icon' in src or 'cookies' in src or 'dummy' in src or 'separador' in src or 'shape' in src:
        new_alt = ""
        
    # Rule 3: Clients (Informative context)
    elif 'clientes/' in src:
        # Extract client name from filename
        basename = os.path.basename(src).split('.')[0]
        # Remove dimensions like -150x150
        basename = re.sub(r'-\d+x\d+', '', basename)
        if re.match(r'^\d+-criaacao', basename):
            pass # Keep original alt (don't overwrite new_alt)
        else:
            basename = basename.replace('-', ' ').title()
            if basename.lower() == 'rio mar': basename = "RioMar"
            if basename.lower() == 'via sul': basename = "Via Sul"
            new_alt = f"Shopping {basename}"
        
    # Apply new alt
    if new_alt is not None:
        if alt_match:
            # replace existing alt
            img_tag = img_tag[:alt_match.start(1)] + new_alt + img_tag[alt_match.end(1):]
        else:
            # inject alt
            img_tag = img_tag.replace('<img ', f'<img alt="{new_alt}" ')
            
    return img_tag

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    new_html = html
    
    # 1. Update OG Image
    og_img = og_mapping.get(filepath.replace('\\', '/'))
    if og_img:
        # find the meta property="og:image"
        new_html = re.sub(
            r'(<meta property=["\']og:image["\'] content=["\'])([^"\']+)(["\']\s*/?>)',
            r'\g<1>' + og_img + r'\g<3>',
            new_html
        )
        
    # 2. Process all IMG tags safely using the multi-line logic
    img_tags = re.findall(r'<img[^>]+>', new_html, re.IGNORECASE)
    
    for img_tag_orig in set(img_tags): 
        replacement = process_img_tag(img_tag_orig)
        if replacement != img_tag_orig:
            new_html = new_html.replace(img_tag_orig, replacement)
            
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html)
        print(f"Updated SEO Image attributes: {filepath}")

print("Image SEO Fixes completed.")
