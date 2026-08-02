import os
import glob
import re

html_files = glob.glob('*.html') + glob.glob('solucoes/*.html')

def fix_portfolio_alt(img_tag_orig):
    img_tag = img_tag_orig
    src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag, re.IGNORECASE)
    if not src_match:
        return img_tag_orig
    src = src_match.group(1).lower()
    
    # Only target portfolio/gallery images that are not logos or icons
    if 'portfolio' in src or 'gallery' in src:
        if 'logo' in src or 'icon' in src or 'dummy' in src or 'cookies' in src:
            return img_tag_orig
            
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
        current_alt = alt_match.group(1) if alt_match else ""
        
        # If the alt looks like it was generated from filename or is too generic
        new_alt = current_alt
        
        # Remove spammy prefixes
        new_alt = re.sub(r'^(imagem de|foto de|imagem do|foto do|imagem|foto)\s+', '', new_alt, flags=re.IGNORECASE)
        new_alt = new_alt.strip()
        
        # Specific fixes based on known bad alts
        if "papai noel shopping iguatemi bosque mar fortaleza" in current_alt.lower():
            new_alt = "Cenografia natalina produzida no Shopping Iguatemi Bosque Fortaleza"
        elif "papai noel e noeletes shopping via sul fortaleza" in current_alt.lower():
            new_alt = "Papai Noel e Noeletes em ação no Shopping Via Sul Fortaleza"
        elif "mockup livro manual" in current_alt.lower():
            new_alt = "Manual do Verdadeiro Papai Noel (Livro)"
        elif "trono do papai noel shopping parangaba" in current_alt.lower():
            new_alt = "Trono do Papai Noel decorado no Shopping Parangaba"
        elif "parada de natal shopping iguatemi" in current_alt.lower():
            new_alt = "Parada de Natal com personagens no Shopping Iguatemi"
        elif "entrega especial papai noel shopping benfica" in current_alt.lower():
            new_alt = "Entrega especial com Papai Noel no Shopping Benfica"
        elif "papai noel noeletes na poltrona 1993" in current_alt.lower():
            new_alt = "Papai Noel e Noeletes em poltrona temática de Natal (1993)"
        elif "papai noel com crianca" in current_alt.lower():
            new_alt = "Papai Noel entregando presente para criança"
            
        # Capitalize first letter
        if len(new_alt) > 0:
            new_alt = new_alt[0].upper() + new_alt[1:]
            
        if new_alt != current_alt:
            if alt_match:
                img_tag = img_tag[:alt_match.start(1)] + new_alt + img_tag[alt_match.end(1):]
            else:
                img_tag = img_tag.replace('<img ', f'<img alt="{new_alt}" ')
                
    return img_tag

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    new_html = html
    img_tags = re.findall(r'<img[^>]+>', new_html, re.IGNORECASE)
    
    for img_tag_orig in set(img_tags): 
        replacement = fix_portfolio_alt(img_tag_orig)
        if replacement != img_tag_orig:
            new_html = new_html.replace(img_tag_orig, replacement)
            
    if new_html != html:
        with open(filepath, 'w', encoding='utf-8', newline='') as f:
            f.write(new_html)
        print(f"Fixed Portfolio Alts in: {filepath}")
