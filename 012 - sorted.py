#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = int(str(input().strip()))
   unsorted.append(unsorted_t)

sorted = sorted(unsorted)
for i in range n:
    print(sorted[i])