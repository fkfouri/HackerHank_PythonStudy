#https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import sys

def calc(temp, v1, v2):
    if v1 != v2:
        temp[0] +=1
    else:
        temp[1] +=1
    return temp


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    temp=[0,0]
    temp = calc(temp, a0, b0)
    temp = calc(temp, a1, b1)
    temp = calc(temp, a2, b2)
    return temp

#a0, a1, a2 = input().strip().split(' ')
#a0, a1, a2 = [int(a0), int(a1), int(a2)]
#b0, b1, b2 = input().strip().split(' ')
#b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(5, 1, 5, 1, 5, 1)
print(" ".join(map(str, result)))