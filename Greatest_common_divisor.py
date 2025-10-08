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