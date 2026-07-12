$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Encoding UTF8 -Raw
    
    # We will use regex to find all <img ...> tags
    $pattern = '(?i)<img\s+([^>]+)>'
    
    $evaluator = {
        param($match)
        $attributes = $match.Groups[1].Value
        
        # Don't lazy load the main logo just to be safe (LCP)
        if ($attributes -match 'logo-criaacao-entretenimento' -or $attributes -match 'class=".*?(hero|logo).*?"' -or $attributes -match 'id=".*?(hero|logo).*?"') {
            # Still check for alt
            if ($attributes -notmatch '(?i)alt=') {
                $attributes += ' alt=""'
            }
            return "<img $attributes>"
        }
        
        if ($attributes -notmatch '(?i)loading=') {
            $attributes += ' loading="lazy"'
        }
        if ($attributes -notmatch '(?i)decoding=') {
            $attributes += ' decoding="async"'
        }
        if ($attributes -notmatch '(?i)alt=') {
            $attributes += ' alt=""'
        }
        
        return "<img $attributes>"
    }
    
    # We must use [regex]::Replace with a MatchEvaluator
    # PowerShell supports passing a scriptblock to [regex]::Replace in Core, but in older versions it might not.
    # To be safe and compatible with PS 5.1:
    $regex = [regex]$pattern
    $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, [System.Text.RegularExpressions.MatchEvaluator] {
        param($match)
        $attributes = $match.Groups[1].Value
        
        if ($attributes -match 'logo-criaacao-entretenimento' -or $attributes -match 'class=".*?(hero|logo).*?"' -or $attributes -match 'id=".*?(hero|logo).*?"') {
            if ($attributes -notmatch '(?i)alt=') {
                $attributes += ' alt=""'
            }
            return "<img $attributes>"
        }
        
        if ($attributes -notmatch '(?i)loading=') {
            $attributes += ' loading="lazy"'
        }
        if ($attributes -notmatch '(?i)decoding=') {
            $attributes += ' decoding="async"'
        }
        if ($attributes -notmatch '(?i)alt=') {
            $attributes += ' alt=""'
        }
        
        return "<img $attributes>"
    })
    
    Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
    Write-Host "Processed $($file.Name)"
}
