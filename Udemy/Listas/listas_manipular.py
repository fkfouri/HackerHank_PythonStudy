#Concatencao de duas listas
list1 = [1,2,3,4]
list2 = [5,6,7,8,9,10]

list3 = list1 + list2

print(list3)

#remocao atraves do indice e o item do index 2
list3.pop(2)
print(list3)

#remocao do elemento numero 4
list3.remove(4)
print(list3)

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

#acrescentando um item em uma posicao da lista - primeiro parametro posicao e o segundo valor
list3.insert(5, 20)
print(list3)

#ordenacao da lista
list3.sort()
print(list3)