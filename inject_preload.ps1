$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Encoding UTF8 -Raw
    
    $preloadTag = "`n  <link rel=`"preload`" as=`"image`" href=`"assets/logos/logo-criaacao-entretenimento.png`">"
    
    # Insert right after <meta charset="utf-8" />
    if ($content -notmatch 'as="image" href="assets/logos/logo-criaacao-entretenimento.png"') {
        $newContent = $content -replace '(<meta charset="utf-8" />)', "`$1$preloadTag"
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        Write-Host "Injected preload in $($file.Name)"
    }
}
