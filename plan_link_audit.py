import json

with open('link_audit_results.json', 'r', encoding='utf-8') as f:
    report = json.load(f)

plan = "# Plano de Ação: Estrutura de Links Internos (Internal Linking)\n\n"
plan += "## User Review Required\n"
plan += "> [!IMPORTANT]\n> A auditoria mapeou toda a malha de links do site. Identificamos problemas técnicos (arquitetura Clean URL) e oportunidades de semântica. NENHUM conteúdo visível será alterado. Aprovação necessária para executar a higienização dos `href`.\n\n"

plan += "## Problemas Técnicos Identificados\n\n"

violations = len(report['clean_url_violations'])
if violations > 0:
    plan += f"### 1. Violação de Clean URLs (Redirecionamentos Internos)\n"
    plan += f"- **Problema**: Foram encontradas {violations} instâncias de links internos apontando para arquivos com a extensão `.html` (ex: `href=\"contato.html\"`). Como o servidor usa Clean URLs, todo clique do usuário sofre um redirecionamento interno (308) desperdiçando Crawl Budget e atrasando o carregamento.\n"
    plan += f"- **Correção**: Atualizaremos todos os `href` internos para remover a extensão `.html` (ex: `href=\"/contato\"`). O `index.html` será encurtado para a raiz `/`.\n\n"

broken = len(report['broken_links'])
if broken > 0:
    plan += f"### 2. Links Quebrados (Broken Links)\n"
    plan += f"- **Problema**: Detectamos {broken} links apontando para arquivos inexistentes.\n"
    plan += f"- **Correção**: Corrigir os caminhos baseados na estrutura real das pastas.\n\n"
else:
    plan += "### 2. Links Quebrados\n- Nenhum link quebrado encontrado entre as páginas principais da malha.\n\n"

orphans = len(report['orphans'])
if orphans > 0:
    plan += f"### 3. Páginas Órfãs (Sem Autoridade)\n"
    plan += f"- **Problema**: {', '.join(report['orphans'])} não recebem nenhum link interno.\n"
    plan += f"- **Correção**: Como não podemos criar conteúdo novo ou links no layout, a recomendação (Sugestão) é adicionar links no footer ou header futuramente.\n\n"
else:
    plan += "### 3. Páginas Órfãs\n- Todas as 8 páginas comerciais estão conectadas na malha de navegação (nenhuma página principal órfã detectada).\n\n"

plan += "## Oportunidades e Sugestões (Auditoria de Anchor Text)\n\n"
generics = [a for a in report['anchor_texts'] if a.get('issue') == 'Generic Anchor']
if generics:
    plan += f"- **Anchor Texts Genéricos**: Detectamos o uso de termos genéricos como 'Saiba mais' ou 'Clique aqui'.\n"
    plan += f"  - *Sugestão de Melhoria Futura (Não será executado agora)*: Trocar por âncoras descritivas como 'Saiba mais sobre a Plataforma 360' para distribuir relevância de palavra-chave (PageRank).\n\n"
else:
    plan += "- **Anchor Texts**: Boa distribuição, sem uso excessivo de termos genéricos como 'clique aqui' nos links de texto puros mapeados.\n\n"

plan += "## Plano de Execução Técnica\n"
plan += "Escreverei um script Python com Expressões Regulares (Regex) ou BeautifulSoup para varrer os atributos `href` das tags `<a>` de todas as páginas. Substituiremos ocorrências de `arquivo.html` pelo caminho limpo `/arquivo`. Não tocaremos no texto âncora, preservando estritamente o conteúdo da interface.\n\n"

with open(r'C:\Users\gilma\.gemini\antigravity-ide\brain\9005844e-b627-4981-9208-ce543088285d\implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(plan)
