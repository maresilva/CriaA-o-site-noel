$files = @("index.html", "contato.html", "quem-somos.html", "solucoes.html", "portfolio.html", "trabalhe-conosco.html")

# 1. Read temp_header_style_block.css and extract the actual Header CSS part
$cssBlock = [System.IO.File]::ReadAllText("temp_header_style_block.css", [System.Text.Encoding]::UTF8)
$headerCssStart = $cssBlock.IndexOf("/* Header using original selectors */")
if ($headerCssStart -eq -1) { $headerCssStart = $cssBlock.IndexOf("#Header_wrapper {") }
$headerCss = $cssBlock.Substring($headerCssStart).Replace("</style>", "").Trim()

# Fix the bad selector in headerCss just in case it's there
$headerCss = $headerCss.Replace("#Wrapper.ca-wrapper       #Header_wrapper {", "#Header_wrapper {")

# Write to assets/css/header.css
[System.IO.File]::WriteAllText("assets/css/header.css", $headerCss, [System.Text.Encoding]::UTF8)
Write-Host "Created assets/css/header.css"

# 2. Create assets/js/header.js
$js = "document.addEventListener('DOMContentLoaded', function() {
    // Active menu item logic
    var currentPage = window.location.pathname.split('/').pop();
    if (!currentPage || currentPage === '') currentPage = 'index.html';
    
    var navLinks = document.querySelectorAll('.menu-main a');
    navLinks.forEach(function(link) {
        var href = link.getAttribute('href');
        if (href && (href === currentPage || (currentPage === 'index.html' && href === '/'))) {
            link.style.color = '#F2B84B';
        }
    });

    // Sticky header logic
    const topbar = document.querySelector('#Top_bar');
    if (topbar) {
        window.addEventListener('scroll', () => {
            topbar.classList.toggle('is-sticky', window.scrollY > 24);
        }, { passive: true });
        
        // Check initial state
        if (window.scrollY > 24) {
            topbar.classList.add('is-sticky');
        }
    }
});"

[System.IO.File]::WriteAllText("assets/js/header.js", $js, [System.Text.Encoding]::UTF8)
Write-Host "Created assets/js/header.js"