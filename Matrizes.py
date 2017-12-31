# TIPO LISTA

a = [1, 2,3,4,5,6,7,8]
print ('max(): ' + str(max(a)))
print ('min(): ' + str(min(a)))

#multiplica por dois todos os elementos
newList = [el*2 for el in a]
print(newList)

#Stack
print('Stack pop(): ' + str(newList.pop()))