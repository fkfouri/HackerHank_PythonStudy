'''
Tipos de funcoes
'''

# funcao sem definicao de return, resulta em None
def test(a):
    a *= 10

print (test(4))

#================================================================
#funcao que retorna multiplos values
def minmax(x,y):
    return min(x,y), max(x,y)

print(minmax(7,4)) #valor esta packed


#================================================================
def div(x,y):
    return x/y

a=30
print(div(a,10))

x,y = 10, 30
print(div(y,x)) # a curiosidade aqui, que foi invertido os argumentos, mas foram utilizados o mesmo argumentos 'x e y' da funcao


print(div(x=30,y=10)) 
print(div(y=10,x=30)) # neste exemplo, os argumentos estao invertidos, mas foram atribuidos nominalmente os valores de cada argumento
                      # assim, a troca da ordenacao de argumentos nao modificou o comportamento da funcao



#================================================================
#optional values
def f01(x,y, z= 0):
    t = (y-x)/x
    if z and z == 100:
        return t * 100
    return t

print(f01(1.2, 91.2))
print(f01(1.2, 91.2, 100))


#================================================================
# Funcao passando outra funcao como argumento
# para o python, funcao e objetos sao iguais.

def order_by(a,b, order_function):
    return order_function(a,b)

print(order_by(4,7, max))
print(order_by(4,7, min))
order_by('teste','fabio',print)