def fun1():
    print("Inside Fun1")
def fun2(f):
    print("inside fun2")
    f()
f=fun1
f()
print()
fun2(f)
"""nested function"""