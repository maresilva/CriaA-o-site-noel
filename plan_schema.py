plan = """# Plano de Ação: Otimização de Schema Markup (Dados Estruturados)

## User Review Required
> [!IMPORTANT]
> A auditoria do JSON-LD encontrou vários erros de duplicação, copy-paste (copiar e colar) incorreto e sintaxe inválida segundo o Google. Vou recriar a arquitetura de Dados Estruturados para refletir a semântica de cada página. Nenhuma mudança de design será feita.

## Problemas Técnicos Identificados

### 1. Breadcrumbs Quebrados (Falso Positivo)
- **Problema**: Todas as páginas do site possuem um `BreadcrumbList` no Schema, mas ele está fixo e *hardcoded* apenas com o item "Home". O Google exige que a trilha reflita exatamente a URL atual (ex: na página de Contato, a trilha deve ser Home > Contato).
- **Correção**: Recriarei as trilhas de Breadcrumb dinamicamente em cada arquivo `.html` para que reflitam a profundidade real (ex: Home > Soluções > Manual do Papai Noel).

### 2. Uso Errado de `WebSite` em Páginas Internas
- **Problema**: A tag `WebSite` está sendo injetada em páginas internas como "Trabalhe Conosco" (e com o título errado "Fale Conosco"). Segundo as diretrizes do Google, a entidade `WebSite` deve existir prioritariamente na Home. As páginas internas devem usar `WebPage`.
- **Correção**: Excluirei o nó `WebSite` das páginas internas e injetarei a entidade correta `WebPage`, apontando o título e URL exatos da página atual.

### 3. Página de Eventos sem Schema (Órfã Semântica)
- **Problema**: A página `eventos.html` é a única do site que não possui absolutamente nenhum dado estruturado. Ela está invisível para os Rich Snippets do Google.
- **Correção**: Injetarei todo o pacote de Schema básico nela (`Organization`, `LocalBusiness`, `WebPage`, `BreadcrumbList`).

### 4. SearchAction e FAQ
- **Diagnóstico**: O prompt pediu auditoria de `SearchAction` e `FAQ`. Como o layout atual do site não possui uma barra de busca interna (Search Box) nem uma sessão de Perguntas Frequentes explícita, a injeção dessas marcações seria considerada *Spam de Schema* pelo Google (violação das diretrizes).
- **Ação**: Não injetaremos `SearchAction` nem `FAQ` para manter a conformidade legal do SEO.

## Plano de Execução Técnica
Usarei um script Python para encontrar a tag `<script type="application/ld+json">` de todas as páginas. Apagarei o conteúdo atual e reconstruirei o JSON-LD injetando o array `@graph` limpo, focado na entidade correta (`WebPage` para internas, `WebSite` para index), corrigindo os Breadcrumbs e adicionando o nó na página de Eventos.
"""

with open(r'C:\Users\gilma\.gemini\antigravity-ide\brain\9005844e-b627-4981-9208-ce543088285d\implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(plan)
