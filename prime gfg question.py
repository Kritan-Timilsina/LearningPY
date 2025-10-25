#User function Template for python3
n = int(input())

# Your code here
flag=0
for i in range(1,n+1):
    if n%i==0:
        flag+=1
    else:
        continue
if flag==2:
    print (True)
else:
    print (False)
    