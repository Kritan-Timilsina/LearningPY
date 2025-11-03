class Solution:
    def printPrimeFactorization(self, n):
        def isPrime(n):
            
             if n<2:
                return False
             for i in range(2,n):
                if n%i==0:
                    return False
             return True
        def PrintPfactorial(n):
            for i in range(2,n+1):
                if isPrime(i):
                    while n%i ==0:
                        print(i,end=" ")
                        n//=i
        PrintPfactorial(n)
Solution().printPrimeFactorization(100)