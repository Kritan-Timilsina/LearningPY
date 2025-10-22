class Solution:
    def __init__(self,n):
        self.n=n
    def printPattern(self):
        n=self.n
        #Code here
        while n>=0:
            print("* "*n)
            n=n-1
n=int(input())      
s=Solution(n)
s.printPattern()