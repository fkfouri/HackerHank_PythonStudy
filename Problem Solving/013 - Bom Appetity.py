#!/bin/python3
#https://www.hackerrank.com/challenges/bon-appetit/problem

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    totalPaid = b * 2
    del ar[k] #remove item from list
    fairPaid = sum(ar) #sum all values
    if totalPaid == fairPaid:
        return 'Bon Appetit'
    else:
        return int((totalPaid - fairPaid)/2)


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)