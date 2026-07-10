$html = Get-Content -Path contato.html -Raw -Encoding UTF8
$start = '<!-- MAIN CONTENT: SOLUCOES -->'
$end = '</main>'
$startIndex = $html.IndexOf($start)
$endIndex = $html.IndexOf($end, $startIndex) + $end.Length

if ($startIndex -ge 0 -and $endIndex -gt $startIndex) {
    $newContent = Get-Content -Path contato_content.txt -Raw -Encoding UTF8
    $result = $html.Substring(0, $startIndex) + $newContent + $html.Substring($endIndex)
    Set-Content -Path contato.html -Value $result -Encoding UTF8
    Write-Host "Replaced successfully!"
} else {
    Write-Host "Markers not found!"
}
