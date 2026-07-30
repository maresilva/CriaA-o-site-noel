plan = """# Plano de Ação: Otimização de SEO Local (Google Maps & NAP)

## User Review Required
> [!IMPORTANT]
> A auditoria revelou que o site não possui ancoragem geográfica. O robô do Google não consegue ter "certeza" de que a empresa atua no Ceará, o que prejudica severamente o rankeamento em buscas como "Papai Noel em Fortaleza". **Nenhuma mudança visual** será feita, agiremos apenas no código (Head, Schema e Links). Aguardo sua aprovação.

## Problemas Técnicos Identificados

### 1. Ausência de Meta Tags Geográficas (Geo.Position)
- **Problema**: O cabeçalho HTML atual do site não envia coordenadas para o motor de busca.
- **Correção**: Injetaremos as *Geo Meta Tags* oficiais (`geo.region`, `geo.placename`, `geo.position` e `ICBM`) no `<head>` de todas as páginas, ancorando a empresa digitalmente nas coordenadas de Fortaleza, CE.

### 2. Schema de Negócio Local Incompleto (Horários e Geo)
- **Problema**: O nosso Schema atual diz que a empresa existe, mas não diz que horas funciona nem qual a coordenada exata no mapa. Isso impede que o site ganhe aquele "card" destacado na direita das buscas do Google.
- **Correção**: Atualizaremos o JSON-LD `LocalBusiness` em todas as páginas para incluir os nós de `openingHoursSpecification` (Segunda a Sexta, 08h-18h) e as propriedades de latitude e longitude.

### 3. Links de Telefone Inativos (Click-to-Call)
- **Problema**: Muitas vezes desenvolvedores esquecem de usar a âncora `<a href="tel:...">` nos telefones espalhados pelo site, impedindo que usuários em celulares cliquem e liguem diretamente. 
- **Correção**: O script vai escanear o HTML e garantir que qualquer número de telefone textual receba a tag técnica `tel:`, sem alterar o visual ou o texto da página, e garantindo consistência NAP (Name, Address, Phone).

## Perguntas em Aberto

> [!WARNING]
> Como não tenho acesso ao endereço físico exato da matriz da empresa, usarei as coordenadas centrais de Fortaleza (-3.731862, -38.526670) e um horário comercial padrão (Seg-Sex, 08:00 - 18:00) exclusivamente para o código de SEO (não aparecerá no visual). **Se você estiver de acordo com isso, basta clicar em Proceed / Aprovar**.

## Plano de Execução Técnica
Construirei um script Python que injetará as tags meta no `<head>`, regerará o nó `LocalBusiness` no JSON-LD já existente (adicionando os horários e geo) e varrerá o `<body>` para envelopar números soltos com a tag `<a href="tel:...">` caso existam.
"""

with open(r'C:\Users\gilma\.gemini\antigravity-ide\brain\9005844e-b627-4981-9208-ce543088285d\implementation_plan.md', 'w', encoding='utf-8') as f:
    f.write(plan)
