def firstDigit(n):
    while n>=10:
        n=n//10
    return n
x=int(input("Enter first digit:"))
print(firstDigit(x))


