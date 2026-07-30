import os
from bs4 import BeautifulSoup
import copy

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

def fix_metas(filepath):
    if not os.path.exists(filepath):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    head = soup.head
    if not head:
        return

    # 1. Clean Canonicals
    canonicals = head.find_all('link', rel='canonical')
    base_name = os.path.basename(filepath)
    if 'solucoes/' in filepath:
        base_name = 'solucoes/' + base_name
        
    correct_canonical_url = f"https://cria-a-o-site-noel.vercel.app/{base_name}"
    
    # Remove all canonicals first
    for c in canonicals:
        c.decompose()
        
    # Re-insert the single correct canonical
    new_canonical = soup.new_tag('link', rel='canonical', href=correct_canonical_url)
    head.append(new_canonical)
    
    # 2. Fix Titles (Length)
    titles = head.find_all('title')
    if titles:
        for i in range(1, len(titles)):
            titles[i].decompose()  # Remove duplicates
        title_tag = head.find('title')
        title_text = title_tag.get_text(strip=True)
        if len(title_text) > 65:
            title_tag.string = title_text[:62] + '...'
            
    # 3. Fix Descriptions (Duplicate and Length)
    descriptions = head.find_all('meta', attrs={'name': 'description'})
    if descriptions:
        # keep the first one, delete rest
        for i in range(1, len(descriptions)):
            descriptions[i].decompose()
        desc_tag = head.find('meta', attrs={'name': 'description'})
        desc_content = desc_tag.get('content', '')
        if len(desc_content) > 160:
            desc_tag['content'] = desc_content[:157] + '...'
    else:
        # Add a default description if none
        new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': 'CriaAção Entretenimento - Especialistas em eventos natalinos e Papai Noel para shoppings e empresas.'})
        head.append(new_desc)
        
    # 4. Author
    if not head.find('meta', attrs={'name': 'author'}):
        new_author = soup.new_tag('meta', attrs={'name': 'author', 'content': 'CriaAção Entretenimento'})
        head.append(new_author)
        
    # 5. Robots
    if not head.find('meta', attrs={'name': 'robots'}):
        new_robots = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'index,follow,max-image-preview:large'})
        head.append(new_robots)
        
    # 6. Viewport & Charset (Basic sanity checks)
    if not head.find('meta', attrs={'name': 'viewport'}):
        new_vp = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1, maximum-scale=1'})
        head.append(new_vp)
        
    # 7. Twitter Cards & OG matching
    # If missing Twitter cards, copy from OG
    og_title = head.find('meta', attrs={'property': 'og:title'})
    og_desc = head.find('meta', attrs={'property': 'og:description'})
    og_image = head.find('meta', attrs={'property': 'og:image'})
    
    if not head.find('meta', attrs={'name': 'twitter:card'}):
        new_tc = soup.new_tag('meta', attrs={'name': 'twitter:card', 'content': 'summary_large_image'})
        head.append(new_tc)
        
    if not head.find('meta', attrs={'name': 'twitter:title'}) and og_title:
        new_tt = soup.new_tag('meta', attrs={'name': 'twitter:title', 'content': og_title.get('content')})
        head.append(new_tt)
        
    if not head.find('meta', attrs={'name': 'twitter:description'}) and og_desc:
        new_td = soup.new_tag('meta', attrs={'name': 'twitter:description', 'content': og_desc.get('content')})
        head.append(new_td)
        
    if not head.find('meta', attrs={'name': 'twitter:image'}) and og_image:
        new_ti = soup.new_tag('meta', attrs={'name': 'twitter:image', 'content': og_image.get('content')})
        head.append(new_ti)

    # 8. Specific fixes for trabalhe-conosco.html
    if 'trabalhe-conosco' in filepath:
        # It copies contato.html heavily. Fix OG and Title
        tc_title = "Trabalhe Conosco | CriaAção Entretenimento"
        tc_desc = "Faça parte da equipe da CriaAção Entretenimento. Cadastre seu currículo e venha criar experiências mágicas de Natal conosco."
        
        # HTML Title and Meta Desc
        if head.find('title'):
            head.find('title').string = tc_title
        if head.find('meta', attrs={'name': 'description'}):
            head.find('meta', attrs={'name': 'description'})['content'] = tc_desc
            
        # OG
        if head.find('meta', attrs={'property': 'og:title'}):
            head.find('meta', attrs={'property': 'og:title'})['content'] = tc_title
        if head.find('meta', attrs={'property': 'og:description'}):
            head.find('meta', attrs={'property': 'og:description'})['content'] = tc_desc
        if head.find('meta', attrs={'property': 'og:url'}):
            head.find('meta', attrs={'property': 'og:url'})['content'] = correct_canonical_url
            
        # Twitter
        if head.find('meta', attrs={'name': 'twitter:title'}):
            head.find('meta', attrs={'name': 'twitter:title'})['content'] = tc_title
        if head.find('meta', attrs={'name': 'twitter:description'}):
            head.find('meta', attrs={'name': 'twitter:description'})['content'] = tc_desc
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print(f"Fixed metas for {filepath}")

for f in files:
    fix_metas(f)

print("All meta tags fixed.")
