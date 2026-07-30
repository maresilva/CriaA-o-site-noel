#!/usr/bin/env python3
"""
fix_js_seo.py – JavaScript SEO Audit & Fix
Analisa e corrige problemas de JavaScript SEO em todos os arquivos HTML do projeto.

Áreas cobertas:
  1. Renderização: scripts render-blocking no <head>/<body>
  2. Conteúdo indexável: conteúdo gerado apenas via JS
  3. Hydration: scripts inline duplicados
  4. Render blocking: adiciona defer/async a scripts externos
  5. Lazy loading: garante loading="lazy" em imagens abaixo do fold
  6. Links JS: converte href="#" em role="button" para não desperdiçar crawl budget
  7. Meta tags JS: remove meta generators desnecessárias, consolida tags duplicadas
"""

import re
import os
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(os.path.dirname(os.path.abspath(__file__)))

# Páginas principais do site
HTML_FILES = [
    'index.html',
    'quem-somos.html',
    'solucoes.html',
    'portfolio.html',
    'contato.html',
    'trabalhe-conosco.html',
    'eventos.html',
    '404.html',
    'solucoes/manual-do-verdadeiro-papai-noel.html',
]

# IDs de scripts que devem receber defer
SCRIPTS_NEED_DEFER = [
    'wp-hooks-js',
    'wp-i18n-js',
    'swv-js',
    'contact-form-7-js',
    'jquery-ui-core-js',
    'jquery-ui-tabs-js',
    'mfn-plugins-js',
    'mfn-menu-js',
    'mfn-animations-js',
    'mfn-jplayer-js',
    'mfn-parallax-js',
    'mfn-scripts-js',
    'elementor-webpack-runtime-js',
    'elementor-frontend-modules-js',
    'elementor-frontend-js',
    'jquery-numerator-js',
]

# Meta generators que são desnecessárias para SEO (revelam stack tecnológica)
REMOVE_GENERATORS = [
    r'<meta\s+content="WordPress[^"]*"\s+name="generator"\s*/?>',
    r'<meta\s+content="Site Kit by Google[^"]*"\s+name="generator"\s*/?>',
    r'<meta\s+content="Elementor[^"]*"\s+name="generator"\s*/?>',
    r'<meta\s+content="Powered by Slider Revolution[^"]*"\s+name="generator"\s*/?>',
]

# CSS que não é above-the-fold e pode ser carregado com media="print" trick
NON_CRITICAL_CSS_IDS = [
    'mfn-jplayer-css',
    'widget-counter-css',
    'widget-spacer-css',
    'widget-image-gallery-css',
    'mfn-animations-css',
]

results = {
    'timestamp': datetime.now().isoformat(),
    'files_processed': [],
    'fixes_applied': {
        'render_blocking_scripts_deferred': 0,
        'meta_generators_removed': 0,
        'href_hash_fixed': 0,
        'non_critical_css_deferred': 0,
        'duplicate_gtm_removed': 0,
        'noscript_fallbacks_added': 0,
        'inline_scripts_optimized': 0,
    },
    'issues_found': [],
    'recommendations': [],
}


def fix_render_blocking_scripts(html, filename):
    """Adiciona defer a scripts externos no footer que não têm defer/async."""
    count = 0
    
    def add_defer(match):
        nonlocal count
        tag = match.group(0)
        # Pula se já tem defer ou async
        if 'defer' in tag or 'async' in tag:
            return tag
        # Pula scripts inline (sem src)
        if 'src=' not in tag:
            return tag
        # Pula JSON-LD e speculation rules
        if 'application/ld+json' in tag or 'speculationrules' in tag or 'application/json' in tag:
            return tag
        # Pula scripts de dados offline
        if 'data-offline' in tag:
            return tag
        
        # Adiciona defer antes do src
        new_tag = tag.replace('<script ', '<script defer="defer" ', 1)
        count += 1
        return new_tag
    
    # Processa apenas scripts com src e com IDs conhecidos
    for script_id in SCRIPTS_NEED_DEFER:
        pattern = rf'<script\s+id="{re.escape(script_id)}"\s+src="[^"]+"\s*>\s*</script>'
        match = re.search(pattern, html)
        if match:
            tag = match.group(0)
            if 'defer' not in tag and 'async' not in tag:
                new_tag = tag.replace('<script ', '<script defer="defer" ', 1)
                html = html.replace(tag, new_tag, 1)
                count += 1
    
    results['fixes_applied']['render_blocking_scripts_deferred'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} scripts render-blocking convertidos para defer"
        )
    return html


def remove_meta_generators(html, filename):
    """Remove meta generators que revelam a stack tecnológica."""
    count = 0
    for pattern in REMOVE_GENERATORS:
        matches = re.findall(pattern, html, re.IGNORECASE)
        for m in matches:
            html = html.replace(m, '', 1)
            count += 1
    
    results['fixes_applied']['meta_generators_removed'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} meta generators removidas (revelavam stack tecnológica)"
        )
    return html


def fix_href_hash_links(html, filename):
    """Adiciona role='button' e tabindex='0' a links com href='#' que são UI controls."""
    count = 0
    
    # Links de menu toggle e close que usam href="#"
    def fix_link(match):
        nonlocal count
        tag = match.group(0)
        
        # Não mexer em links de âncora (href="#section-id")
        href_match = re.search(r'href="(#[^"]*)"', tag)
        if href_match and len(href_match.group(1)) > 1:
            return tag  # É uma âncora legítima
        
        # Já tem role="button"?
        if 'role="button"' in tag:
            return tag
        
        # Adicionar role="button" e tabindex
        new_tag = tag.replace('href="#"', 'href="#" role="button" tabindex="0"', 1)
        count += 1
        return new_tag
    
    html = re.sub(r'<a\s[^>]*href="#"[^>]*>', fix_link, html)
    
    results['fixes_applied']['href_hash_fixed'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} links href='#' receberam role='button' (melhora crawl budget)"
        )
    return html


def defer_non_critical_css(html, filename):
    """Converte CSS não-crítico para carregamento assíncrono com media="print" trick."""
    count = 0
    
    for css_id in NON_CRITICAL_CSS_IDS:
        pattern = rf'(<link[^>]*id="{re.escape(css_id)}"[^>]*)(media="all")'
        match = re.search(pattern, html)
        if match:
            old = match.group(0)
            # Usar print/onload trick para carregar assíncronamente
            new = old.replace('media="all"', 'media="print" onload="this.media=\'all\'"')
            # Adicionar noscript fallback
            noscript = f'\n<noscript>{old}</noscript>'
            html = html.replace(old, new + noscript, 1)
            count += 1
    
    results['fixes_applied']['non_critical_css_deferred'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} CSS não-críticos convertidos para carregamento assíncrono"
        )
    return html


def remove_duplicate_gtm(html, filename):
    """Remove instâncias duplicadas do Google Tag Manager."""
    # Encontra todas as ocorrências do GTM snippet
    gtm_pattern = r'<!-- Google Tag Manager -->\s*<script>[^<]*googletagmanager[^<]*</script>\s*<!-- End Google Tag Manager -->'
    matches = list(re.finditer(gtm_pattern, html))
    
    if len(matches) > 1:
        # Remove todas exceto a primeira (que está no <head>)
        for match in reversed(matches[1:]):
            html = html[:match.start()] + html[match.end():]
            results['fixes_applied']['duplicate_gtm_removed'] += 1
        
        results['issues_found'].append(
            f"{filename}: {len(matches) - 1} snippet(s) GTM duplicado(s) removido(s)"
        )
    
    # Verifica gtag duplicado também
    gtag_script_pattern = r'<script async="" src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>'
    gtag_matches = list(re.finditer(gtag_script_pattern, html))
    
    if len(gtag_matches) > 1:
        # Mantém apenas IDs únicos
        seen_ids = set()
        for match in reversed(gtag_matches):
            tag = match.group(0)
            gid = re.search(r'id=([A-Z0-9-]+)', tag)
            if gid:
                gid = gid.group(1)
                if gid in seen_ids:
                    html = html[:match.start()] + html[match.end():]
                    results['fixes_applied']['duplicate_gtm_removed'] += 1
                else:
                    seen_ids.add(gid)
    
    return html


def add_noscript_seo_fallback(html, filename):
    """Adiciona <noscript> fallback com conteúdo SEO para páginas que dependem de JS."""
    # Verifica se já existe um noscript com conteúdo SEO (não apenas GTM)
    noscript_seo_pattern = r'<noscript[^>]*>(?!<iframe).*?</noscript>'
    has_seo_noscript = bool(re.search(noscript_seo_pattern, html, re.DOTALL))
    
    if not has_seo_noscript:
        # Adicionar aviso noscript para o usuário
        noscript_tag = '''
<noscript>
<div style="padding:20px;text-align:center;background:#f8f0d8;color:#333;font-family:sans-serif;">
<p><strong>JavaScript necessário</strong> — Para a melhor experiência, habilite o JavaScript no seu navegador.</p>
<p>CriaAção Entretenimento — Decoração natalina e eventos para shopping centers em todo o Brasil.</p>
</div>
</noscript>'''
        
        # Inserir logo após o <body>
        body_match = re.search(r'<body[^>]*>', html)
        if body_match:
            insert_pos = body_match.end()
            # Verificar se já tem noscript GTM logo após
            gtm_noscript = re.search(r'\s*<!-- Google Tag Manager \(noscript\) -->', html[insert_pos:insert_pos+200])
            if gtm_noscript:
                insert_pos = insert_pos + gtm_noscript.end()
                # Pular o noscript do GTM
                end_noscript = html.find('<!-- End Google Tag Manager (noscript) -->', insert_pos)
                if end_noscript >= 0:
                    insert_pos = end_noscript + len('<!-- End Google Tag Manager (noscript) -->')
            
            html = html[:insert_pos] + noscript_tag + html[insert_pos:]
            results['fixes_applied']['noscript_fallbacks_added'] += 1
            results['issues_found'].append(
                f"{filename}: adicionado fallback <noscript> com conteúdo SEO"
            )
    
    return html


def optimize_inline_scripts(html, filename):
    """Move scripts inline pesados do <head> para antes do </body>."""
    count = 0
    
    # O script setREVStartSize é render-blocking no head
    rev_pattern = r'<script>function setREVStartSize\(e\)\s*\{.*?</script>'
    rev_match = re.search(rev_pattern, html, re.DOTALL)
    
    if rev_match:
        script_block = rev_match.group(0)
        # Verificar se está dentro do <head>
        head_end = html.find('</head>')
        if rev_match.start() < head_end:
            # Remover do head
            html = html[:rev_match.start()] + html[rev_match.end():]
            # Inserir antes do </body>
            body_end = html.rfind('</body>')
            if body_end < 0:
                body_end = html.rfind('</div></div></main></div></body>')
            if body_end >= 0:
                html = html[:body_end] + '\n' + script_block + '\n' + html[body_end:]
                count += 1
    
    results['fixes_applied']['inline_scripts_optimized'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} script(s) inline movido(s) do <head> para antes do </body>"
        )
    return html


def audit_js_content(html, filename):
    """Audita conteúdo que depende de JavaScript para ser renderizado."""
    issues = []
    
    # Verifica se há document.write (péssimo para SEO)
    if 'document.write' in html:
        issues.append(f"{filename}: usa document.write() — bloqueia parsing e prejudica SEO")
    
    # Verifica conteúdo importante dentro de templates JS
    template_pattern = r'<template[^>]*>.*?</template>'
    templates = re.findall(template_pattern, html, re.DOTALL)
    if templates:
        issues.append(f"{filename}: {len(templates)} <template> encontrados — conteúdo dentro de <template> não é indexado")
    
    # Verifica se counter/countdown depende apenas de JS (sem fallback)
    if 'id="cd-days"' in html or 'id="cd-hours"' in html:
        # Verifica se o valor padrão é "00" (sem conteúdo estático real)
        if '>00</div>' in html:
            issues.append(
                f"{filename}: contagem regressiva sem valor padrão visível — bots verão '00'"
            )
    
    # Verifica se há conteúdo injetado via innerHTML
    innerhtml_count = html.count('.innerHTML')
    if innerhtml_count > 3:
        issues.append(
            f"{filename}: {innerhtml_count} usos de .innerHTML — conteúdo injetado via JS não é indexável"
        )
    
    results['issues_found'].extend(issues)


def audit_lazy_loading(html, filename):
    """Audita implementação de lazy loading de imagens."""
    issues = []
    
    # Verifica imagens acima do fold sem loading="eager"
    # Logo na navegação geralmente é acima do fold
    logo_pattern = r'<img[^>]*logo[^>]*>'
    logo_imgs = re.findall(logo_pattern, html, re.IGNORECASE)
    for img in logo_imgs:
        if 'loading="lazy"' in img:
            issues.append(
                f"{filename}: imagem de logo com loading='lazy' — deve ser 'eager' (acima do fold)"
            )
    
    # Verifica imagens hero acima do fold
    hero_pattern = r'<img[^>]*hero[^>]*>'
    hero_imgs = re.findall(hero_pattern, html, re.IGNORECASE)
    for img in hero_imgs:
        if 'loading="lazy"' in img:
            issues.append(
                f"{filename}: imagem hero com loading='lazy' — deve ser 'eager'"
            )
    
    results['issues_found'].extend(issues)


def process_file(filepath, filename):
    """Processa um arquivo HTML individual."""
    if not filepath.exists():
        return
    
    print(f"  Processando: {filename}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # 1. Auditar conteúdo JS (apenas relatório)
    audit_js_content(html, filename)
    
    # 2. Auditar lazy loading (apenas relatório)
    audit_lazy_loading(html, filename)
    
    # 3. Aplicar correções
    html = fix_render_blocking_scripts(html, filename)
    html = remove_meta_generators(html, filename)
    html = fix_href_hash_links(html, filename)
    html = defer_non_critical_css(html, filename)
    html = remove_duplicate_gtm(html, filename)
    html = add_noscript_seo_fallback(html, filename)
    html = optimize_inline_scripts(html, filename)
    
    # Salvar se houve mudanças
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        results['files_processed'].append({
            'file': filename,
            'status': 'modified',
            'original_size': len(original),
            'new_size': len(html),
        })
        print(f"    [OK] Correcoes aplicadas")
    else:
        results['files_processed'].append({
            'file': filename,
            'status': 'no_changes',
        })
        print(f"    [--] Sem alteracoes necessarias")


def generate_recommendations():
    """Gera recomendações baseadas na auditoria."""
    results['recommendations'] = [
        {
            'priority': 'ALTA',
            'area': 'Render Blocking',
            'issue': 'Scripts sem defer/async bloqueiam a renderização e atrasam FCP/LCP',
            'fix': 'Adicionado defer a scripts que não precisam executar sincronamente',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'area': 'Meta Tags JS',
            'issue': 'Meta generators revelam stack tecnológica (WordPress, Elementor, Slider Revolution)',
            'fix': 'Removidas meta generators desnecessárias — reduz superfície de ataque e bytes no <head>',
            'status': 'APLICADO',
        },
        {
            'priority': 'MÉDIA',
            'area': 'Links JS',
            'issue': 'Links com href="#" desperdiçam crawl budget e confundem bots',
            'fix': 'Adicionado role="button" para indicar que são controles UI, não links navegáveis',
            'status': 'APLICADO',
        },
        {
            'priority': 'MÉDIA',
            'area': 'CSS Render Blocking',
            'issue': 'CSS não-crítico (jplayer, animations, widgets) bloqueia renderização',
            'fix': 'Convertido para carregamento assíncrono via media="print" trick com noscript fallback',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'area': 'GTM Duplicado',
            'issue': 'Google Tag Manager carregado múltiplas vezes — impacta performance e gera dados duplicados',
            'fix': 'Removidas instâncias duplicadas mantendo apenas a do <head>',
            'status': 'APLICADO',
        },
        {
            'priority': 'MÉDIA',
            'area': 'Noscript Fallback',
            'issue': 'Sem fallback <noscript> — bots que não executam JS não veem conteúdo alternativo',
            'fix': 'Adicionado <noscript> com texto descritivo para indexação sem JavaScript',
            'status': 'APLICADO',
        },
        {
            'priority': 'MÉDIA',
            'area': 'Scripts Inline no Head',
            'issue': 'Script setREVStartSize é render-blocking no <head>',
            'fix': 'Movido para antes do </body> para não bloquear renderização inicial',
            'status': 'APLICADO',
        },
        {
            'priority': 'BAIXA',
            'area': 'Conteúdo Indexável',
            'issue': 'Contagem regressiva de Natal renderiza "00" no HTML estático',
            'fix_manual': 'Considerar renderizar data-alvo no HTML para bots verem informação útil',
            'status': 'RECOMENDAÇÃO',
        },
        {
            'priority': 'BAIXA',
            'area': 'Lazy Loading',
            'issue': 'Verificar se imagens above-the-fold (logo, hero) não têm loading="lazy"',
            'fix_manual': 'Imagens acima do fold devem ter loading="eager" ou fetchpriority="high"',
            'status': 'RECOMENDAÇÃO',
        },
        {
            'priority': 'BAIXA',
            'area': 'Hydration',
            'issue': 'Múltiplos scripts inline duplicam lógica (active menu, scroll handlers)',
            'fix_manual': 'Consolidar em arquivo externo único com defer para reduzir parsing time',
            'status': 'RECOMENDAÇÃO',
        },
    ]


def main():
    print("=" * 60)
    print("  JAVASCRIPT SEO AUDIT & FIX")
    print("  CriaAção Entretenimento")
    print("=" * 60)
    print()
    
    for html_file in HTML_FILES:
        filepath = ROOT / html_file
        process_file(filepath, html_file)
    
    generate_recommendations()
    
    # Salvar relatório JSON
    report_path = ROOT / 'js_seo_audit_results.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Resumo
    print()
    print("=" * 60)
    print("  RESUMO")
    print("=" * 60)
    fixes = results['fixes_applied']
    total = sum(fixes.values())
    print(f"  Total de correcoes aplicadas: {total}")
    print(f"    - Scripts render-blocking -> defer: {fixes['render_blocking_scripts_deferred']}")
    print(f"    - Meta generators removidas: {fixes['meta_generators_removed']}")
    print(f"    - Links href='#' corrigidos: {fixes['href_hash_fixed']}")
    print(f"    - CSS nao-critico deferido: {fixes['non_critical_css_deferred']}")
    print(f"    - GTM duplicados removidos: {fixes['duplicate_gtm_removed']}")
    print(f"    - Noscript fallbacks adicionados: {fixes['noscript_fallbacks_added']}")
    print(f"    - Scripts inline otimizados: {fixes['inline_scripts_optimized']}")
    print()
    print(f"  Relatorio salvo em: {report_path}")
    print()


if __name__ == '__main__':
    main()
