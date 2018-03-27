'''
Este exemplo, tenta mostrar que algumas vezes é necessario fazer um login na pagina para que seja
possivel obter dados. 

Este é um exemplo de um login no Wikipedia.

Obs.: O professor mostrou que a pagina gera um token que fica em um hidden field, que eh um tipo de 
      protecao do site, para garantir que a pagina que eta fazendo o submit seja de uma pagina gerada
      pelo proprio sistema
       
'''
import requests
from bs4 import BeautifulSoup

# neste exemplo, o professor arrumou uma maneira para nao mostrar sua senha e login no wikipedia
username = ''
password = ''

#with open('wikidata.txt') as f:
#    contents = f.read().split('\n')
#    username = contents[0]
#    password = contents[1]


payload = {
    'wpName': username,
    'wpPassword': password,
    'wploginattempt': 'Log in',
    'wpEditToken': "+\\",
    'title': "Special:UserLogin",
    'authAction': "login",
    'force': "",
    'wpForceHttps': "1",
    'wpFromhttp': "1",
    #'wpLoginToken': ‘', #We need to read this from the page
    }

#forma como utilizou para oter o token da pagina
def get_login_token(response):
    soup = BeautifulSoup(response.text, 'lxml')
    token = soup.find('input',{'name':"wpLoginToken"}).get('value')
    return token


#abre uma sessao de login
with requests.session() as s:
    response = s.get('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Main+Page')

    #reescreve o valor do wpLoginToken
    payload['wpLoginToken'] = get_login_token(response)

    #Send the login request
    response_post = s.post('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&action=submitlogin&type=login',
                           data=payload)

    #Get another page and check if we’re still logged in
    response = s.get('https://en.wikipedia.org/wiki/Special:Watchlist')
    data = BeautifulSoup(response.content,'lxml')
    print(data.find('div',class_='mw-changeslist').get_text())



    