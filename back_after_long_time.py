#i am writing this to clear my hand as i have not coded since 1+ months 
"""Wap even numbers till n and odd numbers till n"""
n=int(input("Enter a number till which you need result:"))
odd=[]
even=[]
for i in range(1,n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"Even :{even}\n Odd:{odd}")

