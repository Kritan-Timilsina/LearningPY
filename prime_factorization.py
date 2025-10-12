n=int(input("Enter a number:"))
def isPrime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag+=1
    if flag==0:
        return True
    else :
        return False
 
def PrintPfactorial(n):
    for i in range(2,n+1):
        if isPrime(i):
           
            while n%i==0:
                print (i)
                n//=i
PrintPfactorial(n)