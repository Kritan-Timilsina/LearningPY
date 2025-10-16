def average(l):
    sum=0
    for x in l:
        sum=sum+x
    n=len(l)
    return sum//n
l=[10,11,12]
print(average(l))

