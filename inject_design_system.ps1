$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

$filesToProcess = @("index.html", "quem-somos.html", "solucoes.html", "portfolio.html", "contato.html")
$stylesheetLink = '    <link href="assets/css/design-system.css" rel="stylesheet" type="text/css" />'

foreach ($file in $filesToProcess) {
    if (Test-Path $file) {
        $html = [System.IO.File]::ReadAllText($file, $utf8NoBom)
        
        # Check if already injected
        if (-not $html.Contains("design-system.css")) {
            # Find </head> and replace it with $stylesheetLink + `n` + </head>
            $pattern = '(?i)</head>'
            $replacement = "$stylesheetLink`n</head>"
            
            $newHtml = [regex]::Replace($html, $pattern, $replacement)
            [System.IO.File]::WriteAllText($file, $newHtml, $utf8NoBom)
            Write-Output "Injected into $file"
        } else {
            Write-Output "Already injected in $file"
        }
    } else {
        Write-Output "File $file not found!"
    }
}
