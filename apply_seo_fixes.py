import os
from bs4 import BeautifulSoup

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

def fix_html(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    # 1. Main tag wrapper
    if not soup.find('main'):
        # In BeTheme, usually the main content is inside <div id="Content">
        content_div = soup.find('div', id='Content')
        if content_div:
            content_div.name = 'main'
            
    # 2. Fix multiple headers / navs in eventos.html (and generally)
    headers = soup.find_all('header')
    if len(headers) > 1:
        # Keep the first one (usually #Top_bar or #Header), convert rest to div
        for h in headers[1:]:
            h.name = 'div'
            h['class'] = h.get('class', []) + ['header-semantic-fix']
            
    navs = soup.find_all('nav')
    if len(navs) > 1:
        # Usually the first one or the one with id="menu" is the real nav
        # Let's keep the one inside the first header, convert others
        real_nav = soup.find('header').find('nav') if soup.find('header') else navs[0]
        for n in navs:
            if n != real_nav and n != navs[0]:
                n.name = 'div'
                n['class'] = n.get('class', []) + ['nav-semantic-fix']
                
    # 3. Headings Hierarchy & Single H1
    h1s = soup.find_all('h1')
    if len(h1s) > 1:
        for h in h1s[1:]:
            h.name = 'h2'
            
    # Fix skipped headings (e.g. h2 -> h4)
    # We'll just pass through all headings and ensure we don't skip a level
    current_level = 1
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        level = int(tag.name[1])
        if level > current_level + 1:
            # skipped! e.g. current is h2, this is h4
            # We promote it to current_level + 1
            new_level = current_level + 1
            tag.name = f'h{new_level}'
            current_level = new_level
        else:
            current_level = level

    # 4. Empty links missing aria-label
    for a in soup.find_all('a'):
        text = a.get_text(strip=True)
        if not text and not a.get('aria-label'):
            href = a.get('href', '')
            if 'wa.me' in href or 'whatsapp' in href.lower():
                a['aria-label'] = 'Fale conosco no WhatsApp'
            elif 'instagram' in href.lower():
                a['aria-label'] = 'Visite nosso Instagram'
            elif '#' in href or not href:
                a['aria-label'] = 'Ação ou Link'
            else:
                a['aria-label'] = 'Link'

    # 5. Form Inputs missing label / aria-label
    for input_tag in soup.find_all(['input', 'textarea', 'select']):
        type_ = input_tag.get('type')
        if type_ in ['hidden', 'submit', 'button', 'radio', 'checkbox']:
            continue
            
        has_id = input_tag.get('id')
        has_aria = input_tag.get('aria-label')
        has_label = False
        
        if has_id:
            label = soup.find('label', attrs={'for': has_id})
            if label:
                has_label = True
                
        parent_label = input_tag.find_parent('label')
        if parent_label:
            has_label = True
            
        if not has_label and not has_aria:
            name = input_tag.get('name', 'campo')
            input_tag['aria-label'] = f"Preencha o campo {name}"

    with open(filepath, 'w', encoding='utf-8') as f:
        # Use str(soup) to keep it as original as possible without re-indenting everything
        f.write(str(soup))
    print(f"Fixed SEO and A11y in {filepath}")

for f in files:
    fix_html(f)

print("Done all fixes.")
