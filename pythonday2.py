a=5
print(type(a))
print (id(a))
b=a 
print(id(b))
c=b
print(a is b )
print(c is b)
d=7
print(d is a)
b=None 
print(type(b))
# to declare list we use square bracket 
l=[10,20,30]
#to declare tuple we use ( ) Note: Tuples are immutable i.e. not changable 
t=(a,b,c)
#set is also made using curly braces it is collection of keys 
s={a,b,c}
#to create dictionary we use curly braces {} it is collection of key value pairs 
d={
    a:5,b:3
}
print(type(l))
print(type(s))
print(type (t))
print(type(d))
