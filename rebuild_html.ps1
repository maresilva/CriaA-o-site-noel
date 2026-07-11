$ErrorActionPreference = "Stop"

$lines = Get-Content -Path "solucoes.html" -Encoding UTF8

$headerLines = $lines[0..6965]
$footerLines = $lines[7772..($lines.Length - 1)]

$headerHtml = $headerLines -join "`r`n"
$footerHtml = $footerLines -join "`r`n"

$headerHtml = $headerHtml -replace "(?is)<title>.*?</title>", "<title>Onde Atuamos | Natal para Shopping Centers, Empresas, Escolas e Prefeituras</title>"
$headerHtml = $headerHtml -replace "(?is)<meta name=`"description`" content=`".*?`">", "<meta name=`"description`" content=`"A CriaAção desenvolve experiências natalinas para Shopping Centers, prefeituras, escolas, empresas, residências, buffets e projetos sociais.`">"
$headerHtml = $headerHtml -replace "(?i)</head>", "<link rel=`"stylesheet`" href=`"assets/css/onde-atuamos.css`" type=`"text/css`" media=`"all`" />`r`n</head>"

# Read content
$contentHtml = Get-Content -Path "onde_atuamos_content.txt" -Raw -Encoding UTF8
$contentHtml = $contentHtml -replace "<!-- PAGE CONTENT WILL GO HERE -->", ""

$newHtml = $headerHtml + "`r`n" + $contentHtml + "`r`n" + $footerHtml

Set-Content -Path "onde-atuamos.html" -Value $newHtml -Encoding UTF8
Write-Output "Successfully rebuilt onde-atuamos.html"
