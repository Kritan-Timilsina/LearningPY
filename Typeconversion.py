#Type conversion 
#implicit
a=5
b=10.3
c=a+b
print(c)
a=True
c=a+b
print(c)
#Explicit 
a="123"
print(int(a)+b)
#string ma letter le lekhyo bhani invalid aauncha 
l="Kritan"
print(list(l))
print(tuple(l))
print(set(l))
s=('a','b','c','d')
print(str(s))
a=10
b=11
print(str(a)+str(b))
a=20
print(bin(a),hex(a),oct(a))
a="11001"
print(int(a,2))
print(int(a,8))