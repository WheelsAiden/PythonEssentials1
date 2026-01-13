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
    """
    Prints a greeting with a person's name.

    Parameters:
    - first_name: str, person's first name
    - last_name: str, person's last name
    - culture: str, name order convention ("Western" or "Hungarian")
    """
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
