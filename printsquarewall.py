#User function Template for python3
n = int(input())

# Your code here
def sqwall(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        
        print()

sqwall(n)