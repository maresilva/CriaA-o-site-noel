$files = @("contato.html", "quem-somos.html", "solucoes.html", "portfolio.html")

foreach ($f in $files) {
    if (-not (Test-Path $f)) { continue }
    $content = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

    $brandTokensIdx = $content.IndexOf('/* Brand tokens */')
    if ($brandTokensIdx -ge 0) {
        $styleEnd = $content.IndexOf('</style>', $brandTokensIdx)
        $brandBlock = $content.Substring($brandTokensIdx, $styleEnd - $brandTokensIdx)
        
        # Remove bad header styles from this block
        $brandBlock = [System.Text.RegularExpressions.Regex]::Replace($brandBlock, '(?s)#Header_wrapper\s*\{.*?\}', '')
        $brandBlock = [System.Text.RegularExpressions.Regex]::Replace($brandBlock, '(?s)#Top_bar\.ca-topbar\s*\{.*?\}', '')
        $brandBlock = [System.Text.RegularExpressions.Regex]::Replace($brandBlock, '(?s)#Top_bar\.ca-topbar\.is-scrolled\s*\{.*?\}', '')
        
        $before = $content.Substring(0, $brandTokensIdx)
        $after = $content.Substring($styleEnd)
        
        $content = $before + $brandBlock + $after
        [System.IO.File]::WriteAllText($f, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Cleaned Brand tokens in $f"
    } else {
        Write-Host "No Brand tokens in $f"
    }
}
