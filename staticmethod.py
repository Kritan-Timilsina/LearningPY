class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @staticmethod
    def isAdult(age):
        return (age>18)
    def printDetails(self):
        print(self.name)
        print(self.age)
        print(Person.isAdult(self.age))
p=Person("Kritan",21)
p.printDetails()
print(Person.isAdult(21))