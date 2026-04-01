"""Today’s Program: Number Frequency Analyzer
🧠 Task

Write a program that:

Takes a list of integers (you can define it directly).
Creates a dictionary to count how many times each number appears.
Prints:
Frequency of each number
The most frequent number
The least frequent number"""
l=[10,20,10,22,55,88,22,67,100,20,10,18]


d={}

for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for key,values in d.items():
    print(f"{key}:{values}")

max_freq=max(d.values())

min_freq=min(d.values())


for key in d:
    if d[key]==max_freq:
        print(f"Most frequent is {key}")
    if d[key]==min_freq:
        print(f"Least repeated is {key}")
        
