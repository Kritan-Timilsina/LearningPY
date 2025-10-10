def printDetails(**details):# it creates dictionary 
    for d,v in details.items():
        print(f"{d} is {v}")
printDetails(id=101,name="abc",price=100)