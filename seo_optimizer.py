import os
import re

pages_info = {
    "index.html": {
        "title": "CriaAção Entretenimento | Maior Empresa de Natal para Shopping Centers",
        "description": "Especialistas há mais de 30 anos em criar as maiores experiências natalinas para Shoppings e Empresas. Papai Noel, Cenografia e Ativações de alto padrão.",
        "url": "https://criaacao.com/"
    },
    "quem-somos.html": {
        "title": "Quem Somos | CriaAção Entretenimento - Especialistas em Eventos Natalinos",
        "description": "Conheça a história da CriaAção Entretenimento. Mais de 3 décadas de excelência em produções artísticas, cenografia e casting de Papai Noel.",
        "url": "https://criaacao.com/quem-somos"
    },
    "solucoes.html": {
        "title": "Soluções em Entretenimento e Decoração Natalina | CriaAção",
        "description": "Descubra nossas soluções completas: decoração, atrações, personagens, cenografia e casting de Papai Noel para encantar o seu público.",
        "url": "https://criaacao.com/solucoes"
    },
    "portfolio.html": {
        "title": "Portfólio de Projetos Natalinos e Cenografia | CriaAção Entretenimento",
        "description": "Explore os cases de sucesso e os grandes projetos natalinos já realizados pela CriaAção Entretenimento em todo o Brasil.",
        "url": "https://criaacao.com/portfolio"
    },
    "eventos.html": {
        "title": "Eventos e Produções Artísticas | CriaAção Entretenimento",
        "description": "Soluções incríveis para eventos corporativos, paradas de natal e campanhas temáticas que geram experiências inesquecíveis.",
        "url": "https://criaacao.com/eventos"
    },
    "contato.html": {
        "title": "Contato | Fale com a CriaAção Entretenimento",
        "description": "Entre em contato conosco e solicite um orçamento para transformar seu evento ou shopping com a magia do Natal. Atendimento especializado.",
        "url": "https://criaacao.com/contato"
    },
    "trabalhe-conosco.html": {
        "title": "Trabalhe Conosco | Vagas e Oportunidades na CriaAção",
        "description": "Faça parte da nossa equipe. Cadastre seu currículo e venha criar experiências mágicas com a CriaAção Entretenimento.",
        "url": "https://criaacao.com/trabalhe-conosco"
    },
    "404.html": {
        "title": "Página não encontrada | CriaAção Entretenimento",
        "description": "A página que você está procurando não existe ou foi removida. Volte para a página inicial.",
        "url": "https://criaacao.com/404.html",
        "noindex": True
    },
    "solucoes/shopping-centers.html": {
        "title": "Eventos Natalinos para Shopping Centers | CriaAção Entretenimento",
        "description": "Atraia mais clientes e gere encantamento com a melhor cenografia, personagens e o verdadeiro Papai Noel para o seu Shopping Center.",
        "url": "https://criaacao.com/solucoes/shopping-centers"
    },
    "solucoes/gestao-publica.html": {
        "title": "Eventos Natalinos para Gestão Pública e Prefeituras | CriaAção",
        "description": "Projetos de iluminação, paradas natalinas e decoração para espaços públicos. Leve a magia do Natal para a sua cidade com a CriaAção.",
        "url": "https://criaacao.com/solucoes/gestao-publica"
    },
    "solucoes/escolas.html": {
        "title": "Eventos Natalinos para Escolas | CriaAção Entretenimento",
        "description": "Momentos lúdicos e inesquecíveis para o encerramento do ano letivo. Personagens vivos, apresentações e Papai Noel para escolas.",
        "url": "https://criaacao.com/solucoes/escolas"
    },
    "solucoes/empresas-e-corporativo.html": {
        "title": "Eventos Natalinos Corporativos e para Empresas | CriaAção",
        "description": "Celebrações e confraternizações corporativas com atrações exclusivas. Surpreenda seus colaboradores e clientes neste Natal.",
        "url": "https://criaacao.com/solucoes/empresas-e-corporativo"
    },
    "solucoes/condominios-e-residencias.html": {
        "title": "Eventos Natalinos para Condomínios e Residências | CriaAção",
        "description": "Leve o clima festivo para o seu condomínio. Decoração de alto padrão e visita do Papai Noel para moradores e famílias.",
        "url": "https://criaacao.com/solucoes/condominios-e-residencias"
    },
    "solucoes/buffets-e-espacos-de-eventos.html": {
        "title": "Eventos Natalinos para Buffets e Espaços | CriaAção Entretenimento",
        "description": "Agregue valor aos seus pacotes de fim de ano com as atrações, personagens e decorações da CriaAção Entretenimento.",
        "url": "https://criaacao.com/solucoes/buffets-e-espacos-de-eventos"
    },
    "solucoes/hospitais.html": {
        "title": "Ações Natalinas Humanizadas para Hospitais | CriaAção",
        "description": "Ações solidárias e emocionantes. Visita do Papai Noel e personagens para levar esperança e alegria a pacientes e equipes de saúde.",
        "url": "https://criaacao.com/solucoes/hospitais"
    },
    "solucoes/creches.html": {
        "title": "Eventos Natalinos Lúdicos para Creches | CriaAção",
        "description": "Espetáculos adaptados para a primeira infância. Encantamento e magia com os personagens natalinos e o Papai Noel.",
        "url": "https://criaacao.com/solucoes/creches"
    },
    "solucoes/instituicoes-de-acolhimento.html": {
        "title": "Ações Natalinas para Instituições de Acolhimento | CriaAção",
        "description": "Leve carinho e a magia do Natal para abrigos e orfanatos com apresentações especiais e o encanto do Verdadeiro Papai Noel.",
        "url": "https://criaacao.com/solucoes/instituicoes-de-acolhimento"
    },
    "solucoes/manual-do-verdadeiro-papai-noel.html": {
        "title": "Manual do Verdadeiro Papai Noel | CriaAção Entretenimento",
        "description": "Conheça o nosso processo rigoroso e exclusivo de treinamento e formação dos melhores Papais Noéis profissionais do Brasil.",
        "url": "https://criaacao.com/solucoes/manual-do-verdadeiro-papai-noel"
    }
}

tags_to_remove = [
    r'<title[\s>].*?</title>',
    r'<meta\s+[^>]*name=["\']description["\'][^>]*>',
    r'<link\s+[^>]*rel=["\']canonical["\'][^>]*>',
    r'<meta\s+[^>]*name=["\']robots["\'][^>]*>',
    r'<meta\s+[^>]*property=["\']og:[^"\']+["\'][^>]*>',
    r'<meta\s+[^>]*name=["\']twitter:[^"\']+["\'][^>]*>',
    r'<meta\s+[^>]*charset=[^>]*>',
    r'<meta\s+[^>]*name=["\']viewport["\'][^>]*>',
    r'<meta\s+[^>]*name=["\']theme-color["\'][^>]*>',
    r'<link\s+[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>',
    r'<link\s+[^>]*rel=["\']apple-touch-icon["\'][^>]*>',
    r'<link\s+[^>]*rel=["\']manifest["\'][^>]*>',
]

for filepath, info in pages_info.items():
    filepath = filepath.replace('/', os.sep)
    if not os.path.exists(filepath):
        print(f"File {filepath} not found!")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the <head> block
    head_match = re.search(r'(<head[^>]*>)(.*?)(</head>)', content, flags=re.DOTALL | re.IGNORECASE)
    if not head_match:
        print(f"No <head> found in {filepath}")
        continue
        
    head_start = head_match.group(1)
    head_content = head_match.group(2)
    head_end = head_match.group(3)

    # Remove existing tags from head_content
    for tag_pattern in tags_to_remove:
        head_content = re.sub(tag_pattern, '', head_content, flags=re.IGNORECASE | re.DOTALL)
        
    # Clean up multiple empty lines that might have been left behind
    head_content = re.sub(r'\n\s*\n', '\n', head_content)

    # Build the new SEO block
    title = info["title"]
    description = info["description"]
    url = info["url"]
    is_noindex = info.get("noindex", False)
    
    robots_content = "noindex, follow" if is_noindex else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    
    seo_block = f"""
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5" />
  <meta name="theme-color" content="#490b09" />
  
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="{robots_content}" />
  <link rel="canonical" href="{url}" />
  
  <link rel="icon" type="image/x-icon" href="/favicon.ico" />
  <link rel="apple-touch-icon" href="/apple-touch-icon.png" />
  
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="https://criaacao.com/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg" />
  <meta property="og:site_name" content="CriaAção Entretenimento" />
  <meta property="og:locale" content="pt_BR" />
  
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="https://criaacao.com/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg" />
"""

    new_head = head_start + seo_block + head_content + head_end
    
    new_content = content[:head_match.start()] + new_head + content[head_match.end():]
    
    # Ensure <html lang="pt-BR">
    html_match = re.search(r'<html[^>]*>', new_content, flags=re.IGNORECASE)
    if html_match:
        html_tag = html_match.group(0)
        if 'lang=' not in html_tag:
            new_html_tag = html_tag.replace('<html', '<html lang="pt-BR"')
            new_content = new_content.replace(html_tag, new_html_tag)
        else:
            new_html_tag = re.sub(r'lang=["\'][^"\']+["\']', 'lang="pt-BR"', html_tag, flags=re.IGNORECASE)
            new_content = new_content.replace(html_tag, new_html_tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Optimized {filepath}")
