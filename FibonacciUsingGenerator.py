# Write a generator function called fibonacci(n) that does the following:

# Generates the first n Fibonacci numbers

# Uses yield (not return)

# Does not store the sequence in a list

# Works with a for loop

def fibonacci(n):
    a,b=0,1
    count=0
    while count<n:
        yield a
        a,b=b,a+b
        count+=1

x=fibonacci(10)
print(next(x))    
print(next(x))  
print(next(x))  
print(next(x))    
print(next(x))  
print(next(x))  


