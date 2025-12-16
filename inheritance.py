class Person:
    def __init__(self,id,name):
        self.id=id
        self.name=name 
class Employee(Person):
        def __init__(self,id,name,salary):
            super().__init__(id,name)
            self.salary=salary
        def printDetails(self):
            print(self.id)
            print(self.name)
            print(self.salary)
e=Employee(101,"Kritan",700000)
e.printDetails()

In Python, super() is used to call a method from a parent (base) class inside a child (derived) class.
# It is most commonly used to access the parent class’s constructor (__init__) or overridden methods.