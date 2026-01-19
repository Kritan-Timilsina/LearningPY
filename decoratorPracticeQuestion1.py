"""

🧠 Decorator Practice Question

Question:

Write a Python decorator called log_execution that does the following:

Prints "Function started" before the function runs

Prints "Function ended" after the function runs

Works for any function with no arguments"""
def log_execution(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function ended")
    return wrapper

@log_execution
def process_data():
    print("---Processing Data----")
    

process_data()