$htmlPath = "solucoes.html"
$payloadPath = "sol_payload.txt"

# Read both files as UTF8 (this correctly interprets the characters)
$htmlContent = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)
$payloadContent = [System.IO.File]::ReadAllText($payloadPath, [System.Text.Encoding]::UTF8)

# Because we are replacing the entire block, we'll use a regex that matches from the comment to the closing </main>
$htmlContent = $htmlContent -replace '(?s)<!-- MAIN CONTENT: SOLUCOES -->\s*<main id="solucoes-main">.*?</main>', $payloadContent

# Overwrite the HTML file, ensuring UTF-8
[System.IO.File]::WriteAllText($htmlPath, $htmlContent, [System.Text.Encoding]::UTF8)

Write-Host "Fix applied."
