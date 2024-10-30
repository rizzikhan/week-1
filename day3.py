# functions.py

# Day 3 – Functions

# Functions:
# A Python function is a block of organized, reusable code that performs a single, related action.
# Functions provide better modularity for applications and a high degree of code reusability.

# Types of Python Functions:
# 1. Built-in functions: Standard functions available in Python (e.g., print(), len(), etc.).
# 2. Functions defined in built-in modules: Functions available after importing specific modules.
# 3. User-defined functions: Functions created by the user for specific tasks.

# Defining a Python Function:
# Function blocks begin with the keyword 'def' followed by the function name and parentheses.
# The first statement can be a docstring, followed by an indented code block.
# The return statement exits a function, optionally passing back an expression to the caller.

def greetings():
    """This is the docstring of the greetings function."""
    print("Hello World")
    return

# Function definition is here
def printme(str):
    """This prints a passed string into this function."""
    print(str)
    return

# Calling the function
printme("I'm first call to user-defined function!")
printme("Again second call to the same function.")

# Call by Value vs. Call by Reference
def testfunction(arg):
    """Demonstrates call by value."""
    print("ID inside the function:", id(arg))
    arg = arg + 1
    print("New object after increment:", arg, id(arg))

var = 10
print("ID before passing:", id(var))
testfunction(var)
print("Value after function call:", var)

def testfunction_ref(arg):
    """Demonstrates call by reference."""
    print("Inside function:", arg)
    print("ID inside the function:", id(arg))
    arg.append(100)  # Modifies the list in place

var = [10, 20, 30, 40]
print("ID before passing:", id(var))
testfunction_ref(var)
print("List after function call:", var)

# Types of Python Function Arguments:
# 1. Positional or Required Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Positional-only Arguments (Introduced in Python 3.8)
# 5. Keyword-only Arguments
# 6. Arbitrary or Variable-length Arguments

# Positional Arguments
def printme_positional(str):
    """This prints a passed string into this function."""
    print(str)

# Uncommenting the next line will raise a TypeError
# printme_positional()

# Keyword Arguments
def printinfo(name, age):
    """This prints passed information into this function."""
    print("Name:", name)
    print("Age:", age)

printinfo(age=50, name="Miki")

# Default Arguments
def printinfo_default(name, age=35):
    """This prints passed information into this function."""
    print("Name:", name)
    print("Age:", age)

printinfo_default(age=50, name="Miki")
printinfo_default(name="Miki")  # Uses default age

# Positional-only Arguments
def posFun(x, y, /, z):
    """Function that accepts positional-only arguments."""
    print(x + y + z)

print("Evaluating positional-only arguments:")
posFun(33, 22, z=11)

# Keyword-only Arguments
def posFun_kw(*, num1, num2, num3):
    """Function that accepts keyword-only arguments."""
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments:")
posFun_kw(num1=6, num2=8, num3=5)

# Difference between Positional and Keyword Arguments:
# Positional arguments are passed in the order defined in the function declaration.
# Keyword arguments can be passed in any order, identified by parameter names.

# Arbitrary or Variable-length Arguments
def printinfo_var(arg1, *vartuple):
    """This prints variable passed arguments."""
    print("Output is:")
    print(arg1)
    for var in vartuple:
        print(var)

printinfo_var(10)
printinfo_var(70, 60, 50)

# Sum of numbers with arbitrary arguments
def add(*args):
    """Function to sum any number of arguments."""
    s = 0
    for x in args:
        s += x
    return s

result = add(10, 20, 30, 40)
print("Sum:", result)

result = add(1, 2, 3)
print("Sum:", result)

# Arbitrary Keyword Arguments
def addr(**kwargs):
    """Function that accepts arbitrary keyword arguments."""
    for k, v in kwargs.items():
        print("{}: {}".format(k, v))

print("Pass two keyword args:")
addr(Name="John", City="Mumbai")
print("Pass four keyword args:")
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")

# Function with mixed arguments
def percent(math, sci, **optional):
    """Calculates percentage based on provided scores."""
    print("Maths:", math)
    print("Science:", sci)
    total = math + sci
    for k, v in optional.items():
        print("{}: {}".format(k, v))
        total += v
    return total / (len(optional) + 2)

result = percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print("Percentage:", result)


# Order of Python Function Arguments
# In Python, when defining a function, the order of the arguments is crucial. 
# The arguments should be declared in the following sequence:
# 1. Positional-only arguments: Defined before a '/' in the parameter list.
# 2. Positional or keyword arguments: Can be called as either positional or keyword arguments.
# 3. Default arguments: These have default values assigned.
# 4. Arbitrary positional arguments: Prefixed with a single asterisk ('*') and treated as a tuple.
# 5. Keyword-only arguments: Placed after an asterisk ('*'), which means they can only be passed as keyword arguments.
# 6. Arbitrary keyword arguments: Prefixed with double asterisks ('**'), treated as a dictionary.

def func(pos_only, /, pos_or_kw, *, kw_only1='default', kw_only2='default', **kwargs):
    print(f"Positional-only: {pos_only}")
    print(f"Positional or Keyword: {pos_or_kw}")
    print(f"Keyword-only argument 1: {kw_only1}")
    print(f"Keyword-only argument 2: {kw_only2}")
    print(f"Additional Keyword arguments: {kwargs}")

# Calling the function
func(10, 20, kw_only2='new_value', extra='extra_value')


# The Anonymous Functions
# Anonymous functions in Python are defined using the 'lambda' keyword. 
# Unlike normal functions declared with 'def', lambda functions are limited to a single expression.
# Key characteristics:
# - Can take any number of arguments but can only return one value.
# - They do not support multiple expressions or commands.

# Defining a lambda function for summation
sum_lambda = lambda arg1, arg2: arg1 + arg2

# Calling the lambda function
print("Value of total (lambda):", sum_lambda(10, 20))
print("Value of total (lambda):", sum_lambda(20, 20))


# Scope of Variables
# The scope of a variable refers to the region of the program where it is accessible. 
# Python has three main scopes:
# - Local Variables: Variables defined within a function.
# - Global Variables: Variables defined outside of all functions.
# - Nonlocal Variables: Variables defined in the enclosing function scope.

total = 0  # Global variable

def sum_function(arg1, arg2):
    total = arg1 + arg2  # Local variable
    print("Inside the function local total:", total)
    return total

# Calling the function
sum_function(10, 20)
print("Outside the function global total:", total)


# Function Annotations With Return Type
# Function annotations provide a way to attach metadata to function arguments and return types. 
# They are ignored at runtime but can be useful for documentation and type checking.

def my_function(a: int, b: int) -> int:
    c = a + b
    return c

# Print the result
print(my_function(56, 88))
# Print annotations
print(my_function.__annotations__)


# Python Modules
# Modules are files that contain related functions, classes, variables, etc. 
# They help in organizing code and making it reusable.

import math

# Using a function from the math module
print("Square root of 100:", math.sqrt(100))


# List of Python Built-in Functions
# Python has numerous built-in functions that are readily available for use, simplifying various tasks.

# Using built-in functions
print("sum:", sum([10, 20]))
print("min:", min([10, 20, 30]))
print("max:", max([10, 20, 30]))


# Built-in Mathematical Functions
# Python provides specific functions for mathematical operations:

# Example of built-in mathematical functions
print("Absolute value of -10:", abs(-10))
print("Maximum of 10 and 20:", max(10, 20))
print("Minimum of 10 and 20:", min(10, 20))
print("Power of 2 raised to 3:", pow(2, 3))
print("Rounded value of 4.56789:", round(4.56789, 2))
print("Sum of numbers in a list:", sum([1, 2, 3, 4, 5]))


# Advantages of Using Built-in Functions
# Using built-in functions in Python has several advantages:
# - Simplifies code: Reduces complexity and enhances readability.
# - Promotes reusability: Saves time and maintains consistency.
# - Descriptive names: Makes code easier to understand and maintain.

