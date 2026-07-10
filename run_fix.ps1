$replacements = @(
    @('atua\uFFFD\uFFFDo', 'atuação'),
    @('emo\uFFFD\uFFFDo', 'emoção'),
    @('excel\uFFFDncia', 'excelência'),
    @('Excel\uFFFDncia', 'Excelência'),
    @('experi\uFFFDncia', 'experiência'),
    @('Experi\uFFFDncia', 'Experiência'),
    @('H\uFFFD mais', 'Há mais'),
    @('solu\uFFFDes', 'soluções'),
    @('CriaA\uFFFDo', 'CriaAção'),
    @('espa\uFFFDo', 'espaço'),
    @('fotogr\uFFFDfico', 'fotográfico'),
    @('360\uFFFD', '360°'),
    @('opera\uFFFD\uFFFDo', 'operação'),
    @('memor\uFFFDveis', 'memoráveis'),
    @('s\uFFFDo\s', 'são '),
    @('l\uFFFDdica', 'lúdica'),
    @('impec\uFFFDvel', 'impecável'),
    @('in\uFFFDcio', 'início'),
    @('pa\uFFFDs', 'país'),
    @('prop\uFFFDsito', 'propósito'),
    @('inesquec\uFFFDvel', 'inesquecível'),
    @('mem\uFFFDria', 'memória'),
    @('voc\uFFFD\s', 'você '),
    @('Pol\uFFFDtica', 'Política'),
    @('Prote\uFFFD\uFFFDo', 'Proteção'),
    @('conex\uFFFDes', 'conexões'),
    @('cria\uFFFD\uFFFDo', 'criação'),
    @('produ\uFFFD\uFFFDo', 'produção'),
    @('organiza\uFFFD\uFFFDo', 'organização'),
    @('milh\uFFFDes', 'milhões'),
    @('refer\uFFFDncia', 'referência'),
    @('Mam\uFFFDe', 'Mamãe'),
    @('conte\uFFFDdo', 'conteúdo'),
    @('compartilh\uFFFDvel', 'compartilhável'),
    @('seguran\uFFFDa', 'segurança'),
    @('j\uFFFD\satuou', 'já atuou'),
    
    @('atua\uFFFDo', 'atuação'),
    @('emo\uFFFDo', 'emoção'),
    @('opera\uFFFDo', 'operação'),
    @('Prote\uFFFDo', 'Proteção'),
    @('cria\uFFFDo', 'criação'),
    @('produ\uFFFDo', 'produção'),
    @('organiza\uFFFDo', 'organização')
)

$utf8NoBom = New-Object System.Text.UTF8Encoding $False
$files = Get-ChildItem -Filter "*.html"

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
    foreach ($pair in $replacements) {
        $content = [regex]::Replace($content, $pair[0], $pair[1], [System.Text.RegularExpressions.RegexOptions]::None)
    }
    [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBom)
    Write-Host "Fixed $($file.Name)"
}