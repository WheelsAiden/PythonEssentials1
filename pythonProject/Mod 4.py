"""
print("Aiden Walker - 1/12/26")

print()

def enter_value():
    print("Please, enter a value: ")
    return int(input())

a = enter_value()
b = enter_value()
c = enter_value()

print()

def message():
    print("Enter a value: ")

def my_function():
    print("Hello, this is my function!")

print("We start here.")
message()
my_function()
print("We end here.")

print()

# How functions work in Python

# A function is a block of code that runs only when it is called.
# Python reads code from top to bottom.

# If Python reaches a function call before seeing the function definition,
# it will cause an error.

# WRONG example (function defined AFTER it is called):
# print("We start here.")
# message()
# print("We end here.")
#
# def message():
#     print("Enter a value: ")
#
# This causes:
# NameError: name 'message' is not defined


# Correct example — function is defined BEFORE it is called
def message():
    print("Enter a value: ")


print("We start here.")

# Calling the function
message()

print("We end here.")


# You must not use the same name for a function and a variable
# WRONG example:
# message = 1
# This would overwrite the function name


# Using the function for repeated tasks
message()
a = int(input())

message()
b = int(input())

message()
c = int(input())


# The benefit:
# If you want to change the prompt message,
# you only need to change it in ONE place — inside the function

print()

# Functions in Python

# A function is a block of code that performs a specific task when called.
# Functions make code reusable, organized, and easier to read.
# Functions can have parameters and can return values.

# Types of functions:
# 1. Built-in functions (like print() and input())
# 2. Functions from pre-installed modules (imported)
# 3. User-defined functions (created by the programmer)
# 4. Lambda functions (short anonymous functions)

# Defining a function without parameters
def message():
    print("Hello")

message()  # Calling the function

# Defining a function with parameters
def hello(name):
    print("Hello,", name)

name = input("Enter your name: ")
hello(name)  # Calling the function with an argument

# Exercises and Answers

# Exercise 1: The input() function is a built-in function.

# Exercise 2: Calling a function before defining it causes an error
# hi()  # Uncommenting this line would cause NameError
def hi():
    print("hi!")

# Exercise 3: Passing the wrong number of arguments causes an error
# hi(5)  # Uncommenting this line would cause TypeError
hi()  # Correct call with no arguments

# Key Rules:
# 1. Always define a function before calling it.
# 2. Make sure the number of arguments matches the function's parameters.

print()

# Parameterized function example

# Step 1: Define the function with a parameter
def message(number):
    # 'number' is a parameter — it exists only inside this function
    print("Enter a number:", number)

# Step 2: Call the function with an argument
# The argument is the actual value we pass to the parameter
message(5)   # Output: Enter a number: 5
message(10)  # Output: Enter a number: 10

# Notes:
# 1. Parameters live inside the function; arguments come from outside.
# 2. The number of arguments must match the number of parameters.
#    Forgetting an argument or giving extra will cause an error.
# 3. Parameters are like mailboxes; arguments are the mail you put in them.

print()

# Function with a required parameter
def message(number=0):  # default value is 0
    print("Enter a number:", number)

# Calling the function with an argument
message(1)   # Output: Enter a number: 1

# Calling the function without an argument uses the default
message()    # Output: Enter a number: 0

# Global variable with the same name as the parameter
number = 1234

# Calling the function again
message(5)   # Output: Enter a number: 5

# Printing the global variable
print(number)  # Output: 1234

print()

# Function with two parameters
def message(what, number):
    print("Enter", what, "number", number)

# Invoking the function
message("telephone", 11)
message("price", 5)
message("number", "number")

# ---- Example: adding a third parameter ----
def message_extended(what, number, urgency):
    print("Enter", what, "number", number, "-", "Urgency:", urgency)

# Invoking the extended function
message_extended("telephone", 11, "high")
message_extended("price", 5, "low")
message_extended("appointment", 3, "medium")

print()

# Culture-independent introduction function
def introduction(first_name, last_name, culture="Western"):

    Prints a greeting with a person's name.

    Parameters:
    - first_name: str, person's first name
    - last_name: str, person's last name
    - culture: str, name order convention ("Western" or "Hungarian")

    if culture.lower() == "hungarian":
        # Hungarian style: last name first
        print("Hello, my name is", last_name, first_name)
    else:
        # Western style: first name first
        print("Hello, my name is", first_name, last_name)


# Examples using positional and keyword arguments
introduction("Luke", "Skywalker")  # Western by default
introduction("Skywalker", "Luke", culture="Hungarian")  # Hungarian
introduction(first_name="Jesse", last_name="Quick")  # Keyword arguments
introduction(last_name="Kent", first_name="Clark")  # Keyword arguments in reverse order

print()

print("Aiden Wallker - 1/13/26")

def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

# Correct keyword argument usage
introduction(first_name="James", last_name="Bond")
introduction(last_name="Skywalker", first_name="Luke")

# Incorrect keyword argument usage (will cause a TypeError)
# Uncomment to see the error
# introduction(surname="Skywalker", first_name="Luke")

print()

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# mixed positional and keyword arguments
adding(3, b=2, c=1)

print()

# Parametrized function with a default parameter

def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Function calls
introduction("James", "Doe")
introduction("Henry")
introduction(first_name="William")
introduction(last_name="Hopkins", first_name="John")

print()

# Key Takeaways – Functions & Arguments (All-in-One Code Block)

# One-parameter function
def hi(name):
    print("Hi,", name)

hi("Greg")


# Two-parameter function
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")


# Three-parameter function with input
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)


# Positional and keyword arguments
def subtra(a, b):
    print(a - b)

subtra(5, 2)          # 3
subtra(2, 5)          # -3
subtra(a=5, b=2)      # 3
subtra(b=2, a=5)      # 3
subtra(5, b=2)        # 3
# subtra(a=5, 2)      # SyntaxError (positional after keyword)


# Default parameter values
def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")                 # Andy Smith
name("Betty", "Johnson")     # Betty Johnson


# Exercise examples
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()                      # My name is Bond. James Bond.
intro(b="Sean Connery")      # My name is Sean Connery. James Bond.


def intro2(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro2("Susan")              # My name is Bond. Susan.


# Incorrect function definition (will cause SyntaxError)
# def add_numbers(a, b=2, c):
#     print(a + b + c)

# Correct function definition
def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)        # 6

print()

# Example 1: return without an expression (early exit)
def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return  # stops the function early
    print("Happy New Year!")


# Called with no arguments
happy_new_year()

print()  # blank line

# Called with False
happy_new_year(False)

print("\n-----------------\n")

# Example 2: return with an expression
def boring_function():
    return 123


x = boring_function()
print("The boring_function has returned its result. It's:", x)

print("\n-----------------\n")

# Example 3: return value is ignored
def another_boring_function():
    print("'Boredom Mode' ON.")
    return 123


print("This lesson is interesting!")
another_boring_function()  # return value is ignored
print("This lesson is boring...")

print()

# Assigning None to a variable
value = None

# Checking the variable's state
if value is None:
    print("Sorry, you don't carry any value")

# Function that doesn't explicitly return anything
def no_return():
    print("This function doesn't return anything")

# Call the function and capture its "return value"
result = no_return()
print("Returned value:", result)

# Check the type of the returned value
print("Type of returned value:", type(result))

print()

# Original strange_function
def strange_function(n):
    if n % 2 == 0:
        return True

# Testing the function
print(strange_function(2))  # Output: True
print(strange_function(1))  # Output: None

# Explanation:
# - If n is even, the function returns True.
# - If n is odd, there is no return statement executed,
#   so Python automatically returns None.

# Improved version to always return a boolean
def strange_function_fixed(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Or more succinctly
def strange_function_succinct(n):
    return n % 2 == 0

# Testing the improved functions
print(strange_function_fixed(2))      # Output: True
print(strange_function_fixed(1))      # Output: False
print(strange_function_succinct(2))   # Output: True
print(strange_function_succinct(1))   # Output: False

print()
"""
print("Aiden Walker - 1/19/2026")

print()

# Demonstrates passing a list to a function, why non-lists fail,
# and how list references work (lists are NOT copied automatically).

def list_sum(lst):
    # Safety check to avoid errors like list_sum(5)
    if not isinstance(lst, list):
        return "Error: argument must be a list"

    s = 0
    for elem in lst:
        s += elem
    return s


# Correct usage
print(list_sum([5, 4, 3]))  # Output: 12


# Incorrect usage (handled safely now)
print(list_sum(5))          # Output: Error message


# IMPORTANT: lists are passed by reference, not copied
def add_item(lst):
    lst.append(10)


nums = [1, 2, 3]
add_item(nums)
print(nums)                 # Output: [1, 2, 3, 10]


# To avoid modifying the original list, pass a copy instead
nums = [1, 2, 3]
add_item(nums.copy())       # or nums[:] or list(nums)
print(nums)                 # Output: [1, 2, 3]

print()

# A function can return a list, just like it can return any other Python object.
# This function creates a list, fills it, and returns it.

def strange_list_fun(n):
    strange_list = []  # create an empty local list

    for i in range(0, n):  # loop from 0 to n-1
        strange_list.insert(0, i)
        # insert(0, i) places i at the beginning of the list,
        # pushing existing elements to the right

    return strange_list  # return the finished list


# Calling the function with n = 5
print(strange_list_fun(5))
# Output: [4, 3, 2, 1, 0]

# Key idea:
# - Functions can return lists
# - The list is local to the function until returned
# - Assigning the returned list copies the reference, not the contents
#   (use copy(), slicing [:], or list() to make a real copy)

print()

def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print()

def is_year_leap(year):
    if year < 1582:
        return None
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    # Validate input
    if year < 1582 or month < 1 or month > 12:
        return None

    # Month lengths (February handled separately)
    month_lengths = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    # Adjust February for leap years
    if month == 2 and is_year_leap(year):
        return 29

    return month_lengths[month - 1]


# Provided tests
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")


# Additional test cases (recommended)
extra_tests = [
    (2024, 2),   # leap year
    (2023, 2),   # non-leap year
    (2023, 4),   # April
    (2023, 13),  # invalid month
    (1500, 1)    # invalid year
]

print("\nExtra tests:")
for year, month in extra_tests:
    print(year, month, "->", days_in_month(year, month))

print()

def is_year_leap(year):
    if year < 1:
        return False
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if year < 1 or month < 1 or month > 12:
        return None

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_year_leap(year):
        return 29

    return month_days[month - 1]


def day_of_year(year, month, day):
    if year < 1 or month < 1 or month > 12:
        return None

    dim = days_in_month(year, month)
    if dim is None or day < 1 or day > dim:
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)

    total_days += day
    return total_days


# Test cases
print(day_of_year(2000, 12, 31))   # 366 (leap year)
print(day_of_year(2023, 3, 1))     # 60
print(day_of_year(2021, 2, 29))    # None (invalid)
print(day_of_year(2024, 2, 29))    # 60 (leap year)
print(day_of_year(2024, 13, 1))    # None

print()

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")

print()

def liters_100km_to_miles_gallon(liters):
    return (100 * 3.785411784) / (liters * 1.609344)

def miles_gallon_to_liters_100km(miles):
    return (100 * 3.785411784) / (miles * 1.609344)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print()

# =========================
# TAKEAWAY 1: Using return
# =========================

def multiply(a, b):
    return a * b

print("Takeaway 1a:", multiply(3, 4))    # outputs: 12

def multiply_none(a, b):
    return

print("Takeaway 1b:", multiply_none(3, 4))    # outputs: None

# =========================
# TAKEAWAY 2: Assigning function result to a variable
# =========================

def wishes():
    return "Happy Birthday!"

w = wishes()
print("Takeaway 2a:", w)    # outputs: Happy Birthday!

# Difference between printing inside function vs returning
def wishes_with_print():
    print("My Wishes")
    return "Happy Birthday"

print("Takeaway 2b:")
wishes_with_print()    # prints: My Wishes (but return ignored)

print("Takeaway 2c:")
print(wishes_with_print())
# prints:
# My Wishes
# Happy Birthday

# =========================
# TAKEAWAY 3: Passing a list to a function
# =========================

def hi_everybody(my_list):
    for name in my_list:
        print("Hi,", name)

print("Takeaway 3:")
hi_everybody(["Adam", "John", "Lucy"])

# =========================
# TAKEAWAY 4: Returning a list from a function
# =========================

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print("Takeaway 4:", create_list(5))   # outputs: [0, 1, 2, 3, 4]

# =========================
# EXERCISE 1
# =========================

def hi():
    return
    print("Hi!")

print("Exercise 1:", hi())   # outputs: None (nothing is printed inside)

# =========================
# EXERCISE 2
# =========================

def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print("Exercise 2a:", is_int(5))     # True
print("Exercise 2b:", is_int(5.0))   # False
print("Exercise 2c:", is_int("5"))   # None

# =========================
# EXERCISE 3
# =========================

def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print("Exercise 3:", even_num_lst(11))  # [0, 2, 4, 6, 8, 10]

# =========================
# EXERCISE 4
# =========================

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print("Exercise 4:", list_updater(foo))  # [1, 4, 9, 16, 25]

print("Aiden Walker - 1/20/2026")

print()

# Example 1: This will raise an error because x is local to the function
def scope_test():
    x = 123

scope_test()

# x does NOT exist outside the function
# This line will cause:
# NameError: name 'x' is not defined
# print(x)


# --------------------------------------------------


# Example 2: Correct way — return the value from the function
def scope_test_fixed():
    x = 123
    return x

value = scope_test_fixed()
print(value)   # Output: 123

print()

# Example 1: Reading a global variable inside a function

def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)


# Example 2: Local variable shadows the global one

def my_function():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function()
print(var)


# Example 3: Assignment makes the variable local (this will raise an error)

def my_function():
    var += 1      # Python treats var as local because of assignment
    print(var)

var = 10
my_function()    # UnboundLocalError

print()

# Example demonstrating the global keyword in Python

def my_function():
    # Tell Python: use the global variable 'var', not a new local one
    global var
    var = 2  # modifies the global variable
    print("Do I know that variable?", var)  # prints 2

# Create a global variable
var = 1
print("Before function call, var =", var)  # prints 1

# Call the function, which modifies the global variable
my_function()  # prints: Do I know that variable? 2

# Check the value of var after the function call
print("After function call, var =", var)  # prints 2

# -------------------------------------------------------------------
# Key points:
# 1. Normally, assigning inside a function creates a local variable.
# 2. Using 'global var' tells Python to use the variable from the global scope.
# 3. Reading a global variable does NOT require 'global'.
# 4. Best practice: prefer returning values instead of modifying globals directly.
# -------------------------------------------------------------------

print()

# Example 1: Scalars / Immutable types
def my_function_scalar(n):
    print("I got", n)
    n += 1
    print("I have", n)

var = 1
my_function_scalar(var)
print("Outside function (scalar):", var)
print("------")

# Example 2: Lists / Mutable types - reassigning parameter
def my_function_reassign(my_list_1):
    print("Print #1:", my_list_1)
    my_list_1 = [0, 1]  # Reassign the parameter
    print("Print #2:", my_list_1)

my_list_2 = [2, 3]
my_function_reassign(my_list_2)
print("Outside function after reassignment:", my_list_2)
print("------")

# Example 3: Lists / Mutable types - modifying the list in place
def my_function_modify(my_list_1):
    print("Print #1:", my_list_1)
    del my_list_1[0]  # Modify the list object itself
    print("Print #2:", my_list_1)

my_list_2 = [2, 3]
my_function_modify(my_list_2)
print("Outside function after in-place modification:", my_list_2)

print()

# Exercise 1
def message():
    alt = 1
    print("Hello, World!")

# print(alt)  # NameError: name 'alt' is not defined

# --------------------------------------------------

# Exercise 2
a = 1

def fun2():
    a = 2   # local variable
    print(a)

fun2()      # prints 2
print(a)    # prints 1 (global 'a' unchanged)

# --------------------------------------------------

# Exercise 3
a = 1

def fun3():
    global a
    a = 2   # modifies global 'a'
    print(a)

fun3()      # prints 2
a = 3       # modifies global 'a' again
print(a)    # prints 3

# --------------------------------------------------

# Exercise 4
a = 1

def fun4():
    global a
    a = 2   # modifies global 'a'
    print(a)

a = 3       # global 'a' is now 3
fun4()      # prints 2
print(a)    # prints 2 (global 'a' was changed by fun4)
