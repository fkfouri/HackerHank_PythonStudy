#objetos acessados por meio de uma chave, nao por indice
mp = {'chave1':'valor1', 'chave2' : 'valor2'}
print(mp)
assert mp['chave2'] == 'valor2'

#operador in- a chave esta no mapa
print('chave1' in mp)
print('chave3' in mp)

#operador del - remover do mapa
del mp['chave2']
print(mp)