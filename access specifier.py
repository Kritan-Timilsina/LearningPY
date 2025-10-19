""" if we have _ before variable name it suggests user to not use it outside of class but it does not display error when used but when we use _ _ before varibale name it is converted into private data type we can only access it by _class name. _ _ variable name"""
class Test:
    def __init__(self,x):
        self.x=x
        self.__y=10
    def printTest(self):
        print(self.x)
        print(self.__y)# it works since it is used inside class
t=Test(5)
t.printTest()
# print(t.__y) this does not work since it is used outside class

