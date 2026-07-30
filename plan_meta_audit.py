import json
import os

with open('meta_report.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

plan = "# Auditoria de Meta Tags e SEO\n\n"
plan += "## User Review Required\n"
plan += "> [!IMPORTANT]\n> O plano a seguir contém as correções exatas para as Meta Tags (Title, Description, Canonical, OG, Twitter, etc.). Nenhuma alteração estrutural do `<body>`, conteúdo visual, CSS ou JavaScript será feita.\n\n"
plan += "## Problemas Encontrados e Correções Propostas\n\n"

for file, meta in report.items():
    plan += f"### {file}\n"
    
    issues = []
    fixes = []
    
    # Title
    if not meta['title']:
        issues.append("Ausência de Title.")
        fixes.append("Adicionar tag <title> adequada.")
    elif len(meta['title']) > 1:
        issues.append(f"Duplicação de Title ({len(meta['title'])} tags).")
        fixes.append("Remover tags <title> excedentes, mantendo apenas uma.")
    else:
        title = meta['title'][0]
        if len(title) > 65:
            issues.append(f"Title muito longo ({len(title)} caracteres).")
            fixes.append("Reduzir Title para até 60-65 caracteres.")
            
    # Description
    if not meta['description']:
        issues.append("Ausência de Meta Description.")
        fixes.append("Adicionar <meta name='description'> relevante.")
    elif len(meta['description']) > 1:
        issues.append(f"Duplicação de Meta Description ({len(meta['description'])} tags).")
        fixes.append("Manter apenas uma Meta Description consolidada.")
    else:
        desc = meta['description'][0]
        if len(desc) > 160:
            issues.append(f"Meta Description muito longa ({len(desc)} caracteres).")
            fixes.append("Reduzir Description para até 160 caracteres.")
            
    # Canonical
    if not meta['canonical']:
        issues.append("Ausência de Canonical.")
        fixes.append(f"Adicionar <link rel='canonical' href='https://criaacao.com/{os.path.basename(file)}'>.")
    elif len(meta['canonical']) > 1:
        issues.append(f"Duplicação/Conflito de Canonical ({len(meta['canonical'])} tags).")
        fixes.append(f"Manter apenas o Canonical correto apontando para o próprio arquivo ou página oficial.")
    else:
        # Check if canonical is correct for trabalhe-conosco
        if file == 'trabalhe-conosco.html' and 'contato.html' in meta['canonical'][0]:
            issues.append("Conflito: Canonical de Trabalhe Conosco aponta para Contato.")
            fixes.append("Atualizar Canonical para apontar para trabalhe-conosco.html.")
            
    # Robots
    if not meta['robots']:
        issues.append("Ausência de Meta Robots.")
        fixes.append("Adicionar <meta name='robots' content='index,follow,max-image-preview:large'>.")
        
    # Viewport & Charset
    if not meta['viewport']:
        issues.append("Ausência de Viewport.")
        fixes.append("Adicionar tag de viewport padrão.")
    if not meta['charset']:
        issues.append("Ausência de Charset.")
        fixes.append("Adicionar <meta charset='utf-8'>.")
        
    # Author
    if not meta['author']:
        issues.append("Ausência de Meta Author.")
        fixes.append("Adicionar <meta name='author' content='CriaAção Entretenimento'>.")
        
    # Open Graph & Twitter
    if not meta['og']:
        issues.append("Ausência de tags Open Graph (og:title, og:image, etc).")
        fixes.append("Adicionar bloco completo de Open Graph pertinente à página.")
    else:
        # Check if worked-conosco copies contact OG
        if file == 'trabalhe-conosco.html' and 'contato.html' in meta['og'].get('og:url', [''])[0]:
            issues.append("Conflito: Tags Open Graph copiadas de Contato.")
            fixes.append("Atualizar OG Title, Description, e URL para Trabalhe Conosco.")
            
    if not meta['twitter']:
        issues.append("Ausência de Twitter Cards.")
        fixes.append("Adicionar bloco de Twitter Cards (twitter:card, twitter:title, etc).")
        
    if issues:
        for i, issue in enumerate(issues):
            plan += f"- **Problema**: {issue}\n  - *Impacto*: Prejudica indexação, compartilhamento social e CTR nos resultados do Google.\n  - *Correção*: {fixes[i]}\n"
    else:
        plan += "- Todas as Meta Tags essenciais estão implementadas e válidas.\n"
        
    plan += "\n"
    
plan += "## Plano de Ação (Implementação)\n"
plan += "Escreverei um script Python com `BeautifulSoup` que varrerá a seção `<head>` de todas as páginas, removendo tags duplicadas/lixo (ex: `assets/..._file.html`), ajustando os comprimentos textuais (quando extrapolarem 160 caracteres), inserindo Autor, Twitter Cards e Open Graph únicos por página, corrigindo Canonicals e Viewports sem alterar absolutamente nada fora da tag `<head>`.\n\n"

plan += "## Verification Plan\n"
plan += "### Automated Tests\n"
plan += "- Re-executar a extração do `<head>` para garantir 1 Canonical, 1 Description, 1 Title por arquivo.\n"
plan += "- Checar presença e singularidade de OG e Twitter Cards.\n"

with open(r'C:\Users\gilma\.gemini\antigravity-ide\brain\9005844e-b627-4981-9208-ce543088285d\implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(plan)
