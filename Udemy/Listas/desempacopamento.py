lista = [1,2,3]

#exemplo de desempacotamento de uma lista
a,b,c = lista
print(a,b,c)

#desempacotamento de uma tupla
d,e,f = tuple(lista)
print(d,e,f)

#uma forma de desempacotar ignorado elementos (colocando underscore)
#neste exemplo, o interesse apenas pelo primeiro e terceiro elemento
lista1 = [1,2,3,4]
g,_,h,_ = lista1
print(g,h)

#funcao de retorno de uma tupla
def func(x,y):
    return x**2, y**2

print(func(2,3))

#desempacotando o retorno de uma funcao
r1, r2 = func(2,3)
print(r1, r2)