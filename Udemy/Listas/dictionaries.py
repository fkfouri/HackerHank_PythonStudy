'''
Dicionarios - Chave/Valor
'''

mktcaps = {'AAPL':538.7,'GOOG':68.7,'IONS':4.6}



mktcaps['AAPL'] #Returns the value associated with the key "AAPL"

mktcaps.get('GS') #Returns None because GS is not in mktcaps
#mktcaps['GS'] #Error because GS is not in mktcaps

mktcaps['GS'] = 88.65 #Adds GS to the dictionary
print(mktcaps) 

del(mktcaps['GOOG']) #Removes GOOG from mktcaps
print(mktcaps)

mktcaps.keys() #Returns all the keys

mktcaps.values() #Returns all the values

#sort
print(sorted(mktcaps.keys()))
print(sorted(mktcaps.values()))


#iteration
for k in mktcaps:
    print(k, mktcaps[k])



s = {1, 2, 4, 3}
print(max(s), len(s), min(s))