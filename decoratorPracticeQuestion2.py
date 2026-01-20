"""Write a Python decorator called repeat_twice that does the following:

Executes the decorated function two times

Works for any function with no arguments

Uses @ decorator syntax"""

def repeat_twice(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper

@repeat_twice
def greet():
    print("Hello")

greet()