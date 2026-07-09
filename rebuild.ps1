$htmlPath = "solucoes.html"
$payloadPath = "sol_payload.txt"

# Read the clean file and the payload
$htmlContent = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)
$payloadContent = [System.IO.File]::ReadAllText($payloadPath, [System.Text.Encoding]::UTF8)

# Move meta charset to top of <head>
$htmlContent = $htmlContent -replace '(?i)\s*<meta charset="utf-8"\s*/>', ""
$htmlContent = $htmlContent -replace '(?i)<head>', "<head>`n  <meta charset=`"utf-8`" />"

# Fix the title using Base64 to bypass script encoding issues
# Base64 string is <title>CriaAção Entretenimento | Soluções Natalinas Exclusivas</title>
$titleBytes = [System.Convert]::FromBase64String("PHRpdGxlPkNyaWFBw6fDo28gRW50cmV0ZW5pbWVudG8gfCBTb2x1w6fDtWVzIE5hdGFsaW5hcyBFeGNsdXNpdmFzPC90aXRsZT4=")
$titleStr = [System.Text.Encoding]::UTF8.GetString($titleBytes)
$htmlContent = $htmlContent -replace '(?s)<title>.*?</title>', $titleStr

# Change the CSS link
$htmlContent = $htmlContent.Replace('assets/css/quem-somos.css', 'assets/css/solucoes.css')

# Replace the main content block
$htmlContent = $htmlContent -replace '(?s)<!-- MAIN CONTENT: QUEM SOMOS -->\s*<main id="quem-somos-main">.*?</main>', $payloadContent

# Replace any lingering <a href="index.html#solucoes">SOLU&Ccedil;&Otilde;ES</a> with proper link for this page
$htmlContent = $htmlContent.Replace('<a href="index.html#solucoes">SOLU&Ccedil;&Otilde;ES</a>', '<a href="solucoes.html" style="color: #F2B84B;">SOLU&Ccedil;&Otilde;ES</a>')
$htmlContent = $htmlContent.Replace('<a href="quem-somos.html" style="color: #F2B84B;">Quem Somos</a>', '<a href="quem-somos.html">Quem Somos</a>')

# Save back
[System.IO.File]::WriteAllText($htmlPath, $htmlContent, [System.Text.Encoding]::UTF8)

Write-Host "Solucoes rebuilt cleanly."
