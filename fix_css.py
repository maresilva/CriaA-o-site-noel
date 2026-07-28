import re
with open('contato.html', 'r', encoding='utf-8') as f:
    contato_html = f.read()

correct_style = """      <style id="ca-contato-style">
        .ca-contato-section {
          position: relative;
          padding: 80px 20px 140px 20px;
          background: linear-gradient(to bottom, rgba(26, 3, 4, 0.95) 0%, rgba(26, 3, 4, 0.75) 50%, rgba(10, 1, 2, 0.95) 100%), url('assets/images/backgrounds/background-segunda-sessão-shopping-decorado-natal-criaacao-entretenimento.jpg') center/cover fixed;
          overflow: hidden;
          box-sizing: border-box !important;
          width: 100%;
        }

        .ca-contato-container {
          width: 100%;
          max-width: 1200px;
          margin: 0 auto;
          position: relative;
          z-index: 10;
          display: grid;
          grid-template-columns: 1fr 1.2fr;
          gap: 60px;
          align-items: flex-start;
          box-sizing: border-box !important;
        }

        .ca-contato-info-grid {
          display: flex;
          flex-direction: column;
          gap: 20px;
          width: 100%;
          min-width: 0;
        }

        .ca-card {
          background: rgba(255, 255, 255, 0.03) !important;
          border: 1px solid rgba(242, 184, 75, 0.15) !important;
          backdrop-filter: blur(10px) !important;
          border-radius: 20px !important;
          padding: 30px !important;
          display: flex !important;
          align-items: flex-start !important;
          gap: 20px !important;
          transition: all 0.4s ease !important;
          box-sizing: border-box !important;
          width: 100% !important;
          min-width: 0 !important;
          word-break: break-word !important;
        }

        .ca-card:hover {
          background: rgba(255, 255, 255, 0.06) !important;
          border-color: rgba(242, 184, 75, 0.4) !important;
          transform: translateX(10px) !important;
          box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        }

        .ca-card-icon {
          width: 54px !important;
          height: 54px !important;
          background: rgba(242, 184, 75, 0.1) !important;
          border-radius: 50% !important;
          display: flex !important;
          align-items: center !important;
          justify-content: center !important;
          color: #F2B84B !important;
          flex-shrink: 0 !important;
          margin: 0 !important;
        }

        .ca-card-content h3 {
          color: #FFF !important;
          font-size: 20px !important;
          font-weight: 700 !important;
          margin: 0 0 6px 0 !important;
          line-height: 1.3 !important;
        }

        .ca-card-content p {
          color: rgba(255, 255, 255, 0.8) !important;
          font-size: 16px !important;
          line-height: 1.5 !important;
          margin: 0 !important;
        }

        .ca-contato-form-wrapper {
          background: rgba(10, 1, 2, 0.6) !important;
          border: 1px solid rgba(255, 255, 255, 0.08) !important;
          backdrop-filter: blur(20px) !important;
          border-radius: 24px !important;
          padding: 40px !important;
          box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4) !important;
          width: 100% !important;
          min-width: 0 !important;
          box-sizing: border-box !important;
        }

        .ca-form-title {"""

pattern = re.compile(r'      <style id="ca-contato-style">.*?(?=        \.ca-form-title {)', re.DOTALL)
new_html = pattern.sub(correct_style, contato_html)

with open('contato.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print('Fixed CSS successfully.')
