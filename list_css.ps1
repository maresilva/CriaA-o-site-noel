$html = Get-Content index.html -Raw
$matches = [regex]::Matches($html, '<link[^>]*stylesheet[^>]*>')
foreach ($m in $matches) {
    Write-Output $m.Value
}
