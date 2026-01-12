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