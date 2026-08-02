import glob
import os
from bs4 import BeautifulSoup
import urllib.request
import json

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

results = {
    'missing_width_height': 0,
    'lazy_hero': 0,
    'render_blocking_css': 0,
    'sync_js': 0,
    'external_fonts': 0
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # Check images for CLS (missing width/height)
    images = soup.find_all('img')
    for img in images:
        if not img.get('width') or not img.get('height'):
            results['missing_width_height'] += 1
            
    # Check hero image for lazy loading (LCP issue)
    hero_section = soup.find(class_=lambda x: x and 'hero' in x)
    if hero_section:
        hero_imgs = hero_section.find_all('img')
        for img in hero_imgs:
            if img.get('loading') == 'lazy':
                results['lazy_hero'] += 1
                
    # Check CSS for render blocking
    links = soup.find_all('link', rel='stylesheet')
    for link in links:
        if link.get('media') != 'print' and not link.has_attr('onload'):
            results['render_blocking_css'] += 1
            
    # Check JS
    scripts = soup.find_all('script')
    for script in scripts:
        if script.get('src'):
            if not script.has_attr('defer') and not script.has_attr('async') and not script.has_attr('type') == 'module':
                results['sync_js'] += 1
                
    # Check external fonts
    font_links = soup.find_all('link', href=lambda x: x and 'fonts.googleapis.com' in x)
    results['external_fonts'] += len(font_links)

print("--- AUDIT RESULTS ---")
print(f"Images missing width/height (CLS Risk): {results['missing_width_height']}")
print(f"Hero images lazy loaded (LCP Risk): {results['lazy_hero']}")
print(f"Render blocking CSS: {results['render_blocking_css']}")
print(f"Synchronous JS (TBT Risk): {results['sync_js']}")
print(f"External Font calls: {results['external_fonts']}")

# Check large local images
print("\n--- LARGE IMAGES (>300KB) ---")
img_files = glob.glob('assets/images/**/*.*', recursive=True)
for img in img_files:
    size_kb = os.path.getsize(img) / 1024
    if size_kb > 300:
        print(f"{img}: {size_kb:.2f} KB")
