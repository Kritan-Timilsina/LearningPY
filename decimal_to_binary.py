n=int(input("Enter a number:"))
def decToBin(n):
    if n==0:
        return ("0")
    res=""
    while n>0:
        res=res+str(n%2)
        n=n//2
    return (res[::-1])
print("Binary equivalent:",decToBin(n))

""""
or 
def DectoBin(n):
res=bin(n)
return res[2:]


gfg ans
#User function Template for python3
#Complete the below function
def toBinary(n):
    #Your code here
    if n==0:
        return ("0")
    res=""
    while n>0:
        res=res+str(n%2)
        n=n//2
    return (res[::-1])

"""