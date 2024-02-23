# Example of Python Conditionals

# Numeric Comparison
x = 10
if x > 5:
    print("Numeric Comparison: x is greater than 5")
elif x == 5:
    print("Numeric Comparison: x is equal to 5")
else:
    print("Numeric Comparison: x is less than 5")

# String Comparison
word = "Python"
if len(word) > 6:
    print("String Comparison: Length of word is greater than 6")
else:
    print("String Comparison: Length of word is not greater than 6")

# List and Membership Check
fruits = ['apple', 'banana', 'orange']
fruit_to_check = 'banana'
if fruit_to_check in fruits:
    print(f"List and Membership Check: {fruit_to_check} is in the list")
else:
    print(f"List and Membership Check: {fruit_to_check} is not in the list")

# Ternary Operator
y = 7
message = "Ternary Operator: y is greater than 5" if y > 5 else "Ternary Operator: y is not greater than 5"
print(message)

# Nested Conditionals
num = 20
if num > 10:
    if num % 2 == 0:
        print("Nested Conditionals: num is greater than 10 and even")
    else:
        print("Nested Conditionals: num is greater than 10 but not even")
else:
    print("Nested Conditionals: num is not greater than 10")

# Logical Operators
a = 15
b = 25
if a > 10 and b < 30:
    print("Logical Operators: Both conditions are true")

# Complex Conditions
grade = 85
if grade >= 90:
    print("Complex Conditions: A")
elif 80 <= grade < 90:
    print("Complex Conditions: B")
elif 70 <= grade < 80:
    print("Complex Conditions: C")
else:
    print("Complex Conditions: Below C")

# Conditional with Lists
numbers = [1, 2, 3, 4, 5]
if len(numbers) > 3 and 3 in numbers:
    print("Conditional with Lists: List has more than 3 elements and contains 3")

# Using `not` keyword
flag = False
if not flag:
    print("Using `not` keyword: flag is False")


value = 42
if value > 50:
    print("Value is greater than 50")
elif value > 30:
    print("Value is greater than 30")
elif value > 20:
    print("Value is greater than 20")
else:
    print("Value is 20 or less")
