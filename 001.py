print('teste')
print ('oi mundo')

#isto eh um comentario

def simpleArraySum(n, ar):
    # Complete this function
    out = 0
    for x in range(n):
        out = out + ar[x]
    print(out)

simpleArraySum(5,[1,2,3,4,5])