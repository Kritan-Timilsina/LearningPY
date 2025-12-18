"""Question

Create a Python program using inheritance as follows:

1. Base Class: Person

Attributes:

name (string)

age (int)

Constructor:

Initializes name and age

Method:

display() → prints the name and age

2. Derived Class: Student (inherits from Person)

Additional attribute:

roll_no (int)

Constructor:

Takes name, age, and roll_no

Uses super() to initialize name and age

Method:

display_student() → prints name, age, and roll number

3. Create an object of Student

Call both:

display()

display_student()"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"Name:{self.name} \n Age:{self.age}")

class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
    
    def display_student(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("Roll no:",self.roll_no)
s=Student("Kritan",21,20)
s.display()
s.display_student()