class Father:
    def __init__(self,fname):
         self.fname=fname
    def display_father(self):
         print(self.fname)

class Mother:
    def __init__(self,mname):
          self.mname=mname
    def display_mother(self):
         print(self.mname)

class Child(Father,Mother):
     def __init__(self,fname,mname,child_name):
          Father.__init__(self,fname)
          Mother.__init__(self,mname)
          self.child_name=child_name
    
     def display(self):
        self.display_father()
        self.display_mother()
        print(self.child_name)
c1=Child('Krishna','Kriti','Kritan')
c1.display()