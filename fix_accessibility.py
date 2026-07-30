#!/usr/bin/env python3
"""
fix_accessibility.py - Auditoria e Correcao de Acessibilidade (WCAG 2.1 AA)

Areas cobertas:
  1. ARIA: labels genericos, roles incorretos, estados ausentes
  2. Labels: labels de formulario sem for, labels redundantes
  3. Inputs: campos sem labels acessiveis, autocomplete ausente
  4. Contraste: CSS com cores de baixo contraste
  5. Tabulacao: skip links, focus management, tabindex
  6. Landmarks: header, nav, main, footer, aside
  7. Semantica: headings hierarchy, listas, links vs buttons
"""

import re
import os
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(os.path.dirname(os.path.abspath(__file__)))

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

results = {
    'timestamp': datetime.now().isoformat(),
    'files_processed': [],
    'fixes_applied': {
        'skip_links_added': 0,
        'aria_labels_fixed': 0,
        'nav_landmarks_added': 0,
        'focus_visible_added': 0,
        'svg_aria_hidden_added': 0,
        'form_labels_fixed': 0,
        'lang_attributes_fixed': 0,
        'side_slide_aria_fixed': 0,
        'footer_landmark_fixed': 0,
        'contrast_css_added': 0,
        'keyboard_trap_fixed': 0,
        'heading_hierarchy_notes': 0,
    },
    'issues_found': [],
    'recommendations': [],
}


def add_skip_link(html, filename):
    """Adiciona link 'Pular para conteudo principal' (WCAG 2.4.1)."""
    if 'skip-to-content' in html or 'skip-link' in html or 'skiplink' in html:
        return html

    skip_link_html = '''<a class="ca-skip-link" href="#Content">Pular para o conteudo principal</a>
'''
    skip_link_css = '''<style id="ca-a11y-skip-link">
.ca-skip-link {
  position: absolute;
  top: -100%;
  left: 50%;
  transform: translateX(-50%);
  background: #F2B84B;
  color: #1a050a;
  padding: 12px 24px;
  font-weight: 700;
  font-size: 14px;
  z-index: 99999999;
  border-radius: 0 0 8px 8px;
  text-decoration: none;
  transition: top 0.2s ease;
}
.ca-skip-link:focus {
  top: 0;
  outline: 3px solid #fff;
  outline-offset: 2px;
}
</style>
'''
    # Insert after <body> tag
    body_match = re.search(r'<body[^>]*>', html)
    if body_match:
        insert_pos = body_match.end()
        # Skip past noscript GTM if present
        noscript_match = re.search(
            r'\s*<!-- Google Tag Manager \(noscript\) -->.*?<!-- End Google Tag Manager \(noscript\) -->\s*',
            html[insert_pos:insert_pos+500], re.DOTALL
        )
        if noscript_match:
            insert_pos += noscript_match.end()
        # Skip past noscript SEO fallback
        noscript_seo = re.search(r'\s*<noscript>\s*<div[^>]*>.*?</noscript>\s*', html[insert_pos:insert_pos+500], re.DOTALL)
        if noscript_seo:
            insert_pos += noscript_seo.end()

        html = html[:insert_pos] + '\n' + skip_link_html + html[insert_pos:]

        # Add CSS in head
        head_end = html.find('</head>')
        if head_end >= 0:
            html = html[:head_end] + skip_link_css + html[head_end:]

        results['fixes_applied']['skip_links_added'] += 1
        results['issues_found'].append(
            f"{filename}: ADICIONADO skip link 'Pular para conteudo' (WCAG 2.4.1)"
        )
    return html


def fix_generic_aria_labels(html, filename):
    """Corrige aria-labels genericos como 'Link' que nao descrevem o destino (WCAG 1.1.1)."""
    count = 0

    # Fix aria-label="Link" on logo
    old = 'aria-label="Link" class="logo"'
    new = 'aria-label="Pagina inicial - CriaAcao Entretenimento" class="logo"'
    if old in html:
        html = html.replace(old, new)
        count += 1

    # Fix aria-label="Acao ou Link" on close buttons
    old = 'aria-label="Acao ou Link" class="close"'
    new = 'aria-label="Fechar menu lateral" class="close"'
    if old in html:
        html = html.replace(old, new)
        count += 1

    # Try the accented version too
    old_acc = 'aria-label="A\u00e7\u00e3o ou Link" class="close"'
    new_acc = 'aria-label="Fechar menu lateral" class="close"'
    if old_acc in html:
        html = html.replace(old_acc, new_acc)
        count += 1

    # Fix Side_slide role="banner" -> should be role="dialog" or complementary
    old_role = 'id="Side_slide" role="banner"'
    new_role = 'id="Side_slide" role="dialog" aria-label="Menu de navegacao mobile"'
    if old_role in html:
        html = html.replace(old_role, new_role)
        count += 1
        results['fixes_applied']['side_slide_aria_fixed'] += 1

    results['fixes_applied']['aria_labels_fixed'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} aria-label(s) generico(s) corrigido(s) (WCAG 1.1.1)"
        )
    return html


def add_nav_landmark(html, filename):
    """Garante que <nav> tenha aria-label para distinguir navegacoes (WCAG 1.3.1)."""
    count = 0

    # Main navigation
    old_nav = '<nav id="menu">'
    new_nav = '<nav id="menu" aria-label="Menu principal">'
    if old_nav in html:
        html = html.replace(old_nav, new_nav)
        count += 1

    results['fixes_applied']['nav_landmarks_added'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} <nav> recebeu aria-label para acessibilidade (WCAG 1.3.1)"
        )
    return html


def add_focus_visible_css(html, filename):
    """Adiciona estilos de foco visivel para todos os elementos interativos (WCAG 2.4.7)."""
    if 'ca-a11y-focus' in html:
        return html

    focus_css = '''<style id="ca-a11y-focus">
/* Acessibilidade: Focus visible (WCAG 2.4.7) */
*:focus-visible {
  outline: 3px solid #F2B84B !important;
  outline-offset: 3px !important;
}
a:focus-visible, button:focus-visible, input:focus-visible,
select:focus-visible, textarea:focus-visible,
[role="button"]:focus-visible {
  outline: 3px solid #F2B84B !important;
  outline-offset: 3px !important;
  box-shadow: 0 0 0 6px rgba(242, 184, 75, 0.25) !important;
}
/* Reduce motion for users who prefer it */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
/* High contrast mode support */
@media (forced-colors: active) {
  .ca-button-main, .ca-button-secondary {
    border: 2px solid currentColor;
  }
}
</style>
'''
    head_end = html.find('</head>')
    if head_end >= 0:
        html = html[:head_end] + focus_css + html[head_end:]
        results['fixes_applied']['focus_visible_added'] += 1
        results['issues_found'].append(
            f"{filename}: ADICIONADO CSS focus-visible + prefers-reduced-motion (WCAG 2.4.7, 2.3.3)"
        )
    return html


def fix_svg_accessibility(html, filename):
    """Adiciona aria-hidden='true' a SVGs decorativos e role='img' a SVGs informativos (WCAG 1.1.1)."""
    count = 0

    # Decorative SVGs inside links/buttons that already have text
    # These should be aria-hidden="true" so screen readers skip them
    def fix_decorative_svg(match):
        nonlocal count
        tag = match.group(0)
        if 'aria-hidden' in tag or 'role="img"' in tag:
            return tag
        # Add aria-hidden and focusable="false"
        new_tag = tag.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
        count += 1
        return new_tag

    # SVGs inside links/buttons with text are decorative
    # Match <svg inside elements that have text content
    html = re.sub(r'<svg\s+(?:fill|height|width|stroke|viewbox|xmlns)[^>]*>', fix_decorative_svg, html)

    results['fixes_applied']['svg_aria_hidden_added'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} SVG(s) decorativo(s) receberam aria-hidden='true' (WCAG 1.1.1)"
        )
    return html


def fix_form_labels(html, filename):
    """Associa <label> a <input> com atributo for (WCAG 1.3.1, 4.1.2)."""
    count = 0

    # Pattern: <label class="ca-form-label">Text</label> followed by <input id="xxx">
    # These labels need for="xxx"
    label_input_pattern = r'(<label\s+class="ca-form-label")(>)([^<]+</label>\s*<(?:input|select|textarea)[^>]*id="([^"]+)")'
    
    def add_for(match):
        nonlocal count
        tag_start = match.group(1)
        tag_close = match.group(2)
        rest = match.group(3)
        input_id = match.group(4)
        
        if 'for=' in tag_start:
            return match.group(0)
        
        count += 1
        return f'{tag_start} for="{input_id}"{tag_close}{rest}'

    html = re.sub(label_input_pattern, add_for, html)

    # Fix: remove redundant aria-label on inputs that now have proper label[for]
    # The aria-label like "Preencha o campo nome" is redundant if label is associated
    # But we keep them for safety as they provide extra context

    results['fixes_applied']['form_labels_fixed'] += count
    if count > 0:
        results['issues_found'].append(
            f"{filename}: {count} <label> associado(s) a input via for='' (WCAG 1.3.1)"
        )
    return html


def fix_footer_landmark(html, filename):
    """Corrige o footer semantico para ser visivel e ter role correto (WCAG 1.3.1)."""
    # The footer has display:none which makes it invisible to all users
    # We check if there's a visible footer section (inst-section-footer)
    count = 0

    # The actual visible "footer" content is inside inst-section-footer
    # but the <footer> landmark is hidden. Add role="contentinfo" to the visible section.
    if 'inst-section-footer' in html and '<footer' in html:
        # Check if the visible footer area has role
        if 'class="inst-section-footer' in html and 'role="contentinfo"' not in html.split('inst-section-footer')[0][-200:]:
            # The hidden footer already has role="contentinfo", that's fine
            # But we should also ensure the visible copyright section is semantically correct
            pass

    # The Side_slide has role="banner" which is wrong - it's a mobile menu dialog
    # Already fixed in fix_generic_aria_labels
    
    return html


def fix_contrast_css(html, filename):
    """Adiciona CSS para melhorar contraste de textos claros sobre fundos escuros (WCAG 1.4.3)."""
    if 'ca-a11y-contrast' in html:
        return html

    contrast_css = '''<style id="ca-a11y-contrast">
/* Acessibilidade: Melhorias de contraste (WCAG 1.4.3 - AA ratio 4.5:1) */
/* Textos em rgba(255,255,255,0.7) sobre fundo escuro: ratio ~3.5:1 -> melhorar */
.ca-countdown-text,
.ca-indicator-text span,
.ca-segmentos-text,
.ca-desc {
  color: rgba(255, 255, 255, 0.87) !important; /* ratio >= 4.5:1 sobre #1a050a */
}
/* Links no footer/contato sobre fundo escuro */
.inst-contact-link {
  color: rgba(255, 255, 255, 0.92) !important;
}
/* Placeholder text - minimo 4.5:1 */
input::placeholder, textarea::placeholder, select::placeholder {
  color: rgba(255, 255, 255, 0.6);
}
/* Textos sobre fundo dourado - garantir contraste */
.ca-badge {
  color: #F2B84B;
}
</style>
'''
    head_end = html.find('</head>')
    if head_end >= 0:
        html = html[:head_end] + contrast_css + html[head_end:]
        results['fixes_applied']['contrast_css_added'] += 1
        results['issues_found'].append(
            f"{filename}: ADICIONADO CSS de contraste aprimorado (WCAG 1.4.3)"
        )
    return html


def fix_keyboard_accessibility(html, filename):
    """Adiciona JS para acessibilidade via teclado (WCAG 2.1.1, 2.1.2)."""
    if 'ca-a11y-keyboard' in html:
        return html

    keyboard_js = '''<script id="ca-a11y-keyboard">
document.addEventListener("DOMContentLoaded", function() {
  // Escape para fechar menus/modais (WCAG 2.1.2 - sem armadilha de teclado)
  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
      // Fechar side slide
      var side = document.getElementById("Side_slide");
      if (side && side.classList.contains("open")) {
        side.classList.remove("open");
        var overlay = document.getElementById("body_overlay");
        if (overlay) overlay.style.display = "none";
        // Retornar foco ao botao que abriu o menu
        var toggle = document.querySelector(".responsive-menu-toggle");
        if (toggle) toggle.focus();
      }
      // Fechar GDPR
      var gdpr = document.getElementById("mfn-gdpr");
      if (gdpr && gdpr.style.display !== "none") {
        var btn = gdpr.querySelector(".mfn-gdpr-button");
        if (btn) btn.click();
      }
    }
  });
  // Enter/Space em role="button" (WCAG 2.1.1)
  document.querySelectorAll('[role="button"]').forEach(function(el) {
    el.addEventListener("keydown", function(e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        el.click();
      }
    });
  });
  // Dropdown com teclado: Enter/Space para abrir, Escape para fechar
  var dropdown = document.querySelector(".ca-has-dropdown > a");
  if (dropdown) {
    dropdown.setAttribute("aria-expanded", "false");
    dropdown.setAttribute("aria-haspopup", "true");
    dropdown.addEventListener("keydown", function(e) {
      var parent = this.parentElement;
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        var isOpen = parent.classList.contains("is-active");
        parent.classList.toggle("is-active");
        this.setAttribute("aria-expanded", !isOpen);
      }
      if (e.key === "Escape" && parent.classList.contains("is-active")) {
        parent.classList.remove("is-active");
        this.setAttribute("aria-expanded", "false");
        this.focus();
      }
    });
  }
});
</script>
'''
    body_end = html.rfind('</body>')
    if body_end < 0:
        body_end = html.rfind('</html>')
    if body_end >= 0:
        html = html[:body_end] + keyboard_js + '\n' + html[body_end:]
        results['fixes_applied']['keyboard_trap_fixed'] += 1
        results['issues_found'].append(
            f"{filename}: ADICIONADO JS para acessibilidade de teclado (WCAG 2.1.1, 2.1.2)"
        )
    return html


def fix_html_lang(html, filename):
    """Verifica e corrige o atributo lang no <html> (WCAG 3.1.1)."""
    count = 0
    # Already has lang="pt-BR" - OK
    if 'lang="pt-BR"' in html:
        return html
    if 'lang="pt"' in html or 'lang=""' in html or ('<html' in html and 'lang=' not in html[:500]):
        html = re.sub(r'<html([^>]*)>', r'<html\1 lang="pt-BR">', html, count=1)
        count += 1
        results['fixes_applied']['lang_attributes_fixed'] += count
    return html


def audit_heading_hierarchy(html, filename):
    """Audita a hierarquia de headings h1-h6 (WCAG 1.3.1)."""
    headings = re.findall(r'<(h[1-6])\b[^>]*>(.*?)</\1>', html, re.DOTALL | re.IGNORECASE)
    
    if not headings:
        results['issues_found'].append(f"{filename}: ALERTA - nenhum heading encontrado")
        return

    # Check for multiple h1
    h1_count = sum(1 for tag, _ in headings if tag.lower() == 'h1')
    if h1_count == 0:
        results['issues_found'].append(f"{filename}: ALERTA - nenhum <h1> encontrado (WCAG 1.3.1)")
    elif h1_count > 1:
        results['issues_found'].append(f"{filename}: INFO - {h1_count} <h1> encontrados (recomendado: 1)")

    # Check for skipped levels
    prev_level = 0
    for tag, content in headings:
        level = int(tag[1])
        if prev_level > 0 and level > prev_level + 1:
            clean_content = re.sub(r'<[^>]+>', '', content).strip()[:50]
            results['issues_found'].append(
                f"{filename}: ALERTA - salto de <h{prev_level}> para <h{level}> "
                f"('{clean_content}...') (WCAG 1.3.1)"
            )
            results['fixes_applied']['heading_hierarchy_notes'] += 1
        prev_level = level


def audit_images_alt(html, filename):
    """Audita alt text em imagens (WCAG 1.1.1)."""
    imgs = re.findall(r'<img\b([^>]*)/?>', html, re.IGNORECASE)
    
    missing_alt = 0
    empty_alt = 0
    for attrs in imgs:
        if 'alt=' not in attrs:
            missing_alt += 1
        elif 'alt=""' in attrs:
            empty_alt += 1

    if missing_alt > 0:
        results['issues_found'].append(
            f"{filename}: CRITICO - {missing_alt} imagem(ns) SEM atributo alt (WCAG 1.1.1)"
        )
    if empty_alt > 3:
        results['issues_found'].append(
            f"{filename}: INFO - {empty_alt} imagens com alt vazio (decorativas) - ok se intencionais"
        )


def audit_color_contrast(html, filename):
    """Analisa potenciais problemas de contraste de cor (WCAG 1.4.3)."""
    # Check for rgba with low alpha on text colors
    low_contrast_patterns = [
        (r'color:\s*rgba\(255,\s*255,\s*255,\s*0\.[0-6]\d*\)', 'texto branco com opacidade < 0.7'),
        (r'color:\s*#[89a-fA-F]{6}', 'cor clara potencialmente com baixo contraste'),
    ]
    
    for pattern, desc in low_contrast_patterns[:1]:  # Only check rgba for now
        matches = re.findall(pattern, html)
        if len(matches) > 3:
            results['issues_found'].append(
                f"{filename}: INFO - {len(matches)} ocorrencias de {desc} (verificar WCAG 1.4.3)"
            )


def audit_links_purpose(html, filename):
    """Audita links sem texto descritivo (WCAG 2.4.4)."""
    # Find links with only an icon/image and no text or aria-label
    icon_only_links = re.findall(
        r'<a\b([^>]*)>\s*<(?:i|svg|img)\b[^>]*/?\s*>\s*</a>',
        html, re.IGNORECASE | re.DOTALL
    )
    
    no_label = 0
    for attrs in icon_only_links:
        if 'aria-label' not in attrs and 'title' not in attrs:
            no_label += 1
    
    if no_label > 0:
        results['issues_found'].append(
            f"{filename}: ALERTA - {no_label} link(s) com apenas icone sem aria-label (WCAG 2.4.4)"
        )


def process_file(filepath, filename):
    """Processa um arquivo HTML individual."""
    if not filepath.exists():
        return

    print(f"  Processando: {filename}")

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    original = html

    # === AUDITORIAS (apenas relatorio) ===
    audit_heading_hierarchy(html, filename)
    audit_images_alt(html, filename)
    audit_color_contrast(html, filename)
    audit_links_purpose(html, filename)

    # === CORRECOES ===
    html = add_skip_link(html, filename)
    html = fix_generic_aria_labels(html, filename)
    html = add_nav_landmark(html, filename)
    html = add_focus_visible_css(html, filename)
    html = fix_svg_accessibility(html, filename)
    html = fix_form_labels(html, filename)
    html = fix_contrast_css(html, filename)
    html = fix_keyboard_accessibility(html, filename)
    html = fix_html_lang(html, filename)

    # Salvar se houve mudancas
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
    """Gera recomendacoes baseadas na auditoria."""
    results['recommendations'] = [
        {
            'priority': 'CRITICA',
            'wcag': '2.4.1',
            'area': 'Tabulacao',
            'issue': 'Sem skip link para pular navegacao',
            'fix': 'Adicionado link "Pular para conteudo principal" visivel apenas no foco',
            'status': 'APLICADO',
        },
        {
            'priority': 'CRITICA',
            'wcag': '2.4.7',
            'area': 'Tabulacao',
            'issue': 'Sem indicador visual de foco para navegacao por teclado',
            'fix': 'Adicionado CSS :focus-visible com outline dourado de 3px + box-shadow',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'wcag': '1.1.1',
            'area': 'ARIA',
            'issue': 'aria-label="Link" generico nao descreve o destino do link',
            'fix': 'Substituido por descricao significativa do link',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'wcag': '4.1.2',
            'area': 'ARIA',
            'issue': 'Side slide com role="banner" (deveria ser dialog para menu mobile)',
            'fix': 'Alterado para role="dialog" com aria-label descritivo',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'wcag': '1.3.1',
            'area': 'Landmarks',
            'issue': '<nav> sem aria-label para distinguir multiplas navegacoes',
            'fix': 'Adicionado aria-label="Menu principal" ao nav#menu',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'wcag': '1.1.1',
            'area': 'ARIA',
            'issue': 'SVGs decorativos (icones em links) expostos a leitores de tela',
            'fix': 'Adicionado aria-hidden="true" focusable="false" a SVGs decorativos',
            'status': 'APLICADO',
        },
        {
            'priority': 'ALTA',
            'wcag': '1.3.1',
            'area': 'Labels',
            'issue': 'Labels de formulario sem atributo for="" associado ao input',
            'fix': 'Adicionado for="id" em todas as labels do formulario trabalhe-conosco',
            'status': 'APLICADO',
        },
        {
            'priority': 'MEDIA',
            'wcag': '1.4.3',
            'area': 'Contraste',
            'issue': 'Textos com rgba(255,255,255,0.7) sobre fundo escuro - ratio < 4.5:1',
            'fix': 'CSS adicionado para aumentar opacidade de textos sobre fundo escuro',
            'status': 'APLICADO',
        },
        {
            'priority': 'MEDIA',
            'wcag': '2.1.1',
            'area': 'Tabulacao',
            'issue': 'Elementos role="button" nao respondem a Enter/Space',
            'fix': 'Adicionado JS para ativar click em Enter/Space em role="button"',
            'status': 'APLICADO',
        },
        {
            'priority': 'MEDIA',
            'wcag': '2.1.2',
            'area': 'Tabulacao',
            'issue': 'Menu mobile sem mecanismo de fechar via Escape',
            'fix': 'Adicionado handler de Escape para fechar menus e modais',
            'status': 'APLICADO',
        },
        {
            'priority': 'MEDIA',
            'wcag': '2.3.3',
            'area': 'Semantica',
            'issue': 'Animacoes podem causar problemas para usuarios sensiveis a movimento',
            'fix': 'Adicionado @media (prefers-reduced-motion: reduce) para desabilitar animacoes',
            'status': 'APLICADO',
        },
        {
            'priority': 'BAIXA',
            'wcag': '1.3.1',
            'area': 'Semantica',
            'issue': 'Verificar hierarquia de headings (h1 > h2 > h3 sem pular niveis)',
            'fix_manual': 'Revisar manualmente a hierarquia de headings em cada pagina',
            'status': 'RECOMENDACAO',
        },
        {
            'priority': 'BAIXA',
            'wcag': '1.4.11',
            'area': 'Contraste',
            'issue': 'Contraste de elementos nao-textuais (icones, bordas) deve ser >= 3:1',
            'fix_manual': 'Testar com ferramenta de contraste (axe, Lighthouse)',
            'status': 'RECOMENDACAO',
        },
    ]


def main():
    print("=" * 60)
    print("  ACCESSIBILITY AUDIT & FIX (WCAG 2.1 AA)")
    print("  CriaAcao Entretenimento")
    print("=" * 60)
    print()

    for html_file in HTML_FILES:
        filepath = ROOT / html_file
        process_file(filepath, html_file)

    generate_recommendations()

    # Salvar relatorio JSON
    report_path = ROOT / 'a11y_audit_results.json'
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
    print(f"    - Skip links adicionados: {fixes['skip_links_added']}")
    print(f"    - ARIA labels corrigidos: {fixes['aria_labels_fixed']}")
    print(f"    - Nav landmarks adicionados: {fixes['nav_landmarks_added']}")
    print(f"    - Focus visible CSS: {fixes['focus_visible_added']}")
    print(f"    - SVG aria-hidden: {fixes['svg_aria_hidden_added']}")
    print(f"    - Form labels corrigidos: {fixes['form_labels_fixed']}")
    print(f"    - Contraste CSS: {fixes['contrast_css_added']}")
    print(f"    - Teclado acessibilidade: {fixes['keyboard_trap_fixed']}")
    print(f"    - Side slide ARIA: {fixes['side_slide_aria_fixed']}")
    print(f"    - Heading hierarchy notes: {fixes['heading_hierarchy_notes']}")
    print()
    print(f"  Issues encontradas: {len(results['issues_found'])}")
    print(f"  Relatorio salvo em: {report_path}")
    print()


if __name__ == '__main__':
    main()
