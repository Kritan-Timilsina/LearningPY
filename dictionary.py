dict={
    "Kritan":"Handsome","Timilsina":"Cool"
}
print(dict)
dict["Hero"]="Kritan"
print(dict)
print(dict["Kritan"])
print(dict.get("Kritan"))#Get function le chai khojeko chaina bhani return ma None dincha 
print(dict.get("beautiful","Notpresent"))#syntax to print if key is not present