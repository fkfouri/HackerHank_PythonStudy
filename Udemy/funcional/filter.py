'''
filter =>   faz um filter
'''

# filtra os numeros pares do range de 1 a 10
f = filter(lambda x: x%2 == 0, range(10))

for i in f:
    print(i)