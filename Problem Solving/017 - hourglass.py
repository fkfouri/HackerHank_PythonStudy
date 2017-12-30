#https://www.hackerrank.com/challenges/2d-array/problem
#!/bin/python3 

import sys 

def getAmp(y0,x0,arr): 
    s = 0 
    for i in range(3): 
        s += arr[y0][x0 +i] 
    for i in range(3): 
        s += arr[y0+2][x0 + i]   
    s += arr[y0+1][x0+1]     
    return s 
        
    

arr = [] 
for arr_i in range(6): 
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')] 
   arr.append(arr_t) 

n = len(arr[0])     
maxV = -10E5; 
for x in range(n -2): 
    for y in range(n-2): 
        temp = getAmp(y,x,arr) 
        if temp > maxV: 
            maxV = temp 
        
print (maxV) 