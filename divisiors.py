class Solution:
    def print_divisors(self, n):
      
        for i in range(1,n+1):
            if n%i==0:
                print(i,end=" ")
            else :
                continue
n1=Solution()
n1.print_divisors(10)
