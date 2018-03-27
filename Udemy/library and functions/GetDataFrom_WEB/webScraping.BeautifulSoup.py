'''
Uso conjunto do request com o BeautifulSoup
- o request obtem o conteudo da pagina
- o 
'''

import requests
from bs4 import BeautifulSoup

url = "http://www.epicurious.com/search/Tofu Chili"
response = requests.get(url)

#lxml é um tipo de parser, mais rapido
#html5lib é outro tipo de parser, porem mais lento
results_page = BeautifulSoup(response.content,'lxml') 
#print(results_page.prettify())

#encontra na pagina todos os tags que tem a
all_a_tags = results_page.find_all('a')
print(type(all_a_tags)) 
#print(all_a_tags)

#---------------------------------------------------------
# - o objeto bs4.element.ResultSet nao contem o metodo find.
#   apenas retorna todos os resultados de uma pesquisa.
#
# - por outro lado, quando se usa o metodo find... que encontra o primeiro elemento
#   retorna um tipo bs4.element.Tag, que contem sim o metodo find, ou seja,
#   permite que se faca uma nova busca dentro do elemento, que neste exemplo, busca-se
#   um elemento filho da primeira div do tipo 'a' (bs4.element.Tag)
#---------------------------------------------------------

first_div_tag = results_page.find('div')
print(type(first_div_tag)) 
#print(all_a_tags)

print(50 * '-', ' Encontrar uma TAG')
print(first_div_tag.find('a'))


#---------------------------------------------------------
# - pode-se utilizan no metodos find e find_all a busca por SELETORES
#   ex1: results_page.find_all('article',class_="recipe-content-card")
#   ex2: results_page.find('article',{'class':'recipe-content-card'})
#   ex3: results_page.find('a',{'data-reactid':'99'})
#
#   No exemplo 1, o class aparece seguido do underscore pois 'class é um nome resevado do Python e 
#   tambem, para nao dar erro no interpretados, existe o underscore
#
#   No exemplo 2, vc passa um dicionario, podendo ter n elementos de busca
#
#   No exemplo 3, foi buscado uma tag a com um atributo particular
#---------------------------------------------------------

#print(results_page.find_all('article',class_="recipe-content-card"))


print(results_page.find('a',{'data-reactid':'99'})) 
print('PEGANDO SOMENTE A URL DA TAG ==> ', results_page.find('a',{'data-reactid':'99'}).get('href'))
print(50 * '-')

#este comando obtem apenas o texto dentro da tag selecionada
print(results_page.find('article',class_="recipe-content-card").get_text()) 
print(50 * '-')




