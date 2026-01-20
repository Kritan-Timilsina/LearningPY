# Write a Python decorator called execution_timer that does the following:

# Prints “Executing <function_name>...” before the function runs.

# Measures the time taken by the function to execute.

# Prints “Execution of <function_name> took X.XXX seconds” after the function finishes.

# Works for any function with arguments (*args and **kwargs).

# Returns the original function’s return value unchanged.

# Uses @ decorator syntax.
import time

def execution_timer(func):
    def wrapper(*args,**kwargs):
        print(f"Executing {func.__name__}")
        initialtime=time.time()
        result=func(*args,**kwargs)
        finaltime=time.time()
        totaltime=finaltime-initialtime
        print(f"Time required for execution is :{totaltime} seconds")
        print(f"Execution of {func.__name__} completed")
        if result is not None:
            return result
    return wrapper

@execution_timer
def Name(Name,*args,**kwargs):
    print(f"{Name} executed this program")

Name("Kritan")
