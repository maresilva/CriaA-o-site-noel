import os, re, shutil

os.makedirs('solucoes/_blocks', exist_ok=True)

I = {
    'star': '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>',
    'ppl': '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
    'cam': '<rect x="2" y="4" width="20" height="16" rx="2" ry="2"></rect><circle cx="12" cy="12" r="3"></circle><path d="M8 4V2"></path><path d="M16 4V2"></path>',
    'clk': '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    'chk': '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline>',
    'shd': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
    'spk': '<path d="M12 19l7-7 3 3-7 7-3-3z"></path><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"></path><path d="M2 2l7.586 7.586"></path><circle cx="11" cy="11" r="2"></circle>',
    'gft': '<polyline points="20 12 20 22 4 22 4 12"></polyline><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>',
}

def si(p, c='sc-solution-icon', s=24):
    return f'<svg class="{c}" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24">{p}</svg>'

def sc(icon, title, desc):
    return f'<div class="sc-solution-card">{si(icon)}<h3>{title}</h3><p>{desc}</p></div>'

def bc(icon, title, desc):
    return f'<div class="sc-benefit-card">{si(icon, "sc-benefit-icon", 40)}<h3 class="sc-benefit-title">{title}</h3><p class="sc-benefit-text">{desc}</p></div>'

CS = '<style>.sc-solutions-section{position:relative;width:100%;background:linear-gradient(180deg,#0a0102 0%,#1a0304 50%,#0a0102 100%);padding:80px 0}.sc-solutions-container{width:100%;max-width:1280px;margin:0 auto;padding:0 40px;box-sizing:border-box}.sc-solutions-eyebrow{font-family:Inter,sans-serif;font-size:13px;font-weight:700;letter-spacing:.15em;color:#F2B84B;text-transform:uppercase;text-align:center;margin-bottom:12px}.sc-solutions-title{font-family:var(--mfn-heading-font-family,Cinzel,serif);font-size:clamp(24px,3vw,36px);font-weight:700;color:#fff;line-height:1.2;margin:0 0 56px 0;text-align:center}.sc-solutions-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.sc-solution-card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:32px 24px;transition:all .3s ease;display:flex;flex-direction:column;height:100%;box-sizing:border-box}.sc-solution-card:hover{background:rgba(255,255,255,.06);border-color:rgba(242,184,75,.3);transform:translateY(-4px)}.sc-solution-icon{color:var(--ca-gold-500,#F2B84B);width:36px;height:36px;margin-bottom:20px;flex-shrink:0}.sc-solution-card h3{font-family:Inter,sans-serif;font-size:14px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:.06em;margin:0 0 12px 0;line-height:1.3}.sc-solution-card p{font-family:Inter,sans-serif;font-size:14px;line-height:1.6;color:rgba(255,255,255,.6);margin:0}@media(max-width:1024px){.sc-solutions-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:768px){.sc-solutions-section{padding:60px 0}.sc-solutions-container{padding:0 20px}.sc-solutions-grid{grid-template-columns:1fr}.sc-solutions-title{margin-bottom:40px}}</style>'

CB = '<style>.sc-benefits-section{position:relative;width:100%;background:linear-gradient(180deg,#0a0102 0%,#1a0304 50%,#0a0102 100%);padding:80px 0}.sc-benefits-container{width:100%;max-width:1280px;margin:0 auto;padding:0 40px;box-sizing:border-box}.sc-benefits-title{font-family:var(--mfn-heading-font-family,Cinzel,serif);font-size:clamp(24px,3vw,36px);font-weight:700;color:#fff;line-height:1.2;margin:0 0 56px 0;text-align:center}.sc-benefits-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}.sc-benefit-card{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:32px 24px;text-align:center;transition:all .3s ease;display:flex;flex-direction:column;align-items:center;height:100%;box-sizing:border-box}.sc-benefit-card:hover{background:rgba(255,255,255,.06);border-color:rgba(242,184,75,.3);transform:translateY(-4px)}.sc-benefit-icon{color:var(--ca-gold-500,#F2B84B);width:40px;height:40px;margin-bottom:20px;flex-shrink:0}.sc-benefit-title{font-family:Inter,sans-serif;font-size:14px;font-weight:700;color:#fff;text-transform:uppercase;letter-spacing:.06em;margin:0 0 12px 0;line-height:1.3}.sc-benefit-text{font-family:Inter,sans-serif;font-size:14px;line-height:1.6;color:rgba(255,255,255,.6);margin:0}@media(max-width:1024px){.sc-benefits-grid{grid-template-columns:repeat(2,1fr)}}@media(max-width:768px){.sc-benefits-section{padding:60px 0}.sc-benefits-container{padding:0 20px}.sc-benefits-title{margin-bottom:40px}.sc-benefits-grid{grid-template-columns:1fr}}</style>'

# ==== BUILD ESCOLAS SOLUTIONS BLOCK ====
esc_sol = f'<section class="sc-solutions-section">{CS}<div class="sc-solutions-container"><div class="sc-solutions-eyebrow">EXPERIENCIAS PARA A ESCOLA</div><h2 class="sc-solutions-title">Formatos adaptados a rotina e ao espaco escolar</h2><div class="sc-solutions-grid">{sc(I["star"],"VISITA DO PAPAI NOEL","Encontro preparado para diferentes faixas etarias, com interacao mediada pelos educadores e respeito ao ritmo das criancas.")}{sc(I["cam"],"ESPACOS FOTOGRAFICOS","Cenarios planejados para registros da turma, dos alunos com o Papai Noel e das familias durante o evento.")}{sc(I["ppl"],"PERSONAGENS DE APOIO","Mamae Noel, duendes e outros personagens para tornar a experiencia mais rica e envolvente.")}{sc(I["chk"],"ORGANIZACAO POR TURMAS","Planejamento de horarios e fluxo para atender diferentes grupos sem sobrecarregar o ambiente escolar.")}{sc(I["gft"],"KITS E ATIVIDADES","Materiais complementares que podem ser integrados a experiencia de acordo com o formato escolhido.")}{sc(I["clk"],"PLANEJAMENTO CONJUNTO","Cada projeto e construido em parceria com a direcao e a equipe pedagogica da instituicao.")}</div></div></section>'

# ==== BUILD EMPRESAS BENEFITS BLOCK ====
emp_ben = f'<section class="sc-benefits-section">{CB}<div class="sc-benefits-container"><h2 class="sc-benefits-title">Por que empresas de todo o Brasil confiam na Criacao</h2><div class="sc-benefits-grid">{bc(I["shd"],"EXPERTISE COMPROVADA","Mais de 30 anos desenvolvendo experiencias para marcas e corporacoes de diferentes portes e segmentos.")}{bc(I["spk"],"PROJETO EXCLUSIVO","Cada experiencia e desenvolvida sob medida, alinhada a identidade, aos valores e aos objetivos da sua empresa.")}{bc(I["ppl"],"OPERACAO COMPLETA","Equipe dedicada para planejamento, producao, coordenacao, execucao e desmontagem do evento.")}{bc(I["clk"],"FLEXIBILIDADE DE FORMATO","Atendemos confraternizacoes, convencoes, campanhas internas, acoes promocionais e eventos para familias.")}</div></div></section>'

# ==== INJECT INTO ESCOLAS ====
with open('solucoes/escolas.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Find the exact gap between process close and benefits open
# Process section closes, then there's a newline, then benefits opens
gap_marker = '</section>\n\n\n    <!-- ==============================================\n         ETAPA 6: DIFERENCIAIS'
# If the exact comment varies, use a broader match
proc_section_marker = 'class="sc-process-section"'
proc_start = c.index(proc_section_marker)

# Count sections to find the closing tag
depth = 0
proc_end = 0
for m in re.finditer(r'<(section|/section)', c[proc_start:]):
    if m.group(1) == 'section':
        depth += 1
    else:
        depth -= 1
        if depth == 0:
            proc_end = proc_start + m.end()
            break

if proc_end == 0:
    print('ERROR: could not find process section end')
    exit(1)

# Insert the solutions block right after process closing </section>
result = c[:proc_end + 1] + '\n' + esc_sol + '\n' + c[proc_end + 1:]

with open('solucoes/escolas.html', 'w', encoding='utf-8') as f:
    f.write(result)

secs = re.findall(r'<section[^>]*class="(sc-\w+(?:-\w+)*)"', result)
print('Escolas:', ' > '.join(secs), f'({len(result)} bytes)')

# ==== INJECT INTO EMPRESAS ====
with open('solucoes/empresas-e-corporativo.html', 'r', encoding='utf-8') as f:
    c = f.read()

sol_marker = 'class="sc-solutions-section"'
sol_start = c.index(sol_marker)

depth = 0
sol_end = 0
for m in re.finditer(r'<(section|/section)', c[sol_start:]):
    if m.group(1) == 'section':
        depth += 1
    else:
        depth -= 1
        if depth == 0:
            sol_end = sol_start + m.end()
            break

if sol_end == 0:
    print('ERROR: could not find solutions section end')
    exit(1)

result = c[:sol_end + 1] + '\n' + emp_ben + '\n' + c[sol_end + 1:]

with open('solucoes/empresas-e-corporativo.html', 'w', encoding='utf-8') as f:
    f.write(result)

secs = re.findall(r'<section[^>]*class="(sc-\w+(?:-\w+)*)"', result)
print('Empresas:', ' > '.join(secs), f'({len(result)} bytes)')

print('Done!')
