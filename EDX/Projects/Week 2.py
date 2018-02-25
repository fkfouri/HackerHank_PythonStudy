'''
Quiz 1
'''
x = []
y = [None]
z = list()
a = list([])

print(x,y,z,a)

l = [1,2,3,4,5,6,7]
print(l[0], l[:2], l[:-2], l[3:5])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(data[1][0][0])

numbers = [1, 2, 3, 4] 
numbers.append([5, 6, 7, 8])
print(len(numbers))
    

'''
Quiz 2
'''

dict1 = {"john":40, "peter":45} 
dict2 = {"john":466, "peter":45}
#print( dict1 > dict2 )


s = {1, 2, 4, 3}
s[3] = 5,
print(max(s), len(s))