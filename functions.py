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
    while n!=0:
        n=n//10
        count+=1
    return count
print(f"Number of digits is:{NumofDigits(n)}")
# Input: 1234 → Output: 4

# Reverse a number (without string)

# Input: 123 → Output: 321

# Check Armstrong number

# 153 → 1³ + 5³ + 3³ = 153 ✔️