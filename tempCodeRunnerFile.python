class Employee:
    def __init__(self,eid,salary):
        self.eid=eid
        self.salary=salary

    def display(self):
        print(f"eid:{self.eid}\nsalary:{self.salary}")

class Manager(Employee):
    def __init__(self,eid,salary,bonus):
        super().__init__(eid,salary)
        self.bonus=bonus
    def display(self):
        print(f"eid:{self.eid}\nsalary:{self.salary}\nbonus:{self.bonus}")
p1=Manager(101,50000,3000)
p1.display()
