from datetime import date
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def getFromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)
e=Employee.getFromBirthYear("Kritan",2004)
print(e.name)
print(e.age)
    