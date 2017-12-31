#https://www.hackerrank.com/challenges/30-queues-stacks/problem
#https://docs.python.org/2/tutorial/datastructures.html

class Solution:
    def __init__ (self):
        self.q = [] #Queue
        self.s = [] #Stack
        self.reverse = False
    
    #Stack
    def pushCharacter(self, ch):
        self.s.append(ch)
        
    def popCharacter(self):
        return self.s.pop()
     
    #Queue
    def enqueueCharacter(self, ch):
        self.q.append(ch)
        
    def dequeueCharacter(self): 
        if self.reverse == False:
            self.reverse = True
            self.q.reverse()
            
        return self.q.pop()