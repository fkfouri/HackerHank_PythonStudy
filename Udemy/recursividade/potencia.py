'''
exemplo de recursividade aplicado para potencia de qualquer base de um numero

base, exp = 2, 10           => 2 **10 = 1024
'''

def pot(base, exp):
    if exp==0:
        return 1
    #decrementando o expoente ate que chegue a zero
    return base * pot(base, exp -1) 

print(pot(2,10))

print(pot(2,5))
'''
pot(2,5)                            = 36
    2 * pot(2, 4)                   => 2 * 16 = 36
        2 * pot(2, 3)               => 2 * 8 = 16
            2 * pot(2, 2)           => 2 * 4 = 8
                2 * pot(2, 1)       => 2 * 2 = 4
                    2 * pot(2, 0)   => 2 * 1 = 2

'''

print(pot(5,2)) # 5 * 5