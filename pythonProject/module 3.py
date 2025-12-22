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

print("Wheels Aiden - Testing - 11/17/2025-11/18/25")

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

print()

counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

print()

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

print()

secret_number = 777

print("

+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
")

guess = int(input("Enter your guess: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Try again: "))

print()

print("Well done, muggle! You are free now.")

print()

i = 0
while i < 100:
    # do_something()
    i += 1

print()

for i in range(100):
    # do_something()
    pass

print()

for i in range(10):
    print("The value of i is currently", i)

print()

for i in range(2, 8):
    print("The value of i is currently", i)

print()

print("Aiden Walker - 11/24/2025")

print()

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2

print()

for i in range(1, 6):
    print(i, "Mississippi")

print()

Ready or not, here I come!

import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

print("Ready or not, here I come!")

print()

print("Aiden Walker - 12/2/2025")

print()

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

print()

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

print()

print("Version 1 - Using break")
largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

print()

print("verison 2 - Using Continue")
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    counter += 1
    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

print()

while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

print()

# Prompt the user to enter a word
user_word = input("Enter a word: ")

# Convert the word to upper case
user_word = user_word.upper()

for letter in user_word:
    if letter in ("A", "E", "I", "O", "U"):
        continue
    print(letter)

print()

print("Aiden Walker - 12/8/2025")

print()

word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the loop.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)

print()

#origin
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print()

#Modifyed
i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print()

#1st part
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

print()

#2nd part
for i in range(5):
    print(i)
else:
    print("else:", i)

print()

blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("The height of the pyramid:", height)

print()

c0 = int(input())

steps = 0

while c0 != 1:
    if c0 % 2 == 0:      # even
        c0 = c0 // 2
    else:                # odd
        c0 = 3 * c0 + 1

    print(c0)
    steps += 1

print("steps =", steps)

print()
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")

text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")

n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

print()

for i in range(1, 11):
    # Line of code.
        # Line of code.

    x = 1
    while x < 11:
# Line of code.
# Line of code.

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
# Line of code.
# Line of code.

for digit in "0165031806510":
    if digit == "0":
# Line of code.
# Line of code.
# Line of code.

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

for i in range(0, 6, 3):
    print(i)

print()

# Example 1:
print(var > 0)
print(not (var <= 0))


# Example 2:
print(var != 0)
print(not (var == 0))

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

i = 1
j = not not i

print()

i = 15
j = 22

log = i and j

bit = i & j

logneg = not i

print()

flag_register = 0x1234

flag_register = 0000000000000000000000000000x000

x & 1 = x
x & 0 = 0

the_mask = 8

if flag_register & the_mask:
    # My bit is set.
else:
    # My bit is reset.

    flag_register = flag_register & ~the_mask
    flag_register &= ~the_mask

x | 1 = 1
x | 0 = x

flag_register = flag_register | the_mask
flag_register |= the_mask

x ^ 1 = ~x
x ^ 0 = x

flag_register = flag_register ^ the_mask
flag_register ^= the_mask

print()

17 → 10001 (binary)

10001 >> 1 → 1000

17 >> 1  → 17 // 2  → 8

10001 << 2 → 1000100

17 << 2 → 17 * 4 → 68

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

print()

print("Aiden Walker - 12/11/25")

print()

# -----------------------------
# Exercise 1
# -----------------------------
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print("Exercise 1 Output:", not(z))


# -----------------------------
# Exercise 2
# -----------------------------
x = 4
y = 1

a = x & y
b = x | y
c = ~x      # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print("Exercise 2 Outputs:", a, b, c, d, e, f)

print()

# Starting list
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)

# 1. Change the first element (index 0) to 111
numbers[0] = 111
print("After changing first element:", numbers)

# 2. Copy the value of the fifth element (index 4) to the second element (index 1)
numbers[1] = numbers[4]
print("After copying 5th element to 2nd:", numbers)

# 3. Final display
print("Final list content:", numbers)
"""

print("Aiden Walker - 12/22/25"")

print()

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList length:", len(numbers))  # Printing the list's length.

print()

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###

print()

numbers = [111, 7, 2, 1]
print(numbers[-1])
print(numbers[-2])

print()

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: replace the middle number with an integer entered by the user
hat_list[2] = int(input("Enter a number: "))

# Step 2: remove the last element from the list
hat_list.pop()

# Step 3: print the length of the existing list
print(len(hat_list))

print(hat_list)

print()

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

numbers.append(4)
print(len(numbers))
print(numbers)

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

print()

#Code with Insert
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

print()

#Code with append
my_list = []

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print()

#Version 1: Using indices with range() and len()
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

print()

#Version 2: Looping directly through the list (preferred)
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

print()

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

print()

my_list = [10, 1, 8, 3, 5]  # you can replace these numbers with any list
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
