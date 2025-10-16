def issorted(l):
    i=1
    while(i<len(l)):
        if l[i]< l[i-1]:
            return False
        i=i+1
    return True

l=[1,2,3,3.5,5,6]
if issorted(l):
    print("Yes")
else:
    print("No")