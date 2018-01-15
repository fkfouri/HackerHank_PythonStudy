'''
Programaçção funcional:
    Reducao de codigo fonte
    Melhora a velocidade
    Pode facilitar as implementacoes
    Escreve bem menos

Desvantagem:
    Pode gerar codigos dificieis de ler (obscuro)

Lambda
    Nao precisam ser nomeadas
    funcoes anonimas

'''

#funcao tradicional de potencia
def pot2(x):
    return x**2

print(pot2(5))

#funcao lambda de potencia
l_pot2 = lambda x: x**2

print(l_pot2(3))

# funcao lambda de fatorial
l_fat = lambda n: n * l_fat(n-1) if n > 1 else 1
print(l_fat(5))
