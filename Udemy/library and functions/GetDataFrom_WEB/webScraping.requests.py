'''
Exemplo usando a biblioteca requests
'''
import requests


url = "https://en.wikipedia.org/wiki/main_page"

#The rest of your code should go below this line
r = requests.get(url)
print(r.status_code)
wikitext = r.content.decode('utf-8')

print(wikitext.find('Did you know'))

print(wikitext)
