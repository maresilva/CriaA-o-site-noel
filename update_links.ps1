$files = @("index.html", "quem-somos.html", "solucoes.html")

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
        
        if ($file -eq "solucoes.html") {
            # Remove highlight from Quem Somos
            $content = $content.Replace('<a href="quem-somos.html" style="color: #F2B84B;">Quem Somos</a>', '<a href="quem-somos.html">Quem Somos</a>')
            # Add highlight to Solucoes and point to itself
            $content = $content.Replace('<a href="index.html#solucoes">SOLU&Ccedil;&Otilde;ES</a>', '<a href="solucoes.html" style="color: #F2B84B;">SOLU&Ccedil;&Otilde;ES</a>')
        } elseif ($file -eq "quem-somos.html") {
            $content = $content.Replace('href="index.html#solucoes"', 'href="solucoes.html"')
        } elseif ($file -eq "index.html") {
            $content = $content.Replace('<a href="#solucoes">SOLU&Ccedil;&Otilde;ES</a>', '<a href="solucoes.html">SOLU&Ccedil;&Otilde;ES</a>')
            $content = $content.Replace('href="#solucoes" class="ca-button-main"', 'href="solucoes.html" class="ca-button-main"')
        }
        
        [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
    }
}
