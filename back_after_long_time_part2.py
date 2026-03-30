"""Create a list of at least 7 integers.
From that list, do the following:
Print only Prime numbers
Print only Palindrome numbers
Print numbers that are both Prime AND Palindrome"""
from back_after_long_time import isPrime_Palindrome
l=[7,99,127,33,77,88,11]
def SortingList(l):
    for i in l:
        isPrime_Palindrome(i)
        
#SortingList(l)

def CategorizingList(l):
    Prime=[]
    Palindrome=[]
    PrimeandPalindrome=[]
    for j in l:
        prime=True
        palindrome=False
        if j<=1:
            prime=False
            
        for k in range(2,int(j**0.5)+1):
            if j%k==0:
                prime=False
                break
        

        if str(j)==str(j)[::-1]:
            palindrome=True
        
        if prime:
            Prime.append(j)
        if palindrome:
            Palindrome.append(j)
        if prime and palindrome:
            PrimeandPalindrome.append(j)

        
    print(f"Prime numbers are {Prime}")
    print(f"Palindrome numbers are {Palindrome}")
    print(f"Prime and Palindrome numbers are {PrimeandPalindrome}")

CategorizingList(l)
