$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$cssPath = "assets/css/typography.css"
$css = [System.IO.File]::ReadAllText($cssPath, $utf8NoBom)

$desktopCss = @"

/* ========================================================================
 * APLICAÇÃO DESKTOP (ETAPA 2)
 * ========================================================================
 * Aplicação estrita no Desktop para não afetar os componentes Mobile.
 */
@media (min-width: 992px) {
    /* HEROS / GRANDES TÍTULOS */
    h1, .ca-hero-title {
        font-family: var(--ca-font-display, serif) !important;
        font-size: var(--ca-text-5xl) !important;
        line-height: var(--ca-line-tight) !important;
        font-weight: var(--ca-weight-bold) !important;
        letter-spacing: var(--ca-tracking-tight) !important;
    }

    /* H2 / TÍTULOS DE SEÇÃO */
    h2, .ca-title, .sol-title-main {
        font-family: var(--ca-font-display, serif) !important;
        font-size: var(--ca-text-4xl) !important;
        line-height: var(--ca-line-tight) !important;
        font-weight: var(--ca-weight-bold) !important;
    }

    /* H3 / TÍTULOS DE CARDS E SUBSEÇÕES */
    h3, .ca-card-title, .oa-segment-title, .sol-segment-title, .sol-time-title {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-2xl) !important;
        line-height: var(--ca-line-snug) !important;
        font-weight: var(--ca-weight-semibold) !important;
        letter-spacing: var(--ca-tracking-normal) !important;
    }

    /* H4 / MENORES DESTAQUES */
    h4 {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-xl) !important;
        line-height: var(--ca-line-snug) !important;
        font-weight: var(--ca-weight-medium) !important;
    }

    /* TEXTOS / PARÁGRAFOS GERAIS */
    p, .ca-card-desc, .oa-segment-text, .sol-segment-desc, .sol-text-main {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-md) !important;
        line-height: var(--ca-line-relaxed) !important;
        font-weight: var(--ca-weight-regular) !important;
        letter-spacing: var(--ca-tracking-normal) !important;
    }

    /* BOTÕES GERAIS */
    .ca-btn-primary, .ca-btn-secondary, .sol-cta-btn, .ca-card-cta {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-sm) !important;
        font-weight: var(--ca-weight-bold) !important;
        letter-spacing: var(--ca-tracking-wider) !important;
        text-transform: uppercase !important;
    }

    /* EYEBROWS (Sobrancelhas) */
    .ca-eyebrow, .sol-title-eyebrow, .ca-segmentos-eyebrow {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-xs) !important;
        font-weight: var(--ca-weight-bold) !important;
        letter-spacing: var(--ca-tracking-widest) !important;
        text-transform: uppercase !important;
    }

    /* MENU DESKTOP */
    #menu-menu-principal-1 li a, .menu-item a {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-sm) !important;
        font-weight: var(--ca-weight-semibold) !important;
        letter-spacing: var(--ca-tracking-wide) !important;
    }

    /* FOOTER TEXTOS */
    #footer p, #footer .textwidget, #footer a {
        font-family: var(--ca-font-primary, sans-serif) !important;
        font-size: var(--ca-text-sm) !important;
        line-height: var(--ca-line-relaxed) !important;
    }
}
"@

$css += $desktopCss
[System.IO.File]::WriteAllText($cssPath, $css, $utf8NoBom)
Write-Output "Typography Desktop styles appended!"
