$htmlFiles = Get-ChildItem -Path "." -Filter "*.html"

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # We will search for <li><a href="solucoes.html">SOLU&Ccedil;&Otilde;ES</a></li>
    # and append the new menu item right after it.
    
    $searchString = '<li><a href="solucoes.html">SOLU&Ccedil;&Otilde;ES</a></li>'
    $replacement = '<li><a href="solucoes.html">SOLU&Ccedil;&Otilde;ES</a></li>' + "`r`n" + '                <li><a href="onde-atuamos.html">Onde Atuamos</a></li>'
    
    if ($content -match '<li><a href="onde-atuamos.html">') {
        Write-Output "$($file.Name) already has Onde Atuamos in the menu."
        continue
    }
    
    if ($content -match [regex]::Escape($searchString)) {
        $newContent = $content -replace [regex]::Escape($searchString), $replacement
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        Write-Output "Updated menu in $($file.Name)"
    } else {
        Write-Output "Could not find target menu item in $($file.Name)"
    }
}
Write-Output "Done updating menus."
