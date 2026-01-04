f=open ("MyData.txt",'r')
print(f.readline(),end="")
print(f.readline())
print(f.readline())# this only prints 4 letters from line 

f1=open("writingfile.txt",'w')
f1.write("This is first time when i am inserting in file ")

f2=open("writingfile.txt",'a')
f2.write("Laptop")
for data in f:
    print(data)