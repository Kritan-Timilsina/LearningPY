def icecream():
    print("Here's your icecream")

def fudge(func):
    def inner():
        print("You added fudge in your icecream")
        func()
    return inner
icecream=fudge(icecream)
"""manually decorator liyeko yo ma chai @ use nagari """
icecream()