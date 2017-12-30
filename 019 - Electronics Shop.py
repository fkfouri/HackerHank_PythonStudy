#!/bin/python3
#https://www.hackerrank.com/challenges/electronics-shop/problem

import sys

def getMoneySpent(keyboards, drives, s):
    # Complete this function
    max = -1
    for k in range(len(keyboards)):
        for d in range(len(drives)):
            if keyboards[k] + drives[d] <= s and keyboards[k] + drives[d] > max:
                max = keyboards[k] + drives[d]
                
                
    return max 
    

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))

#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)