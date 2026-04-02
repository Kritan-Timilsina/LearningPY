# Write functions for:

# Sum of digits

# Input: 1234 → Output: 10
n=int(input("Enter the number:"))
def SumofDigits(n):
    sum=0
    while n!=0:
        sum+=n%10
        n=n//10
    print(f"Sum of digits is {sum}")

SumofDigits(n)


# Count number of digits
def NumofDigits(n):
    count=0
    if n==0:
        return 1
    while n!=0:
        n=n//10
        count+=1
    return count
print(f"Number of digits is:{NumofDigits(n)}")
# Input: 1234 → Output: 4

# Reverse a number (without string)
def Reverse(n):
    rev = 0
    while n != 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
# Input: 123 → Output: 321
print(f"The number in reverse is:{Reverse(n)}")
# Check Armstrong number
def Armstrong(n):
    copy=n
    sum=0
    while n!=0:
        a=n%10
        n=n//10
        sum=sum+a**3
    if sum==copy:
        print(f"Armstrong Number")
    else:
        print(f"Not Armstrong Number")
Armstrong(n)
# 153 → 1³ + 5³ + 3³ = 153 ✔️