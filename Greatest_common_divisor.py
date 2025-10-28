a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
def minFunction(a,b):
    if (a<b):
        return a
    else :
        return b
gcd=0
min=minFunction(a,b)
for i in range(2,min+1):
    if(a%i==0 and b%i==0):
        gcd=i
    else:
        continue
print("Greatest common divisor:",gcd)

#or 
import math
gcd2=math.gcd(a,b)
print(gcd2)
"""#User function Template for python3
a = int(input())
b = int(input())
def minFunction(a,b):
    if(a<b):
        return a
    else:
        return b
gcd=1
min_val=minFunction(a,b)
for i in range(1,min_val+1):
    if (a%i==0 and b%i==0):
        gcd=i
    else:
        continue
print(gcd)
# Your code here
"""