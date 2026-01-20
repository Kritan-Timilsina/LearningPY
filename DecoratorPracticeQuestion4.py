# Write a Python decorator called track_calls that does the following:

# Counts how many times the decorated function has been called.

# Prints “Call X of <function_name>” before running the function.

# Prints the arguments passed to the function.

# Modifies the return value of the function by multiplying it by 2.

# Works for any function with arguments (*args and **kwargs).

# Uses @ decorator syntax.
def track_calls(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        result=func(*args,**kwargs)
        count+=1
        print(f"Call {count} of {func.__name__}")
        if result is not None:
            return result * 2
    return wrapper


@track_calls
def person(*args,**kwargs):
    print("The given arguments are:")
    for i in args:
        print(i)
    print("The given Keyword Arguments are:")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    

person ("Kritan",21, Address="Baneshwor",Uni="Pokhara")
person ("Aarjan",21, Address="Mulpani",Uni="Pokhara")
