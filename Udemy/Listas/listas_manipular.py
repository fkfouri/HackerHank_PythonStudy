#Concatencao de duas listas
list1 = [1,2,3,4]
list2 = [5,6,7,8,9,10]

list3 = list1 + list2

print(list3)

#a lista pode ser de generica
list4 = [1,'a',[1,2,3]]
print(list4, 'Lista de tipos diferentes')

#criando uma lista vazia
x = list()
y = []
print(x,y,'CRIANDO LISTAS VAZIAS')

#remocao do ultimo item da lista
list3.pop()
print(list3, '=> remocao do ultimo item da lista')

#remocao atraves do indice e o item do index 2
list3.pop(2)
print(list3, '=>remocao atraves do indice e o item do index 2')

#remocao do elemento numero 4
list3.remove(7)
print(list3, '=>remocao do elemento valor 7')

#verifica se o elemento esta na lista
if 14 in list3:
    print('encontrado')
else:
    print('elemento nao encontrado')

#transformacao de lista em tupla
t_list=tuple(list3)
print(t_list, type(t_list))

#acrescentando um item no final da lista
list3.append(15)
list3 += [99]
print(list3, '=> acrescentando um item no final da lista, neste caso, usando dois metodos')



#acrescentando um item em uma posicao da lista - primeiro parametro posicao e o segundo valor
list3.insert(5, 20)
print(list3, '=> acrescentando um item em uma posicao da lista - primeiro parametro posicao e o segundo valor')

#ordenacao da lista
list3.sort()
print(list3, '=> ordenacao da lista')

#faz a unpack do pacote, e adiciona cada  item no final da lista
list3.extend([1,2,3]) 
print(list3, '=> faz a unpack do pacote, e adiciona cada  item no final da lista')


