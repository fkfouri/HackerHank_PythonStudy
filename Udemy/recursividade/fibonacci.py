# fibonacci = 1, 1, 2, 3, 5, 8, 13, ...
#exemplo de recursividade

def fib(n):
    if(n==1 or n ==2):
        return 1
    return fib(n-1) + fib(n-2)

print(fib(7))

'''
Esta é uma implementação lenta.

analise assintotica, é uma analise para verificar a velocidade do algoritimo.
Este algoritimo tem complexidade exponencial, com alto custo de processamento.
Poderia ser utilizado uma especie de dicionario

https://www.udemy.com/algoritmos-e-estruturas-de-dados-com-python3/learn/v4/t/lecture/4267676?start=330
'''