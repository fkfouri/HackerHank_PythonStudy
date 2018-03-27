'''
Basicamente ha tres bibliotecas
- requests: http request e response
- Beautiful Soup: utiliza a tag estruturada html para parsear o conteudo
- Selenium: emula o browser.  Util quando a pagina tem scripts. 
    Originalmente desenvolvido para testar o servidor
'''
import requests
from bs4 import BeautifulSoup
url = 'http://www.uol.comm.br'

try:
    requests.get(url)
    print('ok')
except:
    print('nok')