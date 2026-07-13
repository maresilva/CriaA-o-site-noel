document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('ca-trabalhe-form');
    const successMsg = document.getElementById('ca-form-success-msg');
    const submitBtn = document.getElementById('submit-btn');
    
    // File inputs updates
    const pdfInput = document.getElementById('cv_pdf');
    const pdfName = document.getElementById('pdf_name');
    
    const videoInput = document.getElementById('cv_video');
    const videoName = document.getElementById('video_name');
    
    if(pdfInput) {
        pdfInput.addEventListener('change', function(e) {
            if(this.files && this.files.length > 0) {
                pdfName.textContent = "Arquivo selecionado: " + this.files[0].name;
                pdfName.style.color = "var(--ca-gold-500)";
            } else {
                pdfName.textContent = "Tamanho máximo: 5MB";
                pdfName.style.color = "";
            }
        });
    }
    
    if(videoInput) {
        videoInput.addEventListener('change', function(e) {
            if(this.files && this.files.length > 0) {
                videoName.textContent = "Arquivo selecionado: " + this.files[0].name;
                videoName.style.color = "var(--ca-gold-500)";
            } else {
                videoName.textContent = "Tamanho máximo: 50MB (mp4, mov)";
                videoName.style.color = "";
            }
        });
    }
    
    if(form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Check HTML5 validation
            if (!form.checkValidity()) {
                form.reportValidity();
                return;
            }
            
            // LGPD Check
            const lgpd = document.getElementById('lgpd');
            if(!lgpd.checked) {
                alert("Por favor, aceite os termos da LGPD para continuar.");
                return;
            }
            
            const formData = new FormData(form);
            
            // Disable button and show loading state
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Enviando... <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="spin"><path d="M21 12a9 9 0 1 1-6.219-8.56"></path></svg>';
            
            if(!document.getElementById('spin-style')) {
                const style = document.createElement('style');
                style.id = 'spin-style';
                style.innerHTML = '@keyframes spin { 100% { transform: rotate(360deg); } } .spin { animation: spin 1s linear infinite; }';
                document.head.appendChild(style);
            }
            
            // Send email using formsubmit.co AJAX
            fetch("https://formsubmit.co/ajax/marcos.criaacao@gmail.com", {
                method: "POST",
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Success
                form.style.display = 'none';
                successMsg.style.display = 'block';
                successMsg.scrollIntoView({behavior: "smooth", block: "center"});
            })
            .catch(error => {
                console.error('Error:', error);
                alert("Ocorreu um erro ao enviar. Por favor, tente novamente mais tarde.");
                submitBtn.disabled = false;
                submitBtn.innerHTML = 'Cadastrar Currículo <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>';
            });
        });
    }
});