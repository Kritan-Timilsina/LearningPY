
def fudge(func):
    def inner():
        print("You added fudge in your icecream")
        func()
    return inner

@fudge
def icecream():
    print("Here's your icecream")
icecream()