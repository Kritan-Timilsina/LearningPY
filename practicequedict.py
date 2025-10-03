"""Create a dictionary called student with these keys and values:

"Name" → your name

"Age" → your age

"Grade" → your grade

Tasks:
a. Print the whole dictionary.
b. Print only the student’s "Name".
c. Add a new key "School" with any value.
d. Update the "Age" to your next year’s age.
e. Remove the "Grade" key.
f. Print the final dictionary."""
Student={
  "Name":"Kritan Timilsina","Age":20,"Grade":13
}
print(Student)
print("Name:",Student["Name"])
Student["School"]="NEC"
Student["Age"]=21
del Student["Grade"]
print(Student)