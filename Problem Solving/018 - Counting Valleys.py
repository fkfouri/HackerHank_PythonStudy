#https://www.hackerrank.com/challenges/counting-valleys/problem

n = int(input().strip())
h = input().strip()

#print(h)

v, m, sea = 0, 0, 0

#current Level
cl = 0
up = False
down = False


for i in range(n):
    if h[i]== 'U': #UP
        cl += 1
        if cl > sea:
            m += 1
            up = True
        elif cl == 0:
            down = False
            

    elif h[i] =='D': # DOWN
        cl -= 1
        if cl < sea and down == False:
            v += 1
            down = True
        elif cl == 0:
            up = False 
            
    #print('{0} - {1} - {2}'.format(h[i], cl, isChecked))

print(v)
