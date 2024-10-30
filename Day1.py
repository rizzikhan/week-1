# data_types_operations.py

# Section 1: Data Types
# Python has various built-in data types. They are used to define the type of data a variable can hold.
# Here we cover Numbers, Sequence Types, Boolean, Set, Dictionary, and Range.

# 1.1 Numbers
# Numbers in Pythonn can be of various types: Integer, Float, and Complex.
# - Integer: Whole numbers, positive or negative.
# - Float: Decimal numbers, representing real numbers.
# - Complex: Numbers that have a real part and an imaginary part, expressed as a + bj.

int_num = 10
print("Integer:", int_num, "Type:", type(int_num))

float_num = 10.5
print("Float:", float_num, "Type:", type(float_num))

complex_num = 2 + 3j
print("Complex Number:", complex_num, "Type:", type(complex_num))

# 1.2 Sequence Types
# Python includes several sequence types, including Strings, Lists, and Tuples.
# These sequences allow you to store multiple items in a single variable.

# Strings: A string is a sequence of characters.
str1 = "Hello, World!"
str2 = '''This is a 
multiline string.'''
print("String 1:", str1)
print("String 2:", str2)

# String slicing and operations
print("First two characters of str1:", str1[0:2])  # Accessing a slice of the string
print("Fourth character of str1:", str1[3])        # Indexing starts at 0
print("str1 repeated twice:", str1 * 2)            # Repeating the string
print("Concatenation of str1 and str2:", str1 + " " + str2)  # Concatenating strings

# Lists: An ordered and mutable collection of items.
list1 = [1, "hi", "Python", 2]
print("List:", list1, "Type:", type(list1))
print("List slicing (from index 3):", list1[3:])  # Slicing the list
print("List concatenation:", list1 + list1)        # Concatenating lists
print("List repetition:", list1 * 3)                # Repeating the list

# Tuples: Similar to lists, but immutable (cannot be changed).
tup = ("hi", "Python", 2)
print("Tuple:", tup, "Type:", type(tup))
print("Tuple slicing (from index 1):", tup[1:])    # Slicing the tuple
print("Tuple concatenation:", tup + tup)            # Concatenating tuples

# 1.3 Boolean
# Boolean values represent one of two states: True or False.
bool_true = True
bool_false = False
print("Boolean True:", bool_true, "Type:", type(bool_true))
print("Boolean False:", bool_false, "Type:", type(bool_false))

# 1.4 Set
# A set is an unordered collection of unique elements.
set1 = {1, 2, 3, "Python"}
print("Set:", set1, "Type:", type(set1))
set1.add(4)  # Adding an element to the set
print("Set after adding an element:", set1)
set1.remove(2)  # Removing an element from the set
print("Set after removing an element:", set1)

# 1.5 Dictionary
# A dictionary is a collection of key-value pairs, allowing for fast retrieval of data.
dict1 = {1: 'Jimmy', 2: 'Alex', 3: 'John'}
print("Dictionary:", dict1)
print("Value for key 1:", dict1[1])                 # Accessing value by key
print("Keys in dictionary:", dict1.keys())          # Retrieving all keys
print("Values in dictionary:", dict1.values())      # Retrieving all values

# 1.6 Range
# The range function generates a sequence of numbers, commonly used for iteration.
print("Range from 1 to 5:")
for i in range(1, 6):
    print(i)

# Section 2: Type Conversion
# Type conversion allows you to change the data type of a variable.
# There are two types: Implicit and Explicit conversion.

# Implicit Conversion
# This happens automatically when Python converts one data type to another.
a_int = 1
b_float = 1.0
c_sum = a_int + b_float  # int is converted to float
print("Implicit Conversion Result:", c_sum, "Type:", type(c_sum))

# Explicit Conversion
# This is done manually by the user using built-in functions.
c_float_sum = float(a_int + 2)  # Converting to float explicitly
print("Explicit Conversion Result (int to float):", c_float_sum)

# Converting between integers and floats
a_float = 3.3
b_int = int(a_float)  # float to int conversion (truncates decimal)
print("Converted float to int:", b_int)

# Converting string to number
price_cake = '15'
price_cookie = '6'
total = int(price_cake) + int(price_cookie)  # Converting strings to integers
print("Total price (after conversion):", total)

# Converting lists and tuples
a_tuple = ('a', 1), ('b', 2)  # Creating a tuple of pairs
b_list = [1, 2, 3, 4, 5]
print("List to Tuple:", tuple(b_list))           # Converting list to tuple
print("Tuple to List:", list(a_tuple))            # Converting tuple to list

# Section 3: Basic Operators
# Operators are special symbols that perform operations on variables and values.
# Basic operators include Arithmetic, Comparison, and Assignment operators.

# Arithmetic Operators: Used for mathematical calculations.
a, b = 21, 10
print("Addition:", a + b)              # Addition
print("Subtraction:", a - b)           # Subtraction
print("Multiplication:", a * b)        # Multiplication
print("Division:", a / b)              # Division (float result)
print("Modulus:", a % b)               # Remainder of division
print("Exponent:", a ** b)             # Exponentiation
print("Floor Division:", a // b)       # Division without remainder

# Comparison Operators: Used to compare two values.
print("Equal:", a == b)                # Equal to
print("Not Equal:", a != b)            # Not equal to
print("Greater Than:", a > b)          # Greater than
print("Less Than:", a < b)             # Less than
print("Greater Than or Equal To:", a >= b)  # Greater than or equal to
print("Less Than or Equal To:", a <= b)      # Less than or equal to

# Assignment Operators: Used to assign values to variables.
a = 10
a += 5  # Equivalent to a = a + 5
print("After += 5:", a)
a -= 5  # Equivalent to a = a - 5
print("After -= 5:", a)

# Section 4: String Operations
# Strings in Python come with various built-in methods that allow you to manipulate them easily.
# Here are some common string methods and operations.

# String Methods: Functions that perform operations on string data.
var1 = 'Hello World!'
var2 = "Python Programming"
print("Character at index 0 of var1:", var1[0])  # Accessing a character
print("Characters from index 1 to 5 of var2:", var2[1:5])  # Slicing

# Demonstrating string methods
print("Capitalized var1:", var1.capitalize())  # Capitalizes first character
print("Lowercase var2:", var2.lower())        # Converts to lowercase
print("Count of 'o' in var1:", var1.count('o'))  # Counts occurrences of 'o'
print("Does var1 end with 'World!'?", var1.endswith('World!'))  # Checks suffix
print("Replacing 'World' with 'Python' in var1:", var1.replace("World", "Python"))  # Replaces substring

# Example of using join
list_of_words = ["Hello", "World"]
joined_string = " ".join(list_of_words)  # Joining a list of words into a string
print("Joined String:", joined_string)

# Example of splitting a string
splitted_string = var1.split()  # Splitting string into a list of words
print("Splitted String:", splitted_string)

# Output various string manipulations
print("Uppercase var1:", var1.upper())             # Converts to uppercase
print("Is var1 alphanumeric?", var1.isalnum())     # Checks if string is alphanumeric
print("Is 'Hello' an identifier?", 'Hello'.isidentifier())  # Checks if string is a valid identifier
