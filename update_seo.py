import re
import os

pages = {
    'index.html': {
        'title': 'CriaAção Entretenimento | Natal para Shopping Centers no Brasil',
        'desc': 'Especialistas há mais de 30 anos em criar as maiores experiências natalinas para Shoppings. Papai Noel, Cenografia e Ativações.',
        'url': 'https://cria-a-o-site-noel.vercel.app/'
    },
    'quem-somos.html': {
        'title': 'Quem Somos | CriaAção Entretenimento',
        'desc': 'Conheça a história da CriaAção Entretenimento, líder em soluções de Natal para grandes eventos, shoppings e espaços corporativos.',
        'url': 'https://cria-a-o-site-noel.vercel.app/quem-somos.html'
    },
    'solucoes.html': {
        'title': 'Soluções de Natal para Shoppings e Empresas | CriaAção',
        'desc': 'Descubra nossas soluções completas: Papai Noel Profissional, Cenografia, Plataforma 360°, Personagens, Espaços Fotográficos e mais.',
        'url': 'https://cria-a-o-site-noel.vercel.app/solucoes.html'
    },
    'portfolio.html': {
        'title': 'Portfólio de Natal | Nossos Clientes | CriaAção',
        'desc': 'Veja como transformamos o Natal no RioMar, Iguatemi e outros mais de 40 shoppings espalhados pelo Brasil.',
        'url': 'https://cria-a-o-site-noel.vercel.app/portfolio.html'
    },
    'contato.html': {
        'title': 'Fale Conosco | Orçamento de Natal | CriaAção',
        'desc': 'Entre em contato com nossos especialistas e solicite um orçamento para a decoração e operação de Natal do seu empreendimento.',
        'url': 'https://cria-a-o-site-noel.vercel.app/contato.html'
    }
}

seo_template = '''<meta charset="utf-8" />
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="Natal para Shopping Centers, Papai Noel para Shopping, Empresa de Natal para Shopping, Eventos Natalinos, Decoração Natalina para Shopping, Cenografia Natalina, Papai Noel Profissional, Espaço Fotográfico Natal, Plataforma 360, Personagens Natalinos, Ativações Natalinas, Natal Corporativo, Natal Comercial, Produção de Natal, CriaAção Entretenimento">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{url}">

  <!-- Open Graph -->
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="CriaAção Entretenimento">
  <meta property="og:image" content="https://cria-a-o-site-noel.vercel.app/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg">
  <meta property="og:url" content="{url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://cria-a-o-site-noel.vercel.app/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg">

  <!-- Schema.org -->
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "Organization",
      "@id": "https://cria-a-o-site-noel.vercel.app/#organization",
      "name": "CriaAção Entretenimento",
      "url": "https://cria-a-o-site-noel.vercel.app/",
      "logo": "https://cria-a-o-site-noel.vercel.app/assets/images/gallery/nossa-historia-criaacao-entretenimento.jpg",
      "areaServed": "BR",
      "knowsAbout": "Eventos Natalinos para Shopping Centers"
    }},
    {{
      "@type": "LocalBusiness",
      "@id": "https://cria-a-o-site-noel.vercel.app/#localbusiness",
      "name": "CriaAção Entretenimento",
      "url": "https://cria-a-o-site-noel.vercel.app/",
      "telephone": "+5585988601400",
      "address": {{
        "@type": "PostalAddress",
        "addressLocality": "Fortaleza",
        "addressRegion": "CE",
        "addressCountry": "BR"
      }},
      "areaServed": "BR",
      "priceRange": "$",
      "parentOrganization": {{
        "@id": "https://cria-a-o-site-noel.vercel.app/#organization"
      }}
    }},
    {{
      "@type": "WebSite",
      "@id": "https://cria-a-o-site-noel.vercel.app/#website",
      "url": "https://cria-a-o-site-noel.vercel.app/",
      "name": "CriaAção Entretenimento | Natal para Shopping Centers no Brasil",
      "publisher": {{
        "@id": "https://cria-a-o-site-noel.vercel.app/#organization"
      }}
    }},
    {{
      "@type": "Service",
      "serviceType": "Eventos Natalinos para Shopping Centers",
      "provider": {{
        "@id": "https://cria-a-o-site-noel.vercel.app/#organization"
      }},
      "areaServed": "BR",
      "hasOfferCatalog": {{
        "@type": "OfferCatalog",
        "name": "Serviços de Natal",
        "itemListElement": [
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Papai Noel Profissional" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Personagens Natalinos" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Cenografia Natalina" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Espaço Fotográfico" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Plataforma 360°" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Brindes Personalizados" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Operação Completa" }} }},
          {{ "@type": "Offer", "itemOffered": {{ "@type": "Service", "name": "Ativações Promocionais" }} }}
        ]
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://cria-a-o-site-noel.vercel.app/"
        }}
      ]
    }}
  ]
}}
</script>
  <meta content="telephone=no" name="format-detection" />'''

for filename, data in pages.items():
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-16') as f:
        content = f.read()
    
    # We replace from <meta charset="utf-8" /> (the second one) down to <meta content="telephone=no" name="format-detection" />
    # Let's find the position.
    
    pattern = r'<meta charset="utf-8" />\s*<title>CriaAção Entretenimento.*?<meta content="telephone=no" name="format-detection" />'
    new_seo = seo_template.format(title=data['title'], desc=data['desc'], url=data['url'])
    
    new_content, count = re.subn(pattern, new_seo, content, flags=re.DOTALL)
    
    if count == 0:
        print(f"Pattern not found in {filename}!")
    else:
        with open(filename, 'w', encoding='utf-16') as f:
            f.write(new_content)
        print(f"Updated {filename}")
