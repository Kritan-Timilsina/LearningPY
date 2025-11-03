class Solution:
    def printPrimeFactorization(self, n):
        #code here
        for i in range(2,n):
            if n%i==0:
                flag=0
                for j in range(2,i):
                    if i%j==0:
                        flag+=1
                        break
                if flag<=0:
                    print(i)

Solution().printPrimeFactorization(100)