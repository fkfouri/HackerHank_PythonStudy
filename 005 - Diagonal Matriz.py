#https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

diag1, diag2 = 0, 0

for x in range(len(a)):
    diag1 += a[x][x]
    diag2 += a[len(a) -1 -x][x]
    
x = diag1 - diag2
print(abs(x))