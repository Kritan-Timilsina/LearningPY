list1 = [10, 20, 30, 40, 50, 20, 10]  
list2 = [30, 40, 50, 60, 70, 50]  

# Write a program (using sets) to:
# Find all unique numbers in both lists combined
s1=set(list1)
print(f"Unique number in list 1:{s1}")
s2=set(list2)
print(f"Unique number in list 2:{s2}")
combined=s1|s2
print(f"All unique number in both list: {sorted(combined)}")
# Find numbers common to both lists

print(f"Numbers common in both:{s1&s2}")



# Find numbers only in list1 but not in list2
print(f"Number only in set 1 not in 2:{s1-s2}")
# Find numbers only in list2 but not in list1
print(f"Number only in set 2 not in 1:{s2-s1}")
# Bonus: Sort the results before printing.
