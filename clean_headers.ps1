$files = @("index.html", "contato.html", "quem-somos.html", "solucoes.html", "portfolio.html", "trabalhe-conosco.html")

foreach ($f in $files) {
    if (-not (Test-Path $f)) {
        Write-Host "Skipping $f (not found)"
        continue
    }

    $content = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

    # Remove WP styles
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<style id="global-styles-inline-css">.*?</style>', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<style id="wp-emoji-styles-inline-css">.*?</style>', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<style id="classic-theme-styles-inline-css">.*?</style>', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<style id="mfn-dynamic-inline-css">.*?</style>', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<style id="wp-block-library-inline-css">.*?</style>', '')

    # Insert <link rel="stylesheet" href="assets/css/header-global.css"> right before </head>
    if (-not $content.Contains('header-global.css')) {
        $content = $content.Replace('</head>', "  <link rel='stylesheet' href='assets/css/header-global.css'>
</head>")
    }

    # Now, we need to remove the inline CSS for Header_wrapper and Top_bar.
    $heroIdx = $content.IndexOf('/* CSS for the perfected Hero */')
    if ($heroIdx -ge 0) {
        $headerStart = $content.IndexOf('#Header_wrapper {', $heroIdx)
        $styleEnd = $content.IndexOf('</style>', $heroIdx)
        if ($headerStart -ge 0 -and $headerStart -lt $styleEnd) {
            $before = $content.Substring(0, $headerStart)
            $after = $content.Substring($styleEnd)
            $content = $before + $after
        }
    }

    # Remove the bad header CSS in internal pages' :root block
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Header_wrapper\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Wrapper\.ca-wrapper\s*#Header_wrapper\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Top_bar\.ca-topbar\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Top_bar\.ca-topbar\.is-scrolled\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)@media\s*\(max-width:\s*980px\)\s*\{\s*body\s*#Top_bar.*?\}\s*\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Top_bar\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Top_bar\.is-sticky\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)#Top_bar\.is-sticky\s*\.logo\s*img\s*\{.*?\}', '')
    $content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)\.top_bar_left\s*\{.*?\}', '')

    [System.IO.File]::WriteAllText($f, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Processed $f"
}
