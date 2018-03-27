'''
A diferenca de um tupla e uma lista eh que a tupla eh imutavel
'''

t = (1,2,3,4,5)
print(t)
print(t[3])
#t[3]=99            #=> Erro, nao tolera imutabilidade
#print(t[8])        #=> Erro, index out of range


my_tuple = (123, 'Mike')
print(my_tuple * 2)