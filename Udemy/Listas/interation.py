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
    if item != 7:
        print(item)
    else:
        print('saida break do laco')
        break #sai do laco


print(10*'-')
def search_list(list_of_tuples,value):
    #Write the function here
    for i in list_of_tuples:
        a, b = i
        if a == value:
            return b
    return 0

prices = [('AAPL',96.43),('IONS',39.28),('GS',159.53)]
print(search_list(prices,'IONS')) 
print(search_list(prices,'test')) 
 