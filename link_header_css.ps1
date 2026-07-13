$files = @("index.html", "contato.html", "quem-somos.html", "solucoes.html", "portfolio.html")

foreach ($file in $files) {
    if (-not (Test-Path $file)) { continue }
    $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)

    # Make sure header-global.css is linked
    if (-not $content.Contains("header-global.css")) {
        $headEnd = $content.IndexOf('</head>')
        if ($headEnd -ge 0) {
            $linkTag = "`n    <link rel=`"stylesheet`" href=`"assets/css/header-global.css`">`n"
            $content = $content.Substring(0, $headEnd) + $linkTag + $content.Substring($headEnd)
            [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
            Write-Host "Added header-global.css to $file"
        }
    } else {
        Write-Host "$file already has header-global.css"
    }
}