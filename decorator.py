#it is a function that takes another function as an argument and returns a function
def decorator(func):
    def wrapper():
        print("Transaction initiated.")
        func()
        print("Transaction completed.")
    return wrapper

def hello():
    print("...Executing all steps of Transaction...")

# Applying the decorator to the hello function
decorated_hello=decorator(hello)
decorated_hello()
