a=int(input("Enter first number:"))
b=int(input("Enter Second number:"))
res=max(a,b)
while(res<a*b):
    if res%a==0 and res%b==0:
        break
    res+=1
print("Lcm is ",res)
"""#User function Template for python3
def LCM(a,b):
    # Your code here
    res=max(a,b)
    while(res<a*b):
        if res%a==0 and res%b==0:
            break
        res+=1
    return res"""