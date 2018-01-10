# TIPO LISTA

a = [4,5,3,1,2,8,7,6,8]
print ('max(): ' + str(max(a)))
print ('min(): ' + str(min(a)))
print(10 *'=' + '> testes')
#casos de testes
assert a[0] == 4
assert a[1] == 5
assert a.index(3) == 2

#tudo eh uma sequencia no python
lista = ["a", "b", "c"]
temp = "abc"
assert lista[0] == temp[0]

#Slices
print(10 *'=' + '> Slices')
print(a[3:7]) #pega do indice 3 ao indice 7 => >=3 and <7

print(10 *'=')

#multiplica por dois todos os elementos
newList = [el*2 for el in a]
print(newList)

#entender o reverse
print([4,5,3,1,2,8,7,6,8].reverse()) #funciounou no exo 18
print(reversed([4,5,3,1,2,8,7,6,8])) 
print([4,5,3,1,2,8,7,6,8][::-1])
print(10 *'=')

#entender o sort
print([4,5,3,1,2,8,7,6,8].sort())
print(sorted([4,5,3,1,2,8,7,6,8]))
print(10 *'=')

#Stack
print('Stack pop(): ' + str(newList.pop()))

#Join e converte cada caracter em string
print('Join: ' + ' * '.join([str(el) for el in newList]))

#Organiza, remove duplicidades, ordena
print(set(a))

