'''
formas de encontrar itens em uma colecao (lista/tupla)

'''

#metodo 1 => range
li = [5,6,7,8,89,9]
for index in range(len(li)):
    print(li[index])


#metodo 2 => tipo for each
print(10*'-')
for item in li:
    print(item)