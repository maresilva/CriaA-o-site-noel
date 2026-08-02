import os
import glob
import re
import subprocess
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://www.criaacao.com"
HTML_FILES = [f for f in glob.glob('*.html') + glob.glob('solucoes/*.html') 
              if not any(ex in f for ex in ['design_system1.html', 'missing_footer.html', 'scratch_idx.html', 'header_standard.html', 'new_segment.html', '404.html'])]

EXCLUDE_IMG_KEYWORDS = ['icon', 'cookie', 'dummy', 'shape', 'separador', 'banner-cookies']

def get_git_lastmod(filepath):
    try:
        # Get the last commit date for the file
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%Y-%m-%d', '--', filepath],
            capture_output=True, text=True, check=True
        )
        date_str = result.stdout.strip()
        if date_str:
            return date_str
    except Exception:
        pass
    return None

def is_eligible_image(img_tag, filepath):
    # Check explicit data attribute
    explicit_sitemap = img_tag.get('data-image-sitemap')
    if explicit_sitemap == 'false':
        return False
    if explicit_sitemap == 'true':
        return True
        
    src = img_tag.get('src', '')
    alt = img_tag.get('alt', '')
    
    if not src: return False
    
    # Exclude decorative
    if alt == "": return False
    
    # Main institutional logo shouldn't repeat 20 times. 
    # Usually the header logo is 'logo-criaacao-entretenimento' inside a link or header.
    # We can exclude it if it's exactly the main logo, but allow others.
    if 'logo-criaacao-entretenimento.webp' in src or 'logo-criaacao-entretenimento.png' in src:
        # Only index the main logo on the homepage
        if filepath != 'index.html':
            return False
            
    # Keywords
    src_lower = src.lower()
    for kw in EXCLUDE_IMG_KEYWORDS:
        if kw in src_lower:
            return False
            
    # Local exist validation for build step
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
    canonical = soup.find('link', rel='canonical')
    if canonical and canonical.get('href'):
        return canonical.get('href')
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
    xml = []
    xml.append('<?xml version="1.0" encoding="UTF-8"?>')
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">')
    
    for filepath in HTML_FILES:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        page_url = get_canonical_url(filepath, soup)
        lastmod = get_git_lastmod(filepath)
        
        page_images = set()
        for img in soup.find_all('img'):
            if is_eligible_image(img, filepath):
                abs_src = get_absolute_img_url(img.get('src'))
                page_images.add(abs_src)
                
        xml.append('  <url>')
        xml.append(f'    <loc>{page_url}</loc>')
        if lastmod:
            xml.append(f'    <lastmod>{lastmod}</lastmod>')
            
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
    print("Sitemap gerado com sucesso!")
