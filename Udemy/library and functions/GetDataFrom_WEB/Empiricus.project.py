'''
Projeto para obter descricao, ingredientes e modo de preparo de dois tipos de pratos no 
site Empiricus.com
'''


def get_recipes(keywords):
    #chama internamente as bibliotecas necessarias
    import requests
    from bs4 import BeautifulSoup

    #declaracao de uma lista vazia, para ser inserido resultados conforme a pesquisa for retornando valores
    recipe_list = list()

    url = "http://www.epicurious.com/search/" + keywords
    response = requests.get(url)

    #verifica se ha retorno do servidor
    if not response.status_code == 200:
        return None
    try:
        #aplica o parser
        results_page = BeautifulSoup(response.content,'lxml')

        #busca por articles, que eh como o site esta estruturado
        recipes = results_page.find_all('article',class_="article-content-card") #recipe-content-card

        #laco para obeter um recipe de cada reciples
        for recipe in recipes:
            recipe_link = "http://www.epicurious.com" + recipe.find('a').get('href')
            recipe_name = recipe.find('a').get_text()
            try:
                recipe_description = recipe.find('p',class_='dek').get_text()
            except:
                recipe_description = ''

            #inclui na lista o nome, o link e a descricao do "Recipe"
            recipe_list.append((recipe_name, recipe_link, recipe_description))
        return recipe_list
    except:
        return None

#print(get_recipes("Tofu chili"))

recipe_link = "http://www.epicurious.com" + '/recipes/food/views/spicy-lemongrass-tofu-233844'

def get_recipe_info(recipe_link):
    recipe_dict = dict()
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(recipe_link)
        if not response.status_code == 200:
            return recipe_dict


        result_page = BeautifulSoup(response.content,'lxml')

        ingredient_list = list()
        for ingredient in result_page.find_all('li',class_='ingredient'):
            ingredient_list.append(ingredient.get_text())


        prep_steps_list = list()
        for prep_step in result_page.find_all('li',class_='preparation-step'):
            prep_steps_list.append(prep_step.get_text().strip())

        recipe_dict['ingredients'] = ingredient_list
        recipe_dict['preparation'] = prep_steps_list
        return recipe_dict

    except:

        return recipe_dict
        

# print(get_recipe_info(recipe_link))

#Construindo um dicionario

def get_all_recipes(keywords):
    results = list()
    all_recipes = get_recipes(keywords)
    for recipe in all_recipes:
        recipe_dict = get_recipe_info(recipe[1])
        recipe_dict['name'] = recipe[0]
        recipe_dict['description'] = recipe[2]
        results.append(recipe_dict)
    return(results)

#obtendo um dicionario de todos os resultados de Tofu Chili, com descricao, Ingredientes, etc
print(get_all_recipes("Tofu chili"))