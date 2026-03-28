#i am writing this to clear my hand as i have not coded since 1+ months 
# """Wap even numbers till n and odd numbers till n"""
#     n=int(input("Enter a number till which you need result:"))
#     odd=[]
#     even=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)

#     print(f"Even :{even}\n Odd:{odd}")

"""now creating counter"""
def oecounter(n):
    oc=0
    ec=0
    for i in range(1,n+1):
        if i%2==0:
            ec+=1
        else:
            oc+=1
    print(f"Total no of odd number between 1 and {n} is {oc}\nTotal number of even number between 1 and {n} is {ec}")
n=int(input("Enter n:"))

oecounter(n)
