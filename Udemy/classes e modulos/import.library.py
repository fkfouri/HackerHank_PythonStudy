'''
Neste caso, importa todas as funcoes da biblioteca math
'''
import math

x=81
print(math.sqrt(x))


'''
Neste caso, importa todas as funcoes da biblioteca math.
Neste caso, define um alias para math. Neste caso, escolhido o alias 'm'
'''
import math as m

x=100
print(m.sqrt(x))


'''
Neste caso, nao sera importado toda a biblioteca Math, apenas
a funcao desejada, neste caso, a funcao sqrt
'''
from math import sqrt

x=144
print(sqrt(x))
