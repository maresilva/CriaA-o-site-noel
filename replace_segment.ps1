$html = Get-Content "index.html" -Encoding UTF8
$newSeg = Get-Content "new_segment.html" -Encoding UTF8

$startIdx = -1
$endIdx = -1

for ($i = 0; $i -lt $html.Count; $i++) {
    if ($html[$i] -match "<!-- START OUTROS SEGMENTOS SECTION -->") {
        $startIdx = $i
        break
    }
}

for ($i = $startIdx; $i -lt $html.Count; $i++) {
    if ($html[$i] -match "<!-- START PORTFOLIO SECTION -->") {
        $endIdx = $i
        break
    }
}

if ($startIdx -ge 0 -and $endIdx -gt $startIdx) {
    $pre = $html[0..($startIdx - 1)]
    $post = $html[$endIdx..($html.Count - 1)]
    $result = $pre + $newSeg + $post
    $result | Set-Content "index.html" -Encoding UTF8
    Write-Host "Replaced successfully! Start: $startIdx, End: $endIdx"
} else {
    Write-Host "Indices not found! Start: $startIdx, End: $endIdx"
}
