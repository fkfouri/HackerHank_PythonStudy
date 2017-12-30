#!/bin/python3
#https://www.hackerrank.com/challenges/kangaroo/problem

import sys

def getAn(a1, n, r):
    return a1 + (n -1)*r

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if(v1 == v2 and x1 != x2):
        return 'NO'
    elif x1<x2 and v1 < v2:
        return 'NO'
    elif x1<x2:
        for n in range (100**10):
            if getAn(x1,n,v1) > getAn(x2,n,v2):
                return 'NO'
            elif getAn(x1,n,v1) == getAn(x2,n,v2):
                return 'YES'
    elif x2<x1:
        for n in range (100**10):
            if getAn(x2,n,v2) > getAn(x1,n,v1):
                return 'NO'
            elif getAn(x1,n,v1) == getAn(x2,n,v2):
                return 'YES'
            

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
