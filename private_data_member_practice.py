class HiddenData:
    def __init__(self,x,hidden):
        self.x=x
        self.__hidden=hidden

    def Display(self):
        print(self.x)
        print(self.__hidden)
Hd=HiddenData(2,5)
#print(Hd.__hidden)
Hd.Display()