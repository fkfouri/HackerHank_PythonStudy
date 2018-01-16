import random

#retorna um numero inteiro 0 <= n < 4. Limite superior aberto, ou seja, retorna entre 0 e 3
print(random.randrange(4))

#retorna um numero inteiro entre 1 e 4 (inclusive). Retorna entre 1 e 4
print(random.randint(1,4))

#retorna um elemento aleatorio da lista
lista = ['a','b','c','d']
print(random.choice(lista))

#embaralha uma sequencia
random.shuffle(lista)
print(lista)

#faz uma amostragem de n elementos unicos de uma lista
print(random.sample(lista,3))

#numeros flutuantes entre 0 (incluseive) e 1 (exclusive)
print(random.random())

#numero flutuantes entre 1 range 5
print(random.uniform(1,5))