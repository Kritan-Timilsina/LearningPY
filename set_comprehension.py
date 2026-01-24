numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
# Use set comprehension to create a set of squares of all numbers.
square={x**2 for x in numbers}
print(square)
# Use set comprehension to create a set of only even numbers.
even_numbers={x  for x in numbers if x%2==0}
print(even_numbers)


# Use set comprehension to create a set of “Even” or “Odd” strings for all numbers

Even_or_Odd={"Even"if x%2==0 else "odd" for x in numbers}
print(Even_or_Odd)