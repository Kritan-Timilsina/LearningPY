#decorator modifies function

def add(a,b):
    print(a+b)
def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using modified fx")
    return mfx
@greet
def Hello():
    print("Hello World")
Hello()