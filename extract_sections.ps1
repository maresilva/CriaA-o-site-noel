$content = Get-Content solucoes.html -Encoding UTF8
for ($i=0; $i -lt $content.Length; $i++) {
    $line = $content[$i].Trim()
    if ($line -match '^<section' -or $line -match '^<div id="Content"') {
        Write-Output "$($i): $line"
    }
}
