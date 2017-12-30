#https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

import sys

def solve(n, p):
    if n == p or p == 1:
        return 0
        
    turnL = 0
    for i in range(1, n, 2):
        #print('{0} - {1}'.format(i,turnL))
        if p == i or p == i - 1:
            break
        else:
            turnL +=1
    
    turnR = 0
    for i in range(n, 1, -2):
        #print('{0} - {1}'.format(i, turnR))
        if n % 2 == 1 and (p == i or p == i - 1): 
            break   
        elif n % 2 == 0 and (p == i or p == i + 1):
            break
        else:
            turnR +=1
        
    #print(turnL)
    #print(turnR)
    if turnL < turnR:
        return turnL
    else:
        return turnR
            

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
