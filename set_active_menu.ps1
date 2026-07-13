$files = @("index.html", "contato.html", "quem-somos.html", "solucoes.html", "portfolio.html")

foreach ($f in $files) {
    if (-not (Test-Path $f)) { continue }
    $content = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)

    # 1. Update the CSS to include active state if it doesn't exist
    if (-not $content.Contains('.menu-main li.active a')) {
        $cssToAdd = ".menu-main a:hover,
      .menu-main li.active a {
        color: #F2B84B;
      }"
        $content = $content.Replace('.menu-main a:hover {
        color: #F2B84B;
      }', $cssToAdd)
        # Handle case where the regex might differ in whitespace
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, '\.menu-main\s+a:hover\s*\{\s*color:\s*#F2B84B;\s*\}', $cssToAdd)
    }

    # 2. Add the active class to the correct li
    # First, remove any existing active class to be safe
    $content = $content.Replace('<li class="active">', '<li>')
    
    # Then add it to the correct one
    $linkTarget = 'href="' + $f + '"'
    $content = $content.Replace('<li><a ' + $linkTarget, '<li class="active"><a ' + $linkTarget)
    
    [System.IO.File]::WriteAllText($f, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Set active state in $f"
}
