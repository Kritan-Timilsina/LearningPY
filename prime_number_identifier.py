n=int(input("Enter a number:"))
def prime(n):
    flag=0
    for i in range(2,n):
        if (n%i==0):
            flag+=1
    if flag==0:
        print("You Entered Prime number.")
    else :
        print("You entered composite number.")
prime(n)

