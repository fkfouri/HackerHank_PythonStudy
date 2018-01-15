'''
reduce =>   aplica uma funcao sobre uma sequencia que vai acumulando o 
            valor de retorno de uma funcao a partir de um valor incial

removido da versao 3
        - a maioria das vezes voce faz um for, que deixa mais legivel que realizar um reduce
'''

import functools

lista =[1,2,3,4]
print(functools.reduce(lambda x,y : x+y, lista)) #resulta 10