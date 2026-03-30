#i am writing this to clear my hand as i have not coded since 1+ months 
# """Wap even numbers till n and odd numbers till n"""
#     n=int(input("Enter a number till which you need result:"))
#     odd=[]
#     even=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)

#     print(f"Even :{even}\n Odd:{odd}")

"""now creating counter"""
def oecounter(n):
    oc=0
    ec=0
    for i in range(1,n+1):
        if i%2==0:
            ec+=1
        else:
            oc+=1
    print(f"Total no of odd number between 1 and {n} is {oc}\nTotal number of even number between 1 and {n} is {ec}")
#n=int(input("Enter n:"))

#oecounter(n)
# Write a function:

# Input: number
# Output:
# Prime or Not
# Palindrome or Not

def isPrime(n):
    c=0
    if n<=1:
        print(f"{n} is not a Prime number")
        return 
    for i in range(1,n+1):
        if n%i==0:
            c+=1
        
    if c==2:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")

#n=int(input("Enter value of n:"))
# isPrime(n)


def isPrimeOptimized(n):
    
    if n<=1:
        print(f"{n} is not a Prime number")
        return 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} is not a prime number")
            return 
    print(f"{n} is a Prime number")

#isPrimeOptimized(n)


def isPalindrome(num):
    if str(num)==str(num)[::-1]:
        print(f"{num} is Palindrome")
    else:
        print(f"{num} is not Palindrome")
#isPalindrome(n)


def isPrime_Palindrome(n):
    #assuming 
    pri=True
    pal=True
    if n<=1:
            pri=False
    
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                pri=False
                break
            
    if str(n)==str(n)[::-1]:
        pal=True
   
    if pri==True:
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")

    if pal==True:
        print(f"{n} is a Palindrome number")
    else:
        print(f"{n} is not a Palindrome number")

#isPrime_Palindrome(n)
"""Create a list of at least 5 integers directly in your code.
Write a function isPrime(n) that checks whether a number is prime using the √n method.
Write a function isPalindrome(n) that checks whether a number is a palindrome.
Traverse the list using a loop.
For each number, print:"""

l=[100,101,500,505,300]
def isPrime_Palindrome_list(l):
    for i in l:
        prime=True
        palindrome=False
        if i<=1:
            prime=False
        else:
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    prime=False
                    break
        
        if str(i)==str(i)[::-1]:
            palindrome=True
        if prime:
            print(f"{i} is a Prime number.\n")
        else:
            print(f"{i} is not a Prime number.\n")
        
        if palindrome:
            print(f"{i} is a Palindrome.\n")
        else:
            print(f"{i} is not a Palindrome.\n")
    
    
    



isPrime_Palindrome_list(l)