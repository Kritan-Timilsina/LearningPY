#and,or,not
x=True
y=20
z=False
a=z or x#short circuiting  since first case is true z is only checked 
b=z and y #short circuiting since first condition is 0 second is not checked 
c=not x
print(a,b,c)