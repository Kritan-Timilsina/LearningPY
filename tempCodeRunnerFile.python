class Academic:
    def __init__(self,marks):
        self.marks=marks
    
    def display_academic(self):
        print(self.marks)

class Sports:
    def __init__(self,score):
        self.score=score
    def display_sports(self):
        print(self.score)

class Student(Academic,Sports):
    def __init__(self,marks,score):
        Academic.__init__(self,marks)
        Sports.__init__(self,score)

    def display(self):
        self.display_academic()
        self.display_sports()

s1=Student(1000,100)
s1.display()