#https://www.hackerrank.com/challenges/30-sorting/problem

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

#codigo de Bubble Sort
numberOfSwaps = 0
for i in range(n):
    for j in range( n-1):
        if a[j] > a[j+1]:
            t = a[j+1]
            a[j+1] = a[j]
            a[j] = t
            numberOfSwaps +=1

    if numberOfSwaps == 0:
        break
    
print('Array is sorted in {0} swaps.'.format(numberOfSwaps))
print('First Element: {0}\nLast Element: {1}'.format(a[0],a[n-1]))