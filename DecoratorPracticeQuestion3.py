# Write a Python decorator called logger that does the following:

# Prints “Function <function_name> is about to run” before the function runs

# Prints “Function <function_name> finished execution” after the function runs

# Works for any function with arguments (*args and **kwargs)

# Prints the arguments passed to the function before it runs

def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Function {func.__name__} is about to run")
        func(*args,**kwargs)
        print(f"Function {func.__name__} finished execution")
    return wrapper

@logger
def greet(task,*args):
    print(f"{task} is running")

greet("Cleaning")