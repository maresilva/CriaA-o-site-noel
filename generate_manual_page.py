import os

with open('solucoes.html', 'r', encoding='utf-8') as f:
    content = f.read()

header_idx = content.find('<main id="solucoes-main">')
footer_idx = content.find('<footer class="clearfix mfn-footer" id="Footer"')

if header_idx != -1 and footer_idx != -1:
    # Header includes everything up to but excluding <main id="solucoes-main">
    header = content[:header_idx]
    
    # We will close the <main> manually, so we just take the footer from the start of <footer ...>
    footer = content[footer_idx:]
    
    # Update title and meta description in header
    import re
    header = re.sub(r'<title>.*?</title>', '<title>Manual do Verdadeiro Papai Noel | CriaAção Entretenimento</title>', header, flags=re.IGNORECASE)
    header = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Conheça o Manual do Verdadeiro Papai Noel, conteúdo digital exclusivo disponibilizado aos clientes dos projetos natalinos da CriaAção.">', header, flags=re.IGNORECASE)
    header = re.sub(r'<link rel="canonical" href="[^"]*" />', '<link rel="canonical" href="https://www.criaacao.com/solucoes/manual-do-verdadeiro-papai-noel" />', header, flags=re.IGNORECASE)
    
    # Remove old padding overrides in header if any
    header = re.sub(r'<!-- MOBILE PADDING OVERRIDE FIX -->.*?style>', '', header, flags=re.IGNORECASE | re.DOTALL)
    
    # Set the active menu correctly in the script
    header = re.sub(r'var page = path.split\(\'/\'\)\.pop\(\);', "var page = 'solucoes.html';", header)

    new_hero = """
    <main id="manual-main">
      <!-- ==============================================
           HERO: MANUAL DO VERDADEIRO PAPAI NOEL
      =============================================== -->
      <style>
        .manual-hero-section {
          position: relative;
          padding: 200px 20px 100px; /* Large top padding to account for fixed header */
          background: linear-gradient(135deg, #0a0102 0%, #1a0304 40%, #3a0305 70%, #0a0102 100%);
          overflow: hidden;
          color: #fff;
          min-height: 90vh;
          display: flex;
          align-items: center;
        }
        
        .manual-hero-bg-effects {
          position: absolute;
          inset: 0;
          pointer-events: none;
          z-index: 0;
        }
        
        .manual-hero-bg-effects::after {
          content: '';
          position: absolute;
          top: 0;
          right: -10%;
          width: 60%;
          height: 100%;
          background: radial-gradient(circle at center, rgba(212, 175, 55, 0.15) 0%, transparent 60%);
          filter: blur(60px);
        }

        .manual-hero-container {
          position: relative;
          z-index: 10;
          max-width: 1240px;
          margin: 0 auto;
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 60px;
          align-items: center;
        }
        
        /* Breadcrumb */
        .manual-breadcrumb {
          font-family: var(--mfn-woo-font-family, 'Inter', sans-serif);
          font-size: 13px;
          color: rgba(255,255,255,0.6);
          margin-bottom: 24px;
          animation: fadeUp 1s ease forwards;
          opacity: 0;
        }
        .manual-breadcrumb a {
          color: rgba(255,255,255,0.6);
          text-decoration: none;
          transition: color 0.3s ease;
        }
        .manual-breadcrumb a:hover {
          color: #D4AF37;
        }
        .manual-breadcrumb .current {
          color: #D4AF37;
          pointer-events: none;
        }
        .manual-breadcrumb .separator {
          margin: 0 8px;
          font-size: 10px;
        }

        /* Left Content */
        .manual-hero-content {
          max-width: 600px;
        }

        .manual-eyebrow {
          font-family: var(--mfn-woo-font-family, 'Inter', sans-serif);
          font-size: 14px;
          font-weight: 700;
          letter-spacing: 4px;
          color: #D4AF37;
          text-transform: uppercase;
          margin-bottom: 16px;
          display: block;
          animation: fadeUp 1s ease 0.1s forwards;
          opacity: 0;
        }

        .manual-title {
          font-family: var(--mfn-heading-font-family, 'Cinzel', serif);
          font-size: clamp(40px, 5vw, 64px);
          line-height: 1.1;
          font-weight: 700;
          margin-bottom: 24px;
          text-shadow: 0 4px 20px rgba(0,0,0,0.5);
          animation: fadeUp 1s ease 0.2s forwards;
          opacity: 0;
        }
        
        .manual-title span {
          color: #D4AF37;
        }

        .manual-desc {
          font-family: var(--mfn-woo-font-family, 'Inter', sans-serif);
          font-size: 18px;
          line-height: 1.6;
          color: rgba(255,255,255,0.85);
          margin-bottom: 32px;
          animation: fadeUp 1s ease 0.3s forwards;
          opacity: 0;
        }

        /* Badge */
        .manual-badge {
          display: inline-flex;
          align-items: center;
          gap: 12px;
          background: rgba(212, 175, 55, 0.1);
          border: 1px solid rgba(212, 175, 55, 0.3);
          border-radius: 8px;
          padding: 12px 20px;
          margin-bottom: 40px;
          backdrop-filter: blur(5px);
          animation: fadeUp 1s ease 0.4s forwards;
          opacity: 0;
        }
        .manual-badge svg {
          width: 24px;
          height: 24px;
          color: #D4AF37;
          flex-shrink: 0;
        }
        .manual-badge span {
          font-size: 13px;
          font-weight: 600;
          color: #ffffff;
          letter-spacing: 0.5px;
        }

        /* Buttons */
        .manual-buttons {
          display: flex;
          gap: 16px;
          animation: fadeUp 1s ease 0.5s forwards;
          opacity: 0;
        }

        .manual-btn-primary {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, #D4AF37 0%, #AA8C2C 100%);
          color: #1a050a !important;
          padding: 16px 32px;
          border-radius: 50px;
          font-weight: 700;
          font-size: 15px;
          text-decoration: none;
          transition: all 0.3s ease;
          box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        }
        .manual-btn-primary:hover {
          transform: translateY(-2px);
          box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
          color: #1a050a !important;
        }

        .manual-btn-secondary {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          background: transparent;
          border: 1px solid rgba(212, 175, 55, 0.6);
          color: #ffffff !important;
          padding: 16px 32px;
          border-radius: 50px;
          font-weight: 600;
          font-size: 15px;
          text-decoration: none;
          transition: all 0.3s ease;
        }
        .manual-btn-secondary:hover {
          border-color: #D4AF37;
          background: rgba(212, 175, 55, 0.05);
          color: #D4AF37 !important;
        }

        /* Right Content - Mockup */
        .manual-hero-visual {
          position: relative;
          display: flex;
          justify-content: center;
          align-items: center;
          animation: fadeUp 1.2s cubic-bezier(0.2, 0.8, 0.2, 1) 0.6s forwards;
          opacity: 0;
        }

        .manual-mockup-img {
          width: 100%;
          max-width: 500px;
          height: auto;
          filter: drop-shadow(0 30px 40px rgba(0,0,0,0.6));
          animation: float 6s ease-in-out infinite;
        }

        @keyframes fadeUp {
          from { opacity: 0; transform: translateY(30px); }
          to { opacity: 1; transform: translateY(0); }
        }

        @keyframes float {
          0% { transform: translateY(0); }
          50% { transform: translateY(-15px); }
          100% { transform: translateY(0); }
        }

        /* Responsiveness */
        @media (max-width: 980px) {
          .manual-hero-container {
            grid-template-columns: 1fr;
            text-align: center;
            gap: 40px;
          }
          .manual-hero-content {
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
          }
          .manual-badge {
            text-align: left;
          }
          .manual-buttons {
            flex-direction: column;
            width: 100%;
          }
          .manual-buttons a {
            width: 100%;
          }
          .manual-hero-visual {
            order: 2; /* Visual below content */
          }
          .manual-hero-section {
            padding: 160px 20px 80px;
          }
        }
      </style>

      <section class="manual-hero-section">
        <div class="manual-hero-bg-effects"></div>
        <div class="manual-hero-container">
          
          <!-- Coluna Esquerda -->
          <div class="manual-hero-content">
            <nav class="manual-breadcrumb" aria-label="Breadcrumb">
              <a href="index.html">Home</a> 
              <span class="separator">/</span> 
              <a href="solucoes.html">Soluções</a> 
              <span class="separator">/</span> 
              <span class="current" aria-current="page">Manual do Verdadeiro Papai Noel</span>
            </nav>

            <span class="manual-eyebrow">Conhecimento que encanta</span>
            
            <h1 class="manual-title">Manual do Verdadeiro <span>Papai Noel</span></h1>
            
            <p class="manual-desc">
              Um conteúdo exclusivo para quem acredita que a magia do Natal também nasce do preparo, da presença e de cada detalhe da experiência.
            </p>

            <div class="manual-badge">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>
              </svg>
              <span>VERSÃO DIGITAL GRATUITA PARA CLIENTES DA CRIAAÇÃO</span>
            </div>

            <div class="manual-buttons">
              <a href="contato.html" class="manual-btn-primary" aria-label="Solicitar um projeto">SOLICITAR UM PROJETO</a>
              <a href="#detalhes-manual" class="manual-btn-secondary" aria-label="Conhecer o manual">CONHECER O MANUAL</a>
            </div>
          </div>

          <!-- Coluna Direita -->
          <div class="manual-hero-visual">
            <!-- 
              Substituir src desta imagem pela capa final quando fornecida pelo cliente. 
              Variável/Componente: MOCKUP_LIVRO_PAPAI_NOEL 
            -->
            <img src="assets/images/portfolio/mockup-manual-papai-noel.png" 
                 alt="Mockup tridimensional do livro Manual do Verdadeiro Papai Noel" 
                 class="manual-mockup-img"
                 width="600" height="800"
                 loading="eager" />
          </div>
          
        </div>
      </section>

      <!-- Blank target section for scroll anchor -->
      <section id="detalhes-manual" style="padding: 40px 20px; text-align: center; color: #fff;">
         <!-- Conteúdo futuro da página irá aqui -->
      </section>
      
    </main>
"""

    final_content = header + new_hero + footer
    
    with open('manual-do-verdadeiro-papai-noel.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("manual-do-verdadeiro-papai-noel.html created successfully.")
else:
    print("Could not match header and footer.")
