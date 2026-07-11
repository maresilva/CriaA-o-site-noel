$ErrorActionPreference = "Stop"

$html = Get-Content -Path "index.html" -Raw -Encoding UTF8

$newSection = @"
    <section class="ca-segmentos-section">
      <div class="ca-segmentos-container">
        <div class="ca-segmentos-header reveal ca-animate-fadeup is-visible visible">
          <div class="ca-segmentos-eyebrow">ONDE TAMBÉM ATUAMOS</div>
          <h2 class="ca-segmentos-title">Muito além dos <span>Shopping Centers.</span></h2>
          <p class="ca-segmentos-text">Criamos experiências natalinas personalizadas para diferentes públicos e ambientes, levando o mesmo padrão de excelência, organização e encantamento para cada projeto.<br><br>Do planejamento à execução, adaptamos nossas soluções para atender instituições públicas, empresas privadas e projetos sociais em todo o Brasil.</p>
        </div>

        <div class="ca-segmentos-grid">
          <!-- Card 01: Shopping Centers -->
          <a href="/solucoes" class="ca-segmento-card ca-card-shopping reveal ca-animate-fadeup visible is-visible" style="transition-delay: 0.1s;">
            <img src="assets/images/gallery/shopping_natal_1783720410936.png" class="ca-segmento-bg" alt="Shopping Centers" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Shopping Centers</h3>
                <p class="ca-segmento-desc">Projetos completos para campanhas natalinas, chegada do Papai Noel, espaços fotográficos, ativações e operação integral.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>

          <!-- Card 02: Prefeituras -->
          <a href="/solucoes" class="ca-segmento-card ca-card-prefeituras reveal ca-animate-fadeup visible is-visible" style="transition-delay: 0.2s;">
            <img src="assets/images/gallery/prefeitura_natal_1783720420891.png" class="ca-segmento-bg" alt="Prefeituras" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"></path><path d="M5 21V7l8-4v18"></path><path d="M19 21V11l-6-3"></path><path d="M9 11v-2"></path><path d="M9 15v-2"></path><path d="M9 19v-2"></path></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Prefeituras</h3>
                <p class="ca-segmento-desc">Natal em praças, parques, bairros, eventos públicos e ações culturais para toda a comunidade.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>

          <!-- Card 03: Escolas -->
          <a href="/solucoes" class="ca-segmento-card ca-card-escolas reveal ca-animate-fadeup visible is-visible" style="transition-delay: 0.3s;">
            <img src="assets/images/gallery/escola_natal_1783720429899.png" class="ca-segmento-bg" alt="Escolas" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"></path></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Escolas</h3>
                <p class="ca-segmento-desc">Visitas especiais do Papai Noel, personagens, apresentações e atividades recreativas.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>

          <!-- Card 04: Empresas -->
          <a href="/solucoes" class="ca-segmento-card ca-card-empresas reveal ca-animate-fadeup visible is-visible" style="transition-delay: 0.4s;">
            <img src="assets/images/gallery/empresa_natal_1783720439041.png" class="ca-segmento-bg" alt="Empresas" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01"></path><path d="M16 6h.01"></path><path d="M12 6h.01"></path><path d="M12 10h.01"></path><path d="M12 14h.01"></path><path d="M16 10h.01"></path><path d="M16 14h.01"></path><path d="M8 10h.01"></path><path d="M8 14h.01"></path></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Empresas</h3>
                <p class="ca-segmento-desc">Eventos corporativos, confraternizações, campanhas promocionais e ações para colaboradores.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>

          <!-- Card 05: Residências e Buffets -->
          <a href="/solucoes" class="ca-segmento-card ca-card-residencias reveal ca-animate-fadeup is-visible visible" style="transition-delay: 0.5s;">
            <img src="assets/images/gallery/casa_natal_1783720448832.png" class="ca-segmento-bg" alt="Residências e Buffets" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Residências e Buffets</h3>
                <p class="ca-segmento-desc">Experiências exclusivas, visitas do Papai Noel e eventos familiares personalizados.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>

          <!-- Card 06: Projetos Sociais -->
          <a href="/solucoes" class="ca-segmento-card ca-card-sociais reveal ca-animate-fadeup is-visible visible" style="transition-delay: 0.6s;">
            <img src="assets/images/gallery/social_natal_1783720457458.png" class="ca-segmento-bg" alt="Projetos Sociais" loading="lazy">
            <div class="ca-segmento-overlay"></div>
            <div class="ca-segmento-content">
              <div class="ca-segmento-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
              </div>
              <div>
                <h3 class="ca-segmento-title">Projetos Sociais</h3>
                <p class="ca-segmento-desc">Ações humanizadas em hospitais, creches, asilos e instituições beneficentes, levando o espírito do Natal a quem mais precisa.</p>
                <div class="ca-segmento-link">Conhecer soluções →</div>
              </div>
            </div>
          </a>
        </div>

        <div class="ca-segmentos-cta reveal ca-animate-fadeup" style="transition-delay: 0.7s;">
          <a href="/solucoes" class="ca-segmentos-btn">Conheça todas as soluções →</a>
        </div>
      </div>
    </section>
"@

# I need to insert it right before `<section id="diferenciais"`
# First let me double check if I didn't somehow inject it twice. 
# We'll use regex to remove any existing `<section class="ca-segmentos-section">...` 
# Note: since the string can be multi-line and huge, we might use a robust replacement:
$html = $html -replace '(?is)<section class="ca-segmentos-section">.*?</section>', ''

# Then we insert it before <section id="diferenciais"
$html = $html -replace '(?i)<section id="diferenciais"', "$newSection`n`n      <section id=`"diferenciais`""

Set-Content -Path "index.html" -Value $html -Encoding UTF8
Write-Output "Section inserted properly!"
