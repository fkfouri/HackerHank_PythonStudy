#https://www.hackerrank.com/challenges/flipping-the-matrix/problem
import copy

q = int(input().strip())
n = int(input().strip())

matrix = [[0 for x in range(2 * n)] for y in range(2 * n)] 
#print(matrix)

for i in range(2*n):
    line = [int(a_temp) for a_temp in input().strip().replace('\t',' ').split(' ')] #split e convert em inteiro cada valor da linha   
    #print(line)
    for j in range (2*n):
        #print('i: ' + str(i) + ' - j: ' + str(j) + ' - value: ' + str(line[j]))
        matrix[i][j] = line[j]

#sum of quadrant
def sumQ(matrix, qDesire, prod=False):# x, x0, y, y0): 
    
    if qDesire==1:
        x, x0, y, y0 = 0, n , 0, n
    elif qDesire==2:
        x, x0, y, y0 = 0,n, n, 2*n
    elif qDesire==3:
        x, x0, y, y0 = n, 2*n, 0, n
    else:
        x, x0, y, y0 = n, 2*n, n, 2*n
    
    totalQ = 0  
    prodQ = 1
    for i in range(x, x0):
        l = 0
        for j in range (y, y0):
            l += matrix[i][j]
        totalQ += l
        prodQ *= l
        
    if prod == False:
        return totalQ
    else:
        return prodQ
    

def revertArray(line):
    return line[::-1]

def revertLine(matrix, n, line):
    matrix[line] = revertArray(matrix[line])
    return matrix
    

def revertCol(matrix, n, col):
    temp =[]
    for i in range (2*n):
        temp.append(matrix[i][col])
        #temp[1,i] = matrix[i][col-1]
        
    temp = revertArray(temp)
    for i in range (2*n):
        matrix[i][col] = temp[i]
    
    return matrix[:]



def getBigger(matrix):
    print(matrix)
    q1 = sumQ(matrix, 1) #, 0, n , 0, n)
    q2 = sumQ(matrix, 2) #, 0, n, n, 2*n)
    q3 = sumQ(matrix, 3) #, n, 2*n, 0, n)
    q4 = sumQ(matrix, 4) #, n, 2*n, n, 2*n)
    
    #while max(q1,q2,q3,q4) != q1:  
    if max(q1,q2,q3,q4) == q1:
        return matrix
    
    elif max(q1,q2,q3,q4) == q4:
        if max(q2,q3) == q2 and q2 != q4:
            temp = []
            tempM = []
            for i in range(n, 2*n):
                tempM.append(revertCol(copy.deepcopy(matrix), n, i)[::1])
                temp.append(sumQ(tempM[i -n ], i))

                for i in range(len(temp)):
                    if temp[i] == max(temp):
                        #return getBigger(tempM[i]) 
                        print('q4 q2')
                        
        elif max(q2,q3) == q3 and q3 != q4:       
            temp = []
            tempM = []
            for i in range(n, 2*n):
                tempM.append(revertLine(copy.deepcopy(matrix), n, i)[::1])
                temp.append(sumQ(tempM[i -n ], i))

                for i in range(len(temp)):
                    if temp[i] == max(temp):
                        #print(tempM[i])
                        print('q4 q3')
                        return getBigger(copy.deepcopy(tempM[i]))
        elif q3 == q4:
            temp = []
            tempM = []
            for i in range(0, n):
                tempM.append(revertLine(copy.deepcopy(matrix), n, i)[::1])
                temp.append(sumQ(tempM[i -n ], i))

                print(temp)
                for i in range(len(temp)):
                    if temp[i] == max(temp):
                        print(tempM[i])
                        print('q2 == q3')
                        #return getBigger(copy.deepcopy(tempM[i]))
                
               
    elif max(q1,q2,q3,q4) == q2:
        temp = []
        tempM = []
        for i in range(0, n):
            tempM.append(revertLine(copy.deepcopy(matrix), n, i)[::1])
            temp.append(sumQ(tempM[i], i))

            for i in range(len(temp)):
                if temp[i] == max(temp):
                    print('q2')
                    #return getBigger(tempM[i])  
        
                        
        
    elif max(q1,q2,q3,q4) == q3:
        temp = []
        tempM = []
        for i in range(0, n):
            tempM.append(revertCol(copy.deepcopy(matrix), n, i)[::1])
            temp.append(sumQ(tempM[i], i))

            for i in range(len(temp)):
                if temp[i] == max(temp):
                    print('q3')
                    #return getBigger(tempM[i])  
       
    
    
def getNewBigger(matrix):
    print(matrix)
    q1 = sumQ(matrix, 1) #, 0, n , 0, n)
    q2 = sumQ(matrix, 2) #, 0, n, n, 2*n)
    q3 = sumQ(matrix, 3) #, n, 2*n, 0, n)
    q4 = sumQ(matrix, 4) #, n, 2*n, n, 2*n)
    
    if max(q1,q2,q3,q4) == q1:
        return copy.deepcopy(matrix)
    
    
    
print(matrix)      
matrix = getNewBigger(matrix)
print(sumQ(matrix, 1))

#print('q1: {0} - q2: {1} - q3: {2} - q4: {3}'.format(q1,q2,q3,q4))

#print(sumQ(matrix, 1))
   

#print(revertLine(matrix, n, 4))
    
    
#print(maxQ)       
#print(matrix)
#print(matrix[0])
#print(matrix[0][::-1])