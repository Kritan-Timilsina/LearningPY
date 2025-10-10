def printItem(id,name,price):
    print(f"Id is {id}")
    print(f"name is :{name}")
    print(f"price is :{price}rs")

printItem(101,"Soap",200)#positional argument
print()
printItem(id=202,name="Liquid soap",price=500)#keyword argument

