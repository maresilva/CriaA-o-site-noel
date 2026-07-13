$indexContent = [System.IO.File]::ReadAllText("index.html", [System.Text.Encoding]::UTF8)

# Extract Header from index.html
$headerStart = $indexContent.IndexOf('<div id="Header_wrapper">')
$headerEnd = $indexContent.IndexOf('</div>', $indexContent.IndexOf('</header>')) + 6
$headerHtml = $indexContent.Substring($headerStart, $headerEnd - $headerStart)

$files = @("contato.html", "quem-somos.html", "solucoes.html", "portfolio.html")

foreach ($file in $files) {
    if (-not (Test-Path $file)) { continue }
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

    # Replace Header
    $fStart = $content.IndexOf('<div id="Header_wrapper">')
    if ($fStart -ge 0) {
        $fEnd = $content.IndexOf('</div>', $content.IndexOf('</header>')) + 6
        $content = $content.Substring(0, $fStart) + $headerHtml + $content.Substring($fEnd)
    }

    # Make sure header-global.css is linked
    if (-not $content.Contains("header-global.css")) {
        $headEnd = $content.IndexOf('</head>')
        if ($headEnd -ge 0) {
            $linkTag = "`n    <link rel=`"stylesheet`" href=`"assets/css/header-global.css`">`n"
            $content = $content.Substring(0, $headEnd) + $linkTag + $content.Substring($headEnd)
        }
    }

    # Save
    [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Synced header in $file"
}