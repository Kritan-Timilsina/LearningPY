#program to learn dictionary in python
print("Keys should written as string i.e inside \" \" ")
"""syntax 
dictionary variable={
"Key":value,"key2:",value
}"""
Citizen={
"Name":"Kritan","Address":"Baneshwor","Age":20,"Weight":75
}
print(Citizen)
print("Name:",Citizen ["Name"])
Citizen["College"]="NEC"
print(Citizen)
Citizen["Weight"]=80
print(Citizen) #Modifing value of key 
del Citizen["Weight"]
print(Citizen)