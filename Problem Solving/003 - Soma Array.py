def simpleArraySum(n, ar):
    # Complete this function
    temp = 0
    for x in range(n):
        temp += ar[x]
    return temp

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
