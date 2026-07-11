$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$cssPath = "assets/css/solucoes.css"
$css = [System.IO.File]::ReadAllText($cssPath, $utf8NoBom)

# Add font-family to .oa-title-highlight and .ca-title
$css = $css.Replace(".oa-title-highlight {", ".oa-title-highlight {
    font-family: var(--ca-font-script, 'Great Vibes', cursive);
    font-size: 1.4em;
    font-weight: normal;
    padding: 0 5px;")

# Add a specific override for .ca-title inside .ca-magia-bg
$css += @"

.ca-magia-bg .ca-title {
    font-family: var(--ca-font-display, 'Playfair Display', Georgia, serif);
    font-size: 42px;
    letter-spacing: 1px;
}
"@

[System.IO.File]::WriteAllText($cssPath, $css, $utf8NoBom)
Write-Output "Font improved!"
