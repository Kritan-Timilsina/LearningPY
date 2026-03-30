"""Create a list of at least 7 integers.
From that list, do the following:
Print only Prime numbers
Print only Palindrome numbers
Print numbers that are both Prime AND Palindrome"""
from back_after_long_time import isPrime_Palindrome
l=[100,99,127,33,77,88,85]
def SortingList(l):
    for i in l:
        isPrime_Palindrome(i)
        
SortingList(l)