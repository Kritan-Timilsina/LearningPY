"""Tuples are immutable and they are faster than list"""
t=(10,20,"Kritan")
print(type(t),t)
print(10 in t)
#Note if we create tuple with single value than it wont be of tuple type it will be of their respective type 
t=(5)
print(type(t),t)
t=("Kritan")
print(type(t),t)
#to make single item tuple we should insert comma after it 
t=(5,)
print(type(t),t)
#tuple can also be created without any parenthesis 
