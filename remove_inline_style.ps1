$ErrorActionPreference = "Stop"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$file = "index.html"
$html = [System.IO.File]::ReadAllText($file, $utf8NoBom)

# Regex to remove the exact <style> block containing --wp--preset--aspect-ratio
$pattern = '(?s)<style>\s*:root\s*{.*?--ca-font-primary:.*?</style>'
$newHtml = [regex]::Replace($html, $pattern, '')

if ($html -ne $newHtml) {
    [System.IO.File]::WriteAllText($file, $newHtml, $utf8NoBom)
    Write-Output "Style block removed successfully."
} else {
    Write-Output "Style block not found."
}
