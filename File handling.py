f=open ("MyData.txt",'r')
print(f.readline(),end="")
print(f.readline())
print(f.readline(4))# this only prints 4 letters from line 

f1=open("writingfile.txt",'w')
f1.write("This is first time when i am inserting in file ")

f2=open("writingfile.txt",'a')
f2.write("Laptop")
f.seek(0)# yo line le chai garera pheri file ko starting position ma gayo 
for data in f:
    print(data)
position=f.tell()# tell le chai kun byte ma cha tyo bhancha 
print(position)
f.close()
f1.close()
f2.close()
