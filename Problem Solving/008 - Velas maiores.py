#!/bin/python3
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    mx = 0
    mxCount = 0
    for i in range (n):
        if mx < ar[i]:
            mx = ar[i]
        
    for i in range(n):
        if mx == ar[i]:
            mxCount +=1
    
    return mxCount
        
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
