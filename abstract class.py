from abc import ABC, abstractmethod
class Polygon(ABC):
    def __init__(self,color):
        self.color=color
    @abstractmethod
    def printSides(self):
        pass

class Triangle(Polygon):
    def __init__(self,color):
        super().__init__(color)
    def printSides(self):
        print("There are three Sides")
p=Triangle("RED")
p.printSides()