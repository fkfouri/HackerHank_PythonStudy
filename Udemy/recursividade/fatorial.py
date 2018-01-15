#exemplo de recursividade para determinar fatorial de um numero

# funcao tradicional
def fat(n):
    if n == 0:
        return 1
    return n * fat(n-1)

print(fat(5)) # 5! => 5 * 4 * 3 * 2 * 1 = 120


# funcao lambda de fatorial
l_fat = lambda n: n * l_fat(n-1) if n > 1 else 1
print(l_fat(5))