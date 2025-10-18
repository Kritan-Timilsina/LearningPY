class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def print(self):
        print(str(self.real)+"+i" +str(self.img))
    
    def add(self,c):
        self.real+=c.real
        self.img+=c.img
c1=complex(10,20)
c2=complex(32,11)
c1.add(c2)
c1.print()
