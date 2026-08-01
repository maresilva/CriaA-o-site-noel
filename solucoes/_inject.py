"""Simple injector — inserts blocks before <!-- START INSTITUTIONAL CONTACT SECTION -->"""
import sys

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def save(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  Saved: {len(content)} bytes')

MARKER = '<!-- START INSTITUTIONAL CONTACT SECTION -->'

# ============= SHOPPING CENTERS =============
# Order: solutions, benefits, gallery, faq
print('=== Shopping Centers ===')
c = load('solucoes/shopping-centers.html')
blocks_sh = load('solucoes/_blocks/shopping_solutions.html') + \
            load('solucoes/_blocks/shopping_benefits.html') + \
            load('solucoes/_blocks/shopping_gallery.html') + \
            load('solucoes/_blocks/shopping_faq.html')
c = c.replace(MARKER, blocks_sh + '\n\n' + MARKER)
save('solucoes/shopping-centers.html', c)
del c, blocks_sh

# ============= GESTÃO PÚBLICA =============
print('=== Gestão Pública ===')
c = load('solucoes/gestao-publica.html')
blocks_gp = load('solucoes/_blocks/gestao_solutions.html') + \
            load('solucoes/_blocks/gestao_benefits.html') + \
            load('solucoes/_blocks/gestao_gallery.html') + \
            load('solucoes/_blocks/gestao_faq.html')
c = c.replace(MARKER, blocks_gp + '\n\n' + MARKER)
save('solucoes/gestao-publica.html', c)
del c, blocks_gp

# ============= ESCOLAS =============
print('=== Escolas ===')
c = load('solucoes/escolas.html')
blocks_esc = load('solucoes/_blocks/escolas_solutions.html')
c = c.replace(MARKER, blocks_esc + '\n\n' + MARKER)
save('solucoes/escolas.html', c)
del c, blocks_esc

# ============= EMPRESAS =============
print('=== Empresas ===')
c = load('solucoes/empresas-e-corporativo.html')
blocks_emp = load('solucoes/_blocks/empresas_benefits.html')
c = c.replace(MARKER, blocks_emp + '\n\n' + MARKER)
save('solucoes/empresas-e-corporativo.html', c)

print('\nAll done.')
