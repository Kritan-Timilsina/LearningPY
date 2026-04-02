number=int(input("Enter the number:"))
def SumofDigits(n):
    sum=0
    while n!=0:
        sum+=n%10
        sum=sum/10
    print(f"Sum of digits is {sum}")

SumofDigits(number)