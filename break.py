a=int(input("Enter the number:"))
#find the smallest divisor greater than 1 
for i in range(1,a+1):
    if i!=1 and a%i==0:
        print (i)
        break