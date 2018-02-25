#
lista = [4,10,2,1,5]
print(lista)
print()

#a lista sem o dois ultimos caracter
print(lista[:-2], '=> a lista sem o dois ultimos caracter')

#a lista sem o primeiro caracter
print(lista[1:], '=> a lista sem o primeiro caracter')

#inverte lista
print(lista[::-1], '=> inverte lista')

# Obtem o item index 1
print(lista[1], '=> Obtem o item index 1')

# Obtem o item index 1 de tras pra frente
print(lista[-1], '=> Obtem o item index 1 de tras pra frente')

#lista da posicao 1 ate a posicao 3, sendo o 3 um limite superior aberto .... 1<=p<3
print(lista[1:3], '=> lista da posicao 1 ate a posicao 3, sendo o 3 um limite superior aberto .... 1<=p<3')