# Create a list of numbers from 1 to 20 using list comprehension.
l= [i for i in range(1,21)]
print(l)
# Create a list of even numbers from 1 to 20.
l=[i for i in range(1,21) if i%2==0]
print(l)
# Create a list of squares of numbers from 1 to 10
l=[i**2 for i in range(1,11)]
print(l)
# 👉 Output: [1, 4, 9, 16, ...]
# 🟡 Medium
# Given a list:
l = [10, 25, 30, 45, 60, 75]

# 👉 Create a new list containing only numbers greater than 40
a=[i for i in l if i>40]
print(a)
# From the same list, create a list of:

# 👉 numbers divisible by 5 AND greater than 30
d=[i for i in l if i%5==0 and i>30]
print(d)
# 🔴 Challenging (important)
# Given:
l = [11, 121, 13, 22, 101, 50]
def isPrime(n):
    prime=True
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

p=[i for i in l if isPrime(i)]
print(p)
# 👉 Create:

# A list of prime numbers

# A list of palindrome numbers

# (using your isPrime() and isPalindrome() functions)

# 🔥 Bonus (very good for DSA thinking)
# From a list, create a new list where:
# 👉 Each number is replaced by its sum of digits

# Example:

# [12, 34] → [3, 7]
# 🎯 Goal
# Use only list comprehension
# No normal loops (try your best)