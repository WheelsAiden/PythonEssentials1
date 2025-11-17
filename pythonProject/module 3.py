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

print()

# Print the result.
print("The largest number is:", largest_number)

plant = input("Enter plant name: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not " + plant + "!")

print()

income = float(input("Enter the annual income: "))
if income <= 85528:
    tax = (income * 0.18) - 556.02
else:
    tax = 14839.02 + ((income - 85528) * 0.32)
if tax < 0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")

print()

# Tax calculator function
def calculate_tax(income):
    if income <= 85528:
        tax = (income * 0.18) - 556.02
    else:
        tax = 14839.02 + ((income - 85528) * 0.32)
    if tax < 0:
        tax = 0.0
    return round(tax, 0)

# Test data
test_incomes = [10000, 100000, 1000, -100]

# Run tests
for income in test_incomes:
    tax = calculate_tax(income)
    print(f"Income: {income} → The tax is: {tax} thalers")
"""
print("Wheels Aiden - Testing - 11/17/2025")

print()

year = int(input())

# Check if within Gregorian calendar
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")

x = 10

if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.")

x = 10

if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.

if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.

if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.

x = 10

if x < 10:  # Condition
    print("x is less than 10")  # Executed if the condition is True.

else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.

x = 10

if x > 5:  # True
    print("x > 5")

if x > 8:  # True
    print("x > 8")

if x > 10:  # False
    print("x > 10")

else:
    print("else will be executed")

x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")

x = 10

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")

print()

x = 5
y = 10
z = 8

print(x > y)
print(y > z)

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

print()

while True:
    print("I'm stuck inside a loop.")

print()

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)

print()

# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

