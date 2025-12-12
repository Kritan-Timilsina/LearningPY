class Employee:
    compName="ap"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def setCompName(cls,cName):
        cls.compName=cName

Employee.setCompName("Hello")
print(Employee.compName)
e=Employee("Kritan",20)
print(e.compName)