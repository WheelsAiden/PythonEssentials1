"""
from idlelib.configdialog import VarTrace

print("Aiden Walker - 10/30/25")
print ()
print("Aiden is the best student of the class. I work very hard everyday and I love my 3rd block.")

print()

print("Aiden Walker - 10/30/25")
print()

# Question 1
print(2 == 2)

# Question 2
print(2 == 2.0)

# Question 3
print(1 == 2)

# Making my own questions
print(100==50)

print(100==100)

print()

print("Aiden Walker - 11/3/25")

print()

print("var == 0")
print()

print("black_sheep == 2 * white_sheep")
print()

print("black_sheep == (2 * white_sheep")
print()

print("var = 0  # Assigning 0 to var")
print("var == 0")

print("var = 1  # Assigning 1 to var")
print("var == 0")

print()

v = 0
a = 0

print("v + a =", v + a)

print()

print("True ✅ → means the statement is correct.")
print("False ❌ → means the statement is not correct.")

print()

print("EASY — basic comparisons")
print(5 > 3)
print(2 < 7)
print(10 == 10)
print(4 != 4)

print()

print("MEDIUM — using >= and <=")
print(5 >= 5)
print(6 >= 2)
print(3 <= 3)
print(9 <= 4)

print()

print("HARDER — saving results and using logic")
# Store the result of a comparison
answer = 10 > 5
print(answer)

# Compare two variables
black_sheep = 7
white_sheep = 5
print(black_sheep > white_sheep)

print()

print("HARDEST — use in a decision (if-else)")
temperature = 30

if temperature >= 25:
    print("It’s warm outside!")
else:
    print("It’s cold outside!")

print()

print("BONUS — mixed with math")
print(2 + 3 * 4 > 10)
print((2 + 3) * 4 > 10)

print("Aiden Walker - 11/4/25")

print()

n = int(input())
print(n >= 100)

print()

print("Input\tOutput")
print("55\t", 55 >= 100)
print("99\t", 99 >= 100)
print("100\t", 100 >= 100)
print("101\t", 101 >= 100)
print("-5\t", -5 >= 100)
print("+123\t", +123 >= 100)

print()

print("Aiden Walker - 11/5/25")

print()

print("No coding yet — I’m just reviewing if, elif, else statements. Back when I was a freshman, I learned about them and even made a repo for it, but I can’t access it now because my school’s blocking system won’t let me.")

print()
"""
print("Aiden Walker - 11/6/25")

print()

print("Example 1")
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

print()

print("Example 2")
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

print()

print("Example 3")
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

print()

largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

print()

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

plant = input("Enter plant name: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant + "!")
