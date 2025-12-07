def decFun(f):
    def innerFun():
        print("Welcome")
        f()
    return innerFun
def fun():
    print("User")
fun=decFun(fun)
fun()