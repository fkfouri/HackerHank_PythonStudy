#!/bin/python3
#https://www.hackerrank.com/challenges/sock-merchant/problem

import sys

def sockMerchant(n, ar):
    # Create dict
    socks  = dict()
    for i in range(n):
        #verify if exist keys
        if ar[i] in socks:
            socks[ar[i]] += 1
        else:
            socks[ar[i]] = 1  
    
    pairs = 0
    # for each key value in dict
    for key, value in socks.items():
        # soma pela divisao de numeros inteiros
        pairs += value//2
    
    return(pairs)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)