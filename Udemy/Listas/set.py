'''
Transforma uma colecao em um conjunto (ordenado? e distinto)
'''

t = {'AAPL', 'GE', 'NFLX', 'IONS'}

print('AAPL' in t, '=> AAPL eh membro do conjunto')
print('IBM' in t, '=> IBM nao pertence ao conjunto')

pt = {'IONS', 'IMCL'}
print(t.isdisjoint(pt), ' ENTENDER ESSE CODIGO', ' => Empty intersection') 
print(pt.isdisjoint(t), ' ENTENDER ESSE CODIGO', ' => Empty intersection') 

print(pt <= t, '=> SubSet')
print(pt < t, '#proper-subset test')

print(t>pt, '#superset')
print(t & pt, '#intersection')

print(t | pt, '#union')
print(t - pt, '#set difference')
