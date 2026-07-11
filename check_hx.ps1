$files = Get-ChildItem -Filter *.html
foreach ($f in $files) {
    Write-Host "--- $($f.Name) ---"
    $content = Get-Content -Path $f.FullName -Encoding UTF8 -Raw
    
    $h1s = [regex]::Matches($content, '(?i)<h1[^>]*>(.*?)</h1>')
    Write-Host "H1 Count: $($h1s.Count)"
    foreach ($m in $h1s) {
        # Strip internal tags
        $clean = $m.Groups[1].Value -replace '<[^>]+>','' -replace '\s+', ' '
        Write-Host "  H1: $clean"
    }

    $h2s = [regex]::Matches($content, '(?i)<h2[^>]*>(.*?)</h2>')
    Write-Host "H2 Count: $($h2s.Count)"
    foreach ($m in $h2s) {
        $clean = $m.Groups[1].Value -replace '<[^>]+>','' -replace '\s+', ' '
        Write-Host "  H2: $clean"
    }
}
