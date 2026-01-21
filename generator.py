import sys
def creater():
    lst=[]
    i=1
    while i<=200:
        list.append(i)
        i+=1
    return list

print(creater())
z=sys.getsizeof(lst)
print(z)
#excess memory is used 
#now using generator -it generates one at a time 

def creater1():
    i=1
    while i<=200:
        yield i
        i+=1
print(creater1())
x=creater1()
print(next(x))
print(next(x))
print(next(x))