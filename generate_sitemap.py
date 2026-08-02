import os
import glob
import re
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.criaacao.com"
HTML_FILES = glob.glob('*.html') + glob.glob('solucoes/*.html')

# Exclusions
EXCLUDE_HTML = ['design_system1.html', 'missing_footer.html', 'scratch_idx.html', 'header_standard.html', 'new_segment.html', '404.html']
EXCLUDE_IMG_KEYWORDS = ['icon', 'logo', 'cookie', 'dummy', 'shape', 'separador', 'banner-cookies', 'clientes']

def is_eligible_image(img_tag, filepath):
    src = img_tag.get('src', '')
    alt = img_tag.get('alt', '')
    
    if not src: return False
    
    # 1. Purely decorative via alt
    if alt == "": return False
    
    # 2. Excluded keywords in filename/path
    src_lower = src.lower()
    for kw in EXCLUDE_IMG_KEYWORDS:
        if kw in src_lower:
            return False
            
    # 3. Check if broken locally (simulated via local path)
    if not src.startswith('http'):
        if filepath.startswith('solucoes'):
            local_path = os.path.join(os.path.dirname(filepath), '..', src)
        else:
            local_path = src
        local_path = os.path.normpath(local_path).lstrip('\\/')
        if not os.path.exists(local_path):
            return False
            
    return True

def get_canonical_url(filepath, soup):
    # Try to find canonical tag
    canonical = soup.find('link', rel='canonical')
    if canonical and canonical.get('href'):
        return canonical.get('href')
        
    # Fallback deduction
    clean_path = filepath.replace('\\', '/').replace('.html', '')
    if clean_path == 'index':
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{clean_path}"

def get_absolute_img_url(src):
    if src.startswith('http'):
        return src
    src = src.lstrip('./')
    return f"{BASE_URL}/{src}"

def generate_sitemap():
    # Header
    xml = []
    xml.append('<?xml version="1.0" encoding="UTF-8"?>')
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">')
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    for filepath in HTML_FILES:
        if any(ex in filepath for ex in EXCLUDE_HTML):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        page_url = get_canonical_url(filepath, soup)
        
        # Collect unique valid images
        page_images = set()
        for img in soup.find_all('img'):
            if is_eligible_image(img, filepath):
                abs_src = get_absolute_img_url(img.get('src'))
                page_images.add(abs_src)
                
        # Generate URL block
        xml.append('  <url>')
        xml.append(f'    <loc>{page_url}</loc>')
        xml.append(f'    <lastmod>{today}</lastmod>') # Only updating lastmod on script run, removing priority/changefreq
        
        for img_url in sorted(page_images):
            xml.append('    <image:image>')
            xml.append(f'      <image:loc>{img_url}</image:loc>')
            xml.append('    </image:image>')
            
        xml.append('  </url>')
        
    xml.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(xml))
        
if __name__ == '__main__':
    generate_sitemap()
    print("Sitemap gerado com sucesso em sitemap.xml")
