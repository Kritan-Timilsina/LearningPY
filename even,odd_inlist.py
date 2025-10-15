def oddEvenList(l):
   
    for e in l:
        if e%2==0:
            even.append(e)
        else:
            odd.append(e)
    
l=[10,20,14,25,27,19,30]
odd=[]
even=[]
oddEvenList(l)
print(odd)
print(even)