'''
map => Queremos aplicar uma funcao em todos os itens de uma ou mais sequencias

'''

lista = [1,2,3]
m = map(lambda x: x**2, lista)
n = map(lambda x: str(x) + ' --> ' + str(x**2), lista)

for i in m:
    print(i)

for i in n:
    print(i)