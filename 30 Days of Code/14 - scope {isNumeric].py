#https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    
    ## funciona
    #def computeDifference(self):
    #    for i in range(len(self.__elements)):
    #        for j in range (len(self.__elements)):
    #            delta = abs(self.__elements[i] - self.__elements[j])
    #            if delta >= self.maximumDifference:
    #                self.maximumDifference = delta

    ##Pratico
    def computeDifference(self):
            self.maximumDifference=max(a)-min(a)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)