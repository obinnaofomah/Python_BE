"""
Different Types of Loops:
1. For loop
2. While Loop
3. Nested Loops
4. Break statements
5. continue statements
6. else statements
"""

fruits = ['apple', 'banana', 'orange']
len(fruits) # size or length of the array
for fruit in fruits:
    print(fruit)


# Keeps increasing a value till it gets to a maximum value which is 5
count = 0
while count < 5:
    print(count)
    count += 1

# for every increase in range(3) theres a double print in the range(2)
for i in range(3):
    for j in range(2):
        print(i, j)


# provide explanations of how the remaining 3 loop types act in the examples below.
for i in range(5):
    if i == 3:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)


for i in range(5):
    print(i)
else:
    print("Loop completed")



# First Home_work
    def printStudentNames(students):
        """Using one of the loop statements stated above. Write a function logic that prints each students 
        
        students = ["Mark", "Kingsley", "Jacob", "Augustine", "Rita", "Precious", "Sarah", "Philip", "Treasure", "Matthew", "Jesus", "Aguero", "Ronaldo", "Lopez"]
        """

    def primeNumbers():
        """
        Write a function that prints all prime number up to 100.
        
        Hint: Use the loop statement to loop through the range(100) and write the mathematical condition for prime numbers to just print if that condition is true

        returns 
        -------
        null
        """

    def evenNumbers():
        """
        Do the same using one of the loop functions above to write a function to prints all even numbers up to 1000.

        Hint: An even number is one divisible by 2: Condition n % 2 == 0
        returns
        ----------
        null
        """

    