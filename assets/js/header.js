document.addEventListener('DOMContentLoaded', function() {
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
});