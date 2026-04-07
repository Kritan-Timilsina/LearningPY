# Create a tuple with 5 numbers and print it.
# From a tuple:
t=(5,3,2,11,2)
print(t)

# 👉 Print:

# First element
print(t[0])
print(t[-1])
# Last element
# Count how many times a number appears:
# t = (1, 2, 2, 3, 2, 4)
print(f"Count of tuple is:{t.count(2)}")
# 👉 Count occurrences of 2

# 🟡 Medium
# Given:
t = (25,10,100,23,1)

print(f"Max of tuple is {t}")
# 👉 Find:

# Maximum value
print(max(t))

# Minimum value
print(min(t))

# Sum of all elements
print(sum(t))
# Convert a list into a tuple and print it:
l = [1, 2, 3, 4]
l=tuple(l)
print(l)
# Given a tuple:
t = (10, 20, 30, 40)
def tupleList(t):
    l=[]
    for i in t:
        l.append(i**2)
    tup=tuple(l)
    print(tup)
tupleList(t)

# 👉 Create a new tuple with each value doubled

# 🔴 Slightly Challenging
# Write a function that:
def calculator(a,b):
    return a+b,a*b,a-b
print(calculator(10,2))
# Takes two numbers
# Returns:
# Sum
# Product
# Difference

# 👉 Use tuple return

# Given:
t = (10, 20, 30, 40, 50)
def tuprev(t):
    rev=()
    for i in range(len(t)-1,-1,-1):
        rev=rev+(t[i],)
    print(rev)
        
tuprev(t)


# 👉 Reverse the tuple (without using built-in reverse function)

# 🔥 Bonus (important thinking)
# Given:
t = (1, 2, 3)

# 👉 Convert it into:

# (1, 4, 9)
def tupsq(t):
    sq=()
    for i in t:
        sq+=(i**2,)
    print(sq)
tupsq(t)
# (Hint: square each element)

# 🎯 Goal
# Understand immutability