import re

filepath = r"d:\Sites\Criação entretenimento\referencia\criaacao.com\solucoes.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Replace <title>
content = re.sub(r'<title>.*?</title>', '<title>CriaAção Entretenimento | Soluções Natalinas Exclusivas</title>', content)

# Replace the CSS link
content = content.replace('href="assets/css/quem-somos.css"', 'href="assets/css/solucoes.css"')

# Replace main content block
new_main = """    <!-- MAIN CONTENT: SOLUCOES -->
    <main id="solucoes-main">
      
      <!-- 1. HERO INSTITUCIONAL -->
      <section class="sol-section sol-hero">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Excelência em Entretenimento</div>
          <h1 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">Soluções completas para<br>um <span>Natal inesquecível</span></h1>
          <p class="sol-text-main sol-reveal slide-in-up sol-stagger-2">Do planejamento à operação, oferecemos experiências modulares e integradas que se adaptam perfeitamente à necessidade do seu espaço.</p>
          <a href="https://wa.me/5585988601400?text=Ol%C3%A1!%20Gostaria%20de%20saber%20mais%20sobre%20as%20Solu%C3%A7%C3%B5es%20Natalinas." target="_blank" class="sol-btn-primary sol-reveal slide-in-up sol-stagger-3">
            Falar com Especialista
          </a>
        </div>
      </section>

      <!-- 2. GRID DE SOLUÇÕES PRINCIPAIS -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Nossas Soluções</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">Tudo que seu evento <span>precisa</span></h2>
          
          <div class="sol-grid">
            <div class="sol-card sol-reveal slide-in-up sol-stagger-1">
              <div class="sol-card-icon"><i class="fas fa-gift fa-2x"></i></div>
              <h3 class="sol-card-title">Papai Noel e Mamãe Noel</h3>
              <p class="sol-card-text">Profissionais rigorosamente selecionados, treinados e caracterizados com figurinos de alto padrão para encantar toda a família.</p>
            </div>
            
            <div class="sol-card sol-reveal slide-in-up sol-stagger-2">
              <div class="sol-card-icon"><i class="fas fa-magic fa-2x"></i></div>
              <h3 class="sol-card-title">Duendes e Personagens</h3>
              <p class="sol-card-text">Atores performáticos para paradas natalinas, recepção de clientes e interação imersiva pelo shopping.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-3">
              <div class="sol-card-icon"><i class="fas fa-camera fa-2x"></i></div>
              <h3 class="sol-card-title">Espaço Fotográfico</h3>
              <p class="sol-card-text">Operação completa de fotografia com impressão na hora, sistema de vendas e cenografia integrada ao trono.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-4">
              <div class="sol-card-icon"><i class="fas fa-sync-alt fa-2x"></i></div>
              <h3 class="sol-card-title">Plataforma 360°</h3>
              <p class="sol-card-text">Ativação moderna e atrativa que gera vídeos curtos personalizados para as redes sociais dos visitantes.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-5">
              <div class="sol-card-icon"><i class="fas fa-box-open fa-2x"></i></div>
              <h3 class="sol-card-title">Brindes e Mimos</h3>
              <p class="sol-card-text">Personalização de presentes, distribuição de doces e lembranças especiais durante as ações de relacionamento.</p>
            </div>

            <div class="sol-card sol-reveal slide-in-up sol-stagger-6">
              <div class="sol-card-icon"><i class="fas fa-star fa-2x"></i></div>
              <h3 class="sol-card-title">Paradas Natalinas</h3>
              <p class="sol-card-text">Apresentações itinerantes com músicos, acrobatas e personagens que transformam os corredores do shopping.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 3. SOLUÇÕES POR SEGMENTO -->
      <section class="sol-section">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Atendimento Especializado</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">Soluções para <span>cada segmento</span></h2>
          
          <div class="sol-segments-grid sol-reveal slide-in-up sol-stagger-2">
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Shopping Centers</h4>
              <p class="sol-segment-desc">Operações completas de temporada e eventos de chegada.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Empresas</h4>
              <p class="sol-segment-desc">Festas de confraternização e ações de endomarketing.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Prefeituras</h4>
              <p class="sol-segment-desc">Eventos abertos em praças e programações culturais.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Escolas</h4>
              <p class="sol-segment-desc">Chegada do Papai Noel lúdica e entrega de presentes.</p>
            </div>
            <div class="sol-segment-item">
              <h4 class="sol-segment-title">Hospitais</h4>
              <p class="sol-segment-desc">Visitas humanizadas para levar esperança e alegria.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 4. TIMELINE COMO FUNCIONA -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Processo de Trabalho</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">Como <span>funciona</span></h2>
          
          <div class="sol-timeline">
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-1">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">1. Diagnóstico e Planejamento</h3>
                <p class="sol-text-main" style="font-size:1rem; margin:0;">Analisamos o espaço, o perfil do público e definimos juntos os serviços que melhor atendem ao escopo da sua campanha.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-2">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">2. Seleção e Treinamento</h3>
                <p class="sol-text-main" style="font-size:1rem; margin:0;">Escalamos a equipe ideal e realizamos nossos workshops exclusivos de atuação, postura e atendimento encantador.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-3">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">3. Produção e Figurinos</h3>
                <p class="sol-text-main" style="font-size:1rem; margin:0;">Separamos, higienizamos e ajustamos todos os trajes de alto padrão, garantindo estética impecável para as fotos.</p>
              </div>
            </div>
            <div class="sol-time-item sol-reveal slide-in-up sol-stagger-4">
              <div class="sol-time-dot"></div>
              <div class="sol-time-content">
                <h3 class="sol-time-title">4. Operação Completa</h3>
                <p class="sol-text-main" style="font-size:1rem; margin:0;">Gerenciamos escalas, substituições, pausas e o dia a dia da ação, entregando relatórios de desempenho.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 5. CARDS O QUE ESTA INCLUSO -->
      <section class="sol-section">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Gestão Transparente</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">O que está <span>incluso no pacote</span></h2>
          
          <div class="sol-included-grid sol-reveal slide-in-up sol-stagger-2">
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Cachês da equipe atuante</span></div>
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Aluguel e manutenção de figurinos</span></div>
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Gerente operacional dedicado</span></div>
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Seguro de acidentes pessoais</span></div>
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Logística e deslocamento</span></div>
            <div class="sol-included-card"><i class="fas fa-check-circle sol-included-icon"></i> <span style="color:#fff;">Plantão de backup de personagens</span></div>
          </div>
        </div>
      </section>

      <!-- 6. GALERIA INSTITUCIONAL -->
      <section class="sol-section sol-section-alt">
        <div class="sol-container">
          <div class="sol-title-eyebrow sol-reveal slide-in-up">Nosso Portfólio de Serviços</div>
          <h2 class="sol-title-main sol-reveal slide-in-up sol-stagger-1">Confira na <span>prática</span></h2>
          
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
            <h2 class="sol-title-main" style="margin-bottom: 20px;">Vamos criar o <span>Natal perfeito</span> para o seu público?</h2>
            <p class="sol-text-main" style="margin: 0 auto 30px;">Converse com nossa equipe para montar um pacote de soluções sob medida para o seu orçamento e tamanho de evento.</p>
            <a href="https://wa.me/5585988601400?text=Ol%C3%A1!%20Gostaria%20de%20montar%20um%20pacote%20de%20Solu%C3%A7%C3%B5es%20Natalinas." target="_blank" class="sol-btn-primary">
              <i class="fab fa-whatsapp" style="font-size:1.2rem;"></i> Solicitar Proposta
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
    </main>"""

# Using regex to replace everything from <main id="quem-somos-main"> to </main>
import re
new_content = re.sub(r'<!-- MAIN CONTENT: QUEM SOMOS -->\s*<main id="quem-somos-main">.*?</main>', new_main, content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Replacement done.")
