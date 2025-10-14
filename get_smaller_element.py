def getSmaller(l,x):
    res=[]
    for e in l:
        if e<x:
            res.append(e)
    return res
l=[10,20,30,40,50,60]
x=50
print(getSmaller(l,x))