$cssPath = "d:\Sites\Criação entretenimento\referencia\criaacao.com\assets\css\solucoes.css"
$cssContent = @"
/* solucoes.css - Design System Premium for Soluções page */
:root {
  --ca-vinho: #1A050A;
  --ca-vinho-light: #2b0a12;
  --ca-dourado: #F2B84B;
  --ca-dourado-dark: #D4AF37;
  --ca-branco: #FFFFFF;
  --ca-vidro: rgba(255, 255, 255, 0.03);
  --ca-vidro-border: rgba(255, 255, 255, 0.08);
  --ca-border-radius: 24px;
}

body {
  background-color: var(--ca-vinho);
  color: var(--ca-branco);
  font-family: 'Nunito', sans-serif;
  overflow-x: hidden;
}

/* Animations */
.sol-reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: all 0.9s cubic-bezier(0.25, 1, 0.5, 1);
}

.sol-reveal.sol-visible {
  opacity: 1;
  transform: translateY(0);
}

.sol-stagger-1 { transition-delay: 100ms; }
.sol-stagger-2 { transition-delay: 200ms; }
.sol-stagger-3 { transition-delay: 300ms; }
.sol-stagger-4 { transition-delay: 400ms; }
.sol-stagger-5 { transition-delay: 500ms; }
.sol-stagger-6 { transition-delay: 600ms; }

/* Global Components */
.sol-section {
  padding: 120px 20px;
  position: relative;
}

.sol-section-alt {
  background: linear-gradient(180deg, var(--ca-vinho) 0%, rgba(43, 10, 18, 0.6) 50%, var(--ca-vinho) 100%);
}

.sol-container {
  max-width: 1200px;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

.sol-title-eyebrow {
  color: var(--ca-dourado);
  font-size: 13px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 4px;
  margin-bottom: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
}

.sol-title-eyebrow::before,
.sol-title-eyebrow::after {
  content: '';
  height: 1px;
  width: 50px;
  background: linear-gradient(90deg, transparent, var(--ca-dourado), transparent);
}

.sol-title-main {
  font-size: clamp(2.5rem, 5vw, 4rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 30px;
  color: var(--ca-branco);
  letter-spacing: -1px;
}

.sol-title-main span {
  color: var(--ca-dourado);
  background: linear-gradient(90deg, #F2B84B, #FFD700);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.sol-text-main {
  font-size: clamp(1.15rem, 2vw, 1.3rem);
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.75);
  margin-bottom: 45px;
  max-width: 750px;
  font-weight: 300;
}

.sol-btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  background: linear-gradient(135deg, var(--ca-dourado) 0%, #E6A73A 100%);
  color: var(--ca-vinho);
  padding: 18px 40px;
  border-radius: 50px;
  font-weight: 800;
  font-size: 1.1rem;
  letter-spacing: 0.5px;
  text-decoration: none;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 10px 20px rgba(242, 184, 75, 0.2);
  position: relative;
  overflow: hidden;
}

.sol-btn-primary::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(rgba(255,255,255,0.4), transparent);
  transform: rotate(45deg);
  transition: all 0.6s ease;
  opacity: 0;
}

.sol-btn-primary:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(242, 184, 75, 0.4);
}

.sol-btn-primary:hover::after {
  opacity: 1;
  transform: rotate(45deg) translate(50%, 50%);
}

/* 1. Hero Institucional */
.sol-hero {
  min-height: 90vh;
  display: flex;
  align-items: center;
  position: relative;
  padding-top: 150px;
  background: 
    linear-gradient(135deg, rgba(26, 5, 10, 0.98) 0%, rgba(26, 5, 10, 0.8) 50%, rgba(26, 5, 10, 0.3) 100%),
    url('../images/backgrounds/background-768x543-criaacao-entretenimento.png') center/cover fixed;
}

.sol-hero::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 150px;
  background: linear-gradient(to top, var(--ca-vinho), transparent);
}

/* 2. Grid de Soluções Principais */
.sol-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 35px;
  margin-top: 70px;
}

.sol-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0.01));
  backdrop-filter: blur(25px);
  -webkit-backdrop-filter: blur(25px);
  border: 1px solid var(--ca-vidro-border);
  border-radius: var(--ca-border-radius);
  padding: 50px 40px;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  height: 100%;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.02), 0 10px 30px rgba(0,0,0,0.2);
}

.sol-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--ca-dourado), #FFF5E1);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.5s cubic-bezier(0.19, 1, 0.22, 1);
}

.sol-card:hover {
  transform: translateY(-12px);
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.08), rgba(255, 255, 255, 0.02));
  border-color: rgba(242, 184, 75, 0.4);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(242, 184, 75, 0.05);
}

.sol-card:hover::before {
  transform: scaleX(1);
}

.sol-card-icon {
  width: 70px;
  height: 70px;
  background: linear-gradient(135deg, rgba(242, 184, 75, 0.15), rgba(242, 184, 75, 0.05));
  border: 1px solid rgba(242, 184, 75, 0.2);
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--ca-dourado);
  margin-bottom: 30px;
  transition: all 0.4s ease;
}

.sol-card-icon svg {
  width: 32px;
  height: 32px;
  filter: drop-shadow(0 0 8px rgba(242, 184, 75, 0.4));
  transition: all 0.4s ease;
}

.sol-card:hover .sol-card-icon {
  background: linear-gradient(135deg, var(--ca-dourado), #D4AF37);
  color: var(--ca-vinho);
  transform: scale(1.05) translateY(-5px);
  box-shadow: 0 10px 20px rgba(242, 184, 75, 0.3);
}

.sol-card:hover .sol-card-icon svg {
  filter: none;
}

.sol-card-title {
  font-size: 1.6rem;
  font-weight: 800;
  margin-bottom: 20px;
  color: var(--ca-branco);
  letter-spacing: -0.5px;
}

.sol-card-text {
  color: rgba(255, 255, 255, 0.65);
  line-height: 1.7;
  font-size: 1.05rem;
  margin-bottom: 0;
  flex-grow: 1;
}

/* 3. Soluções por Segmento */
.sol-segments-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 25px;
  margin-top: 60px;
}

.sol-segment-item {
  background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
  border: 1px solid var(--ca-vidro-border);
  border-radius: 20px;
  padding: 40px 25px;
  text-align: center;
  transition: all 0.4s ease;
  cursor: pointer;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.sol-segment-item:hover {
  border-color: rgba(242, 184, 75, 0.6);
  background: linear-gradient(145deg, rgba(242, 184, 75, 0.1), rgba(255,255,255,0.01));
  transform: translateY(-8px);
  box-shadow: 0 15px 30px rgba(242, 184, 75, 0.15);
}

.sol-segment-title {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--ca-dourado);
  margin-bottom: 12px;
}

.sol-segment-desc {
  font-size: 0.95rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.6);
}

/* 4. Timeline Como Funciona */
.sol-timeline {
  position: relative;
  max-width: 900px;
  margin: 80px auto 0;
}

.sol-timeline::before {
  content: '';
  position: absolute;
  top: 0; left: 50%;
  transform: translateX(-50%);
  width: 2px; height: 100%;
  background: linear-gradient(to bottom, transparent, rgba(242, 184, 75, 0.3), transparent);
}

.sol-time-item {
  display: flex;
  justify-content: flex-end;
  padding-right: 50%;
  position: relative;
  margin-bottom: 60px;
}

.sol-time-item:nth-child(even) {
  justify-content: flex-start;
  padding-right: 0;
  padding-left: 50%;
}

.sol-time-dot {
  position: absolute;
  top: 30px; right: -10px;
  width: 20px; height: 20px;
  background: var(--ca-vinho);
  border: 4px solid var(--ca-dourado);
  border-radius: 50%;
  box-shadow: 0 0 15px rgba(242, 184, 75, 0.6);
  z-index: 2;
  transition: all 0.3s ease;
}

.sol-time-item:hover .sol-time-dot {
  background: var(--ca-dourado);
  transform: scale(1.2);
}

.sol-time-item:nth-child(even) .sol-time-dot {
  left: -10px; right: auto;
}

.sol-time-content {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.01));
  backdrop-filter: blur(15px);
  border: 1px solid var(--ca-vidro-border);
  border-radius: var(--ca-border-radius);
  padding: 40px;
  width: calc(100% - 50px);
  transition: all 0.4s ease;
}

.sol-time-item:hover .sol-time-content {
  transform: translateY(-8px);
  border-color: rgba(242, 184, 75, 0.4);
  box-shadow: 0 20px 40px rgba(0,0,0,0.3);
}

.sol-time-title {
  color: var(--ca-dourado);
  font-size: 1.4rem;
  font-weight: 800;
  margin-bottom: 15px;
}

/* 5. Cards O que está incluso */
.sol-included-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 25px;
  margin-top: 60px;
}

.sol-included-card {
  display: flex;
  align-items: center;
  gap: 20px;
  background: rgba(0,0,0,0.25);
  padding: 25px;
  border-radius: 20px;
  border-left: 5px solid var(--ca-dourado);
  transition: all 0.3s ease;
}

.sol-included-card:hover {
  background: rgba(0,0,0,0.4);
  transform: translateX(10px);
}

.sol-included-icon {
  color: #4CAF50; /* Green check */
  filter: drop-shadow(0 0 5px rgba(76, 175, 80, 0.5));
}

/* 6. Galeria Institucional */
.sol-gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-auto-rows: 280px;
  gap: 25px;
  margin-top: 60px;
}

.sol-gallery-item {
  border-radius: var(--ca-border-radius);
  overflow: hidden;
  position: relative;
  box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}

.sol-gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s cubic-bezier(0.25, 1, 0.5, 1);
}

.sol-gallery-item:hover img {
  transform: scale(1.08);
}

.sol-gallery-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(26,5,10,0.95) 0%, rgba(26,5,10,0.4) 50%, transparent 100%);
  display: flex;
  align-items: flex-end;
  padding: 30px;
  opacity: 0;
  transition: opacity 0.4s ease;
}

.sol-gallery-item:hover .sol-gallery-overlay {
  opacity: 1;
}

.sol-gallery-overlay h4 {
  color: var(--ca-dourado);
  font-size: 1.4rem;
  font-weight: 800;
  margin: 0;
  transform: translateY(20px);
  transition: transform 0.4s ease;
}

.sol-gallery-item:hover .sol-gallery-overlay h4 {
  transform: translateY(0);
}

/* 7. CTA Final */
.sol-cta {
  background: linear-gradient(135deg, var(--ca-vinho) 0%, rgba(26, 5, 10, 0.8) 100%), url('../images/backgrounds/background-768x543-criaacao-entretenimento.png') center/cover;
  padding: 120px 20px;
  text-align: center;
  border-top: 1px solid rgba(255,255,255,0.05);
  position: relative;
}

.sol-cta::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(26, 5, 10, 0.7);
  backdrop-filter: blur(5px);
}

.sol-cta-box {
  max-width: 900px;
  margin: 0 auto;
  background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
  backdrop-filter: blur(20px);
  padding: 80px 50px;
  border-radius: 30px;
  border: 1px solid rgba(242, 184, 75, 0.3);
  position: relative;
  z-index: 2;
  box-shadow: 0 30px 60px rgba(0,0,0,0.4);
}

.sol-cta-box h2 {
  font-size: clamp(2rem, 4vw, 3rem);
}

/* Responsive */
@media (max-width: 768px) {
  .sol-section { padding: 80px 15px; }
  .sol-timeline::before { left: 24px; }
  .sol-time-item, .sol-time-item:nth-child(even) {
    justify-content: flex-start;
    padding-right: 0;
    padding-left: 60px;
    margin-bottom: 40px;
  }
  .sol-time-dot, .sol-time-item:nth-child(even) .sol-time-dot {
    left: 14px; right: auto;
  }
  .sol-time-content { width: 100%; padding: 25px; }
  .sol-title-eyebrow { justify-content: center; text-align: center; }
  .sol-hero, .sol-title-main, .sol-text-main { text-align: center; }
  .sol-cta-box { padding: 50px 20px; }
  .sol-grid { gap: 20px; }
  .sol-card { padding: 35px 25px; }
}
"@
[System.IO.File]::WriteAllText($cssPath, $cssContent, [System.Text.Encoding]::UTF8)

$htmlPath = "d:\Sites\Criação entretenimento\referencia\criaacao.com\solucoes.html"
$content = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)

$newMain = @"
    <!-- MAIN CONTENT: SOLUCOES -->
    <main id="solucoes-main">
      
      <!-- 1. HERO INSTITUCIONAL -->
      <section class="sol-section sol-hero">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Alto Padrão em Entretenimento</div>
          <h1 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O portfólio completo para<br>um <span>Natal memorável</span></h1>
          <p class="sol-text-main sol-reveal slide-in-up sol-stagger-2">Do planejamento à excelência na execução, entregamos experiências modulares, encantadoras e perfeitamente adequadas à magnitude do seu evento.</p>
          <a href="https://wa.me/5585988601400?text=Ol%C3%A1!%20Gostaria%20de%20saber%20mais%20sobre%20as%20Solu%C3%A7%C3%B5es%20Natalinas." target="_blank" class="sol-btn-primary sol-reveal slide-in-up sol-stagger-3">
            Falar com um Especialista
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
        </div>
      </section>

      <!-- 2. GRID DE SOLUÇÕES PRINCIPAIS -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Nossas Soluções</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O espetáculo que seu público <span>merece</span></h2>
          
          <div class="sol-grid">
            <div class="sol-card sol-reveal slide-in-up sol-stagger-1">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 12 20 22 4 22 4 12"></polyline><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path></svg>
              </div>
              <h3 class="sol-card-title">Papai e Mamãe Noel</h3>
              <p class="sol-card-text">Elenco de elite, com figurinos impecáveis e treinamento humanizado, preparado para encantar e gerar conexão genuína com famílias exigentes.</p>
            </div>
            
            <div class="sol-card sol-reveal slide-in-up sol-stagger-2">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg>
              </div>
              <h3 class="sol-card-title">Duendes e Ajudantes</h3>
              <p class="sol-card-text">Atores performáticos para criar narrativas lúdicas, organizar filas de maneira divertida e manter a magia viva nos corredores do seu espaço.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-3">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
              </div>
              <h3 class="sol-card-title">Espaço Fotográfico</h3>
              <p class="sol-card-text">Operação comercial completa de fotografia profissional. Impressão imediata, equipe treinada em vendas e cenografia integrada ao trono oficial.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-4">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
              </div>
              <h3 class="sol-card-title">Ativação Plataforma 360°</h3>
              <p class="sol-card-text">Uma experiência moderna e engajadora. Geração de vídeos curtos personalizados instantâneos que impulsionam o alcance orgânico nas redes sociais.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-5">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              </div>
              <h3 class="sol-card-title">Mimos e Brindes Personalizados</h3>
              <p class="sol-card-text">Desenvolvimento e curadoria de lembranças especiais, biscoitos artesanais e mimos que fortalecem o relacionamento com seus visitantes.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-6">
              <div class="sol-card-icon">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              </div>
              <h3 class="sol-card-title">Paradas e Cortejos Natalinos</h3>
              <p class="sol-card-text">Apresentações itinerantes monumentais com músicos, acrobatas e bailarinos, transformando os corredores em verdadeiros palcos móveis.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. SOLUÇÕES POR SEGMENTO -->
      <section class="sol-section">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Atendimento Segmentado</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">A expertise exata para <span>cada setor</span></h2>
          
          <div class="sol-segments-grid sol-reveal slide-in-up sol-stagger-2">
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Shopping Centers</h4>
              <p class="sol-segment-desc">Operações robustas para grandes inaugurações, gestão de fluxo e temporada completa de fim de ano.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Eventos Corporativos</h4>
              <p class="sol-segment-desc">Ações de endomarketing e celebrações empresariais para engajar equipes e familiares.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Prefeituras</h4>
              <p class="sol-segment-desc">Megaproduções em praças públicas, paradas culturais e celebrações que marcam a cidade.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Instituições de Ensino</h4>
              <p class="sol-segment-desc">Chegadas lúdicas, interação educativa e entrega de presentes que marcam a infância.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Hospitais</h4>
              <p class="sol-segment-desc">Visitas humanizadas com profissionais sensíveis, levando esperança e acolhimento aos pacientes.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 4. TIMELINE COMO FUNCIONA -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">O Método CriaAção</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O passo a passo para o <span>sucesso</span></h2>
          
          <div class="sol-timeline">
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-1">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">1. Diagnóstico e Planejamento</h3>
                <p class="sol-text-main" style="font-size:1.05rem; margin:0;">Analisamos a topografia do seu espaço, o perfil demográfico do público e orquestramos as melhores soluções para maximizar o impacto da sua campanha.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-2">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">2. Curadoria e Treinamento</h3>
                <p class="sol-text-main" style="font-size:1.05rem; margin:0;">Realizamos seletivas criteriosas e submetemos a equipe a workshops imersivos de atuação, postura e atendimento encantador ao cliente.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-3">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">3. Estética e Produção Visual</h3>
                <p class="sol-text-main" style="font-size:1.05rem; margin:0;">Nosso acervo próprio de figurinos de alto padrão é preparado, higienizado e ajustado sob medida, garantindo fotografias e vídeos deslumbrantes.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-4">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">4. Gestão e Operação Total</h3>
                <p class="sol-text-main" style="font-size:1.05rem; margin:0;">Supervisionamos toda a operação in loco: escalas, plantões, substituições de emergência e relatórios de resultados, para que você não precise se preocupar com nada.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 5. CARDS O QUE ESTA INCLUSO -->
      <section class="sol-section">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Gestão Transparente</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O que está garantido <span>no seu pacote</span></h2>
          
          <div class="sol-included-grid sol-reveal slide-in-up sol-stagger-2">
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Cachês e tributos da equipe atuante</span>
            </div>
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Uso e manutenção de figurinos premium</span>
            </div>
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Gerenciamento operacional e supervisão in loco</span>
            </div>
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Seguro de responsabilidade e acidentes pessoais</span>
            </div>
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Logística, traslados e alimentação da equipe</span>
            </div>
            <div class="sol-included-card">
              <svg xmlns="http://www.w3.org/2000/svg" class="sol-included-icon" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              <span style="color:#fff; font-weight: 600; font-size:1.1rem;">Plantão ativo e backup de personagens</span>
            </div>
          </div>
        </div>
      </section>

      <!-- 6. GALERIA INSTITUCIONAL -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Nosso Portfólio de Soluções</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O resultado na <span>prática</span></h2>
          
          <div class="sol-gallery sol-reveal slide-in-up sol-stagger-2">
            <div class="sol-gallery-item">
              <img src="assets/images/gallery/papai-noel-com-crianca-no-trono-criaacao-entretenimento.png" alt="Papai Noel no Trono">
              <div class="sol-gallery-overlay"><h4 style="color:var(--ca-dourado); margin:0;">Papai Noel Clássico</h4></div>
            </div>
            <div class="sol-gallery-item" style="grid-row: span 2;">
              <img src="assets/images/gallery/Duendes-e1720275042996-criaacao-entretenimento.png" alt="Apresentação de Duendes">
              <div class="sol-gallery-overlay"><h4 style="color:var(--ca-dourado); margin:0;">Atores Performáticos</h4></div>
            </div>
            <div class="sol-gallery-item">
              <img src="assets/images/gallery/Plataforma-360o-e1720275137989-criaacao-entretenimento.png" alt="Plataforma 360 graus">
              <div class="sol-gallery-overlay"><h4 style="color:var(--ca-dourado); margin:0;">Plataforma 360°</h4></div>
            </div>
            <div class="sol-gallery-item">
              <img src="assets/images/gallery/Brindes-e1720275106833-criaacao-entretenimento.png" alt="Brindes Personalizados">
              <div class="sol-gallery-overlay"><h4 style="color:var(--ca-dourado); margin:0;">Mimos e Brindes</h4></div>
            </div>
            <div class="sol-gallery-item">
              <img src="assets/images/gallery/Acoes-Tematicas-e1720275059494-criaacao-entretenimento.png" alt="Ações Temáticas">
              <div class="sol-gallery-overlay"><h4 style="color:var(--ca-dourado); margin:0;">Personagens Temáticos</h4></div>
            </div>
          </div>
        </div>
      </section>

      <!-- 7. CTA FINAL -->
      <section class="sol-cta">
        <div class="sol-container">
          <div class="sol-cta-box sol-reveal slide-in-up">
            <h2 class="sol-title-main" style="margin-bottom: 25px;">Pronto para criar o <span>Natal dos sonhos?</span></h2>
            <p class="sol-text-main" style="margin: 0 auto 40px;">Fale agora com nossa equipe corporativa para desenharmos juntos um plano de ação impecável, dimensionado sob medida para o seu investimento.</p>
            <a href="https://wa.me/5585988601400?text=Ol%C3%A1!%20Gostaria%20de%20montar%20um%20pacote%20de%20Solu%C3%A7%C3%B5es%20Natalinas%20Premium." target="_blank" class="sol-btn-primary">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg> Solicitar Proposta Comercial
            </a>
          </div>
        </div>
      </section>

      <!-- JS Animação Reveal -->
      <script>
        document.addEventListener("DOMContentLoaded", function() {
          const reveals = document.querySelectorAll(".sol-reveal");
          const revealOnScroll = () => {
            const windowHeight = window.innerHeight;
            const elementVisible = 100;
            reveals.forEach((reveal) => {
              const elementTop = reveal.getBoundingClientRect().top;
              if (elementTop < windowHeight - elementVisible) {
                reveal.classList.add("sol-visible");
              }
            });
          };
          window.addEventListener("scroll", revealOnScroll);
          revealOnScroll();
        });
      </script>
    </main>
"@

$content = $content -replace '(?s)<!-- MAIN CONTENT: SOLUCOES -->\s*<main id="solucoes-main">.*?</main>', $newMain
[System.IO.File]::WriteAllText($htmlPath, $content, [System.Text.Encoding]::UTF8)

Write-Host "Script completed."
