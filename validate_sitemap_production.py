import xml.etree.ElementTree as ET
import urllib.request
import urllib.error

SITEMAP_PATH = 'sitemap.xml'
NS = {
    'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
    'image': 'http://www.google.com/schemas/sitemap-image/1.1'
}

def validate_url(url):
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req, timeout=10)
        # Check HTTP 200
        if response.status != 200:
            return f"ERRO: Status {response.status}"
            
        # Check redirect (urllib follows by default, so if final url != original url, it's a redirect)
        if response.geturl() != url:
            return f"AVISO: Redirecionamento detectado para {response.geturl()}"
            
        # Check Content-Type for images
        content_type = response.headers.get('Content-Type', '')
        if url.endswith('.webp') and 'image' not in content_type:
             return f"AVISO: Content-Type suspeito: {content_type}"
             
        return "OK"
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return "ERRO: Bloqueado (403 Forbidden)"
        return f"ERRO HTTP: {e.code}"
    except urllib.error.URLError as e:
        return f"ERRO URL: Falha ao alcançar o servidor ({e.reason})"
    except Exception as e:
        return f"ERRO DESCONHECIDO: {str(e)}"

def run_validation():
    try:
        tree = ET.parse(SITEMAP_PATH)
    except FileNotFoundError:
        print("sitemap.xml não encontrado localmente.")
        return
        
    root = tree.getroot()
    
    urls_to_check = []
    
    for url_node in root.findall('sm:url', NS):
        loc = url_node.find('sm:loc', NS)
        if loc is not None:
            urls_to_check.append(loc.text)
            
        for img_node in url_node.findall('image:image', NS):
            img_loc = img_node.find('image:loc', NS)
            if img_loc is not None:
                urls_to_check.append(img_loc.text)
                
    print(f"Iniciando validação de {len(urls_to_check)} URLs (páginas + imagens)...")
    
    issues = 0
    for url in urls_to_check:
        if not url.startswith('https://'):
            print(f"[FALHA] URL não é HTTPS: {url}")
            issues += 1
            continue
            
        status = validate_url(url)
        if status != "OK":
            print(f"[{status}] {url}")
            issues += 1
            
    print("-" * 40)
    if issues == 0:
        print("Validação finalizada. Nenhuma anomalia detectada!")
    else:
        print(f"Validação finalizada com {issues} alertas/erros encontrados.")
        print("IMPORTANTE: O script reporta falhas, mas não modifica o XML nem os arquivos remotos.")

if __name__ == '__main__':
    run_validation()
