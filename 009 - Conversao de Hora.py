#!/bin/python3
#https://www.hackerrank.com/challenges/time-conversion/problem

import sys
from datetime import datetime

def timeConversion(s):
    # Complete this function
    time = datetime.strptime(s, '%I:%M:%S%p')
    #return '{%H:%M:%S}'.format(time) #nao funciona
    return time.strftime('%H:%M:%S')

s = input().strip()
result = timeConversion(s)
print(result)