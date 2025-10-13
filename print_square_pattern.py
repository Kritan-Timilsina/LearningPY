#User function Template for python3
n = int(input())

# Your code here
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n,)
    else:
        print("*"+" "*(2*(n-2)+1)+"*")
        