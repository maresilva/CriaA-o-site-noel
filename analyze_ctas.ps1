$files = @("index.html", "quem-somos.html", "solucoes.html", "portfolio.html", "contato.html")
foreach ($file in $files) {
    Write-Output "========================================"
    Write-Output "PAGE: $file"
    Write-Output "========================================"
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding UTF8
        # Match anchor tags that have href
        $matches = [regex]::Matches($content, '(?i)<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>')
        foreach ($m in $matches) {
            $fullTag = $m.Groups[0].Value
            $href = $m.Groups[1].Value
            # Basic cleanup of inner text
            $text = $m.Groups[2].Value -replace '<[^>]+>','' -replace '\s+',' '
            $text = $text.Trim()
            
            # Check if it looks like a button/CTA
            $isCTA = ($fullTag -match '(?i)class="[^"]*(btn|button|cta)[^"]*"')
            $type = if ($isCTA) { "[CTA]" } else { "[LINK]" }
            
            if ($text) {
                Write-Output "$type Text: '$text' -> Href: '$href'"
            }
        }
    } else {
        Write-Output "File not found."
    }
}
