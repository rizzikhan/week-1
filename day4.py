# Day 4 - Data Structures in Python

# Python Lists
# A list is one of the built-in data types in Python. 
# A Python list is a sequence of comma-separated items, enclosed in square brackets [ ].
# The items in a Python list need not be of the same data type.
# A list is an ordered collection of items, where each item has a unique position index starting from 0.

list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]

# Python List Methods
# Python includes the following list methods:
# 1. list.append(obj) - Appends object obj to list.
# 2. list.clear() - Clears the contents of the list.
# 3. list.copy() - Returns a copy of the list object.
# 4. list.count(obj) - Returns count of how many times obj occurs in the list.
# 5. list.extend(seq) - Appends the contents of seq to the list.
# 6. list.index(obj) - Returns the lowest index in the list that obj appears.
# 7. list.insert(index, obj) - Inserts object obj into the list at offset index.
# 8. list.pop(obj=list[-1]) - Removes and returns last object or obj from the list.
# 9. list.remove(obj) - Removes object obj from the list.
# 10. list.reverse() - Reverses objects of the list in place.
# 11. list.sort([func]) - Sorts objects of the list, use compare func if given.

# Accessing List Items
print("Items from index 1 to last in list1: ", list1[1:]) # ['Physics', 21, 69.75]
print("Items from index 0 to 1 in list2: ", list2[:2]) # [1, 2]
print("Items from index 0 to last in list3: ", list3[:]) # ['a', 'b', 'c', 'd']

# Changing List Items
print("Original list: ", list1) # Original list
list1[1:3] = ['Z'] # Change items at index 1 and 2
print("List after changing with sublist: ", list1) # ['Rohan', 'Z', 69.75]

# Adding List Items
# Adding using append()
list1.append('e')
print("List after appending: ", list1) # ['Rohan', 'Z', 69.75, 'e']

# Adding using insert()
list1.insert(2, 'Chemistry')
print("List after inserting at index 2: ", list1) # ['Rohan', 'Z', 'Chemistry', 69.75, 'e']
list1.insert(-1, 'Pass')
print("List after inserting 'Pass': ", list1) # ['Rohan', 'Z', 'Chemistry', 69.75, 'Pass', 'e']

# Adding using extend()
another_list = [4, 5, 6]
list1.extend(another_list)
print("Extended list:", list1) # ['Rohan', 'Z', 'Chemistry', 69.75, 'Pass', 'e', 4, 5, 6]

# Removing List Items
# Remove using remove()
list1.remove("Chemistry")
print("List after removing 'Chemistry': ", list1) # ['Rohan', 'Z', 69.75, 'Pass', 'e', 4, 5, 6]

# Remove using pop()
popped_item = list1.pop(2) # removes and returns the item at index 2
print("List after popping index 2: ", list1) # ['Rohan', 'Z', 'Pass', 'e', 4, 5, 6]

# Remove using clear()
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print("Cleared list:", my_list) # []

# Remove using del keyword
del list1[2]
print("List after deleting index 2: ", list1) # ['Rohan', 'Z', 'Pass', 'e', 4, 5, 6]

# Looping through Lists
# Using for loop
lst = [25, 12, 10, -21, 10, 100]
for num in lst:
    print(num, end=' ') # prints each number

# Using while loop
my_list = [1, 2, 3, 4, 5]
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# Loop through items with index
for i in range(len(lst)):
    print("lst[{}]: ".format(i), lst[i])

# Iterate using List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers) # [1, 4, 9, 16, 25]

# Iterate using the enumerate() function
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit) # prints index and fruit

# List Comprehension
uppercase_letters = [char.upper() for char in "hello world" if char.isalpha()]
print(uppercase_letters)  # ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']

# List Comprehensions and Lambda
original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)  # [2, 4, 6, 8, 10]

# Nested Loops in Python List Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
CombLst = [(x, y) for x in list1 for y in list2]
print(CombLst)  # [(1, 4), (1, 5), ...]

# Conditionals in Python List Comprehension
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, ...]

# List Comprehensions vs For Loop
chars = []
for ch in 'TutorialsPoint':
    if ch not in 'aeiou':
        chars.append(ch)
print(chars)  # ['T', 't', 'r', 'l', 's', 'P', 'n', 't']

chars = [char for char in 'TutorialsPoint' if char not in 'aeiou']
print(chars)  # ['T', 't', 'r', 'l', 's', 'P', 'n', 't']

squares = [x * x for x in range(1, 11)]
print(squares)  # [1, 4, 9, ..., 100]

# Advantages of List Comprehension
# - Conciseness: More concise and readable compared to traditional for loops.
# - Efficiency: Generally faster and more efficient than for loops.
# - Clarity: Results in clearer and more expressive code.
# - Reduced Chance of Errors: Less chance of errors due to compactness.

# Python - Sort Lists
# Sorting Lists in Python
# The sort() method sorts the elements of a list in place.
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print("List before sort:", list1)
list1.sort()
print("List after sort: ", list1)  # ['Biology', 'chemistry', 'maths', 'physics']

list2 = [10, 16, 9, 24, 5]
print("List before sort:", list2)
list2.sort()
print("List after sort: ", list2)  # [5, 9, 10, 16, 24]

# Using sorted() function
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1]

# Sorting List Items with Callback Function
list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
print("List before sort:", list1)
list1.sort(key=str.lower)
print("List after sort: ", list1)  # ['biology', 'Biomechanics', 'Physics', 'psychology']

# Copying a List in Python
# Shallow Copy
import copy
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shallow_copied_list = copy.copy(original_list)
shallow_copied_list[0][0] = 100
print("Original List:", original_list)  # [[100, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Shallow Copied List:", shallow_copied_list)  # [[100, 2, 3], [4, 5, 6], [7, 8, 9]]

# Deep Copy
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[0][0] = 200
print("Original List after deep copy modification:", original_list)  # [[100, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Deep Copied List:", deep_copied_list)  # [[200, 2, 3], [4, 5, 6], [7, 8, 9]]

# Python Tuples
# A tuple is similar to a list in Python. However, it is immutable, which means once it is created, the items in it cannot be modified.
# Tuples are defined by enclosing the elements in parentheses ().

# Tuple Creation
tuple1 = (1, 2, 3)
tuple2 = (1,)  # A single element tuple requires a trailing comma.
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ('Rohan', 3.14, 'Physics', True)

# Accessing Tuple Items
print("First item of tuple1:", tuple1[0])  # 1
print("Last item of tuple1:", tuple1[-1])  # 3

# Iterating through Tuple
for item in tuple4:
    print(item)  # prints each item

# Count and Index
print("Count of 1 in tuple1:", tuple1.count(1))  # 1
print("Index of 3 in tuple1:", tuple1.index(3))  # 2

# Converting List to Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("Converted tuple:", my_tuple)  # (1, 2, 3)

# Tuple Packing and Unpacking
packed_tuple = 1, 2, 3
a, b, c = packed_tuple  # unpacking
print("Unpacked values:", a, b, c)  # 1 2 3

# Python Sets
# A set is a collection which is unordered, unchangeable, and unindexed. Sets are defined by curly brackets {}.

# Creating a Set
set1 = {1, 2, 3}
set2 = {1, "Rohan", 3.14}

# Adding Items to a Set
set1.add(4)
print("Set after adding 4:", set1)  # {1, 2, 3, 4}

# Removing Items from a Set
set1.remove(2)
print("Set after removing 2:", set1)  # {1, 3, 4}

# Using discard() method
set1.discard(3)  # If 3 is present, remove it. If not, do nothing.
print("Set after discarding 3:", set1)  # {1, 4}

# Looping Through a Set
for item in set1:
    print(item)  # prints each item

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
set_c = set_a.union(set_b)
print("Union of set_a and set_b:", set_c)  # {1, 2, 3, 4, 5}

# Intersection
set_d = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", set_d)  # {3}

# Difference
set_e = set_a.difference(set_b)
print("Difference of set_a from set_b:", set_e)  # {1, 2}

# Symmetric Difference
set_f = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", set_f)  # {1, 2, 4, 5}

# Set Comprehensions
set_comp = {x * x for x in range(10)}
print("Set Comprehension:", set_comp)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Python Dictionaries
# A dictionary is an unordered collection of items. Each item is stored as a pair of key and value.
# Dictionaries are defined by curly brackets {} with key-value pairs separated by a colon.

# Creating a Dictionary
dict1 = {"name": "Rohan", "age": 21, "subject": "Physics"}
print("Dictionary:", dict1)

# Accessing Dictionary Items
print("Name:", dict1["name"])  # Rohan
print("Age:", dict1.get("age"))  # 21

# Adding Items to a Dictionary
dict1["marks"] = 80
print("Updated Dictionary:", dict1)

# Removing Items from a Dictionary
del dict1["subject"]
print("Dictionary after deletion:", dict1)

# Looping Through a Dictionary
for key, value in dict1.items():
    print(key, value)

# Dictionary Comprehensions
dict_comp = {x: x ** 2 for x in (2, 3, 4, 5)}
print("Dictionary Comprehension:", dict_comp)  # {2: 4, 3: 9, 4: 16, 5: 25}


# Python - Tuples

# A tuple is a built-in data type in Python that is a sequence of comma-separated items enclosed in parentheses.
# Tuples can contain items of different data types.

# Creating tuples
tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1 + 2j)
empty_tuple = ()  # An empty tuple
single_element_tuple = (50,)  # A single element tuple must have a trailing comma

# Python - Access Tuple Items
# Accessing items in a tuple using indexing
tuple1 = ("Rohan", "Physics", 21, 69.75)
tuple2 = (1, 2, 3, 4, 5)

print("Item at 0th index in tuple1: ", tuple1[0])  # Access first item
print("Item at index 2 in tuple2: ", tuple2[2])  # Access third item

# Accessing items using negative indexing
print("Item at 0th index in tup1: ", tup1[-1])  # Last item
print("Item at index 2 in tup2: ", tup2[-3])  # Third last item

# Slicing tuples
print("Items from index 1 to last in tup1: ", tup1[1:])  # From second item to last
print("Items from index 2 to last in tup2: ", tup2[2:-1])  # From third to second last

# Accessing slices in multiple tuples
print("Items from index 1 to last in tuple1: ", tuple1[1:])  # Second to last in tuple1
print("Items from index 0 to 1 in tuple2: ", tuple2[:2])  # First two items in tuple2
print("Items from index 0 to index last in tuple3: ", tup3[:])  # All items in tup3

# Python - Update Tuples
# Tuples are immutable; they cannot be changed directly.
# However, we can concatenate tuples or create a new one.

# Original tuple
T1 = (10, 20, 30, 40)
# Tuple to be concatenated
T2 = ('one', 'two', 'three', 'four')
# Updating the tuple using the concatenation operator
T1 = T1 + T2
print("Updated Tuple:", T1)  # Output: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

# Creating a new tuple by adding elements
T1 = (37, 14, 95, 40)
new_elements = ('green', 'blue', 'red', 'pink')
# Extracting slices of the original tuple
part1 = T1[:2]  # Elements before index 2
part2 = T1[2:]  # Elements from index 2 onward
# Create a new tuple
updated_tuple = part1 + new_elements + part2
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)  # Output: (37, 14, 'green', 'blue', 'red', 'pink', 95, 40)

# Updating tuples by converting to lists
T1 = (10, 20, 30, 40)
# Convert the tuple to a list
list_T1 = list(T1)
# Using list comprehension to add 100 to each item
updated_list = [item + 100 for item in list_T1]
# Converting the updated list back to a tuple
updated_tuple = tuple(updated_list)
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)  # Output: (110, 120, 130, 140)

# Adding new elements using append
T1 = (10, 20, 30, 40)
list_T1 = list(T1)
new_elements = [50, 60, 70]
# Updating the list using append()
for element in new_elements:
    list_T1.append(element)
# Converting list back to tuple
updated_tuple = tuple(list_T1)
print("Original Tuple:", T1)
print("Updated Tuple:", updated_tuple)  # Output: (10, 20, 30, 40, 50, 60, 70)

# Python - Unpack Tuple Items
tup1 = (10, 20, 30)
x, y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)

# Example of ValueError when unpacking
try:
    x, y = tup1  # Correct
    x, y, p, q = tup1  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")  # Not enough values to unpack

# Unpacking with starred expressions
x, *y = tup1
print("x: ", x, "y: ", y)  # Output: x: 10 y: [20, 30]

tup1 = (10, 20, 30, 40, 50, 60)
x, *y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)  # Output: x: 10 y: [20, 30, 40, 50] z: 60

*x, y, z = tup1
print("x: ", x, "y: ", y, "z: ", z)  # Output: x: [10, 20, 30, 40] y: 50 z: 60

# Python - Loop Tuples
tup = (25, 12, 10, -21, 10, 100)
# Using a for loop to iterate through tuple
for num in tup:
    print(num, end=' ')  # Output items in same line

# Using a while loop to iterate through tuple
my_tup = (1, 2, 3, 4, 5)
index = 0
while index < len(my_tup):
    print(my_tup[index])  # Output: 1 2 3 4 5
    index += 1

# Accessing items using indices
for i in range(len(tup)):
    print(f"tup[{i}]: ", tup[i])

# Python - Join Tuples
# Joining two tuples
T1 = (10, 20, 30, 40)
T2 = ('one', 'two', 'three', 'four')
joined_tuple = T1 + T2
print("Joined Tuple:", joined_tuple)  # Output: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

# Joining tuples using list comprehension
T1 = (36, 24, 3)
T2 = (84, 5, 81)
joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
print("Joined Tuple:", joined_tuple)  # Output: [36, 24, 3, 84, 5, 81]

# Joining tuples using extend method
T1 = (10, 20, 30, 40)
T2 = ('one', 'two', 'three', 'four')
L1 = list(T1)
L2 = list(T2)
L1.extend(L2)
T1 = tuple(L1)
print("Joined Tuple:", T1)  # Output: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

# Joining tuples using sum()
T1 = (10, 20, 30, 40)
T2 = ('one', 'two', 'three', 'four')
T3 = sum((T1, T2), ())
print("Joined Tuple:", T3)  # Output: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

# Joining tuples using for loop
T1 = (10, 20, 30, 40)
T2 = ('one', 'two', 'three', 'four')
for t in T2:
    T1 += (t,)  # Concatenating tuples
print(T1)  # Output: (10, 20, 30, 40, 'one', 'two', 'three', 'four')

# Python - Tuple Methods
# Demonstrating tuple methods
tup1 = (25, 12, 10, -21, 10, 100)
print("Tup1:", tup1)
x = tup1.index(10)  # Returns the first index of 10
print("First index of 10:", x)  # Output: 2

tup1 = (10, 20, 45, 10, 30, 10, 55)
print("Tup1:", tup1)
c = tup1.count(10)  # Counts occurrences of 10
print("Count of 10:", c)  # Output: 3

tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print("Tup1:", tup1)
c = tup1.count(0.25)  # Counts occurrences of 0.25
print("Count of 0.25:", c)  # Output: 3

# Exercise - Creating a tuple with unique numbers
T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
T2 = ()
for x in T1:
    if x not in T2:
        T2 += (x,)
print("Original tuple:", T1)
print("Unique numbers:", T2)  # Output: (1, 9, 6, 3, 4, 5, 2, 7, 8)

# Sum of all numbers in a tuple
T1 = (1, 9, 1, 6, 3, 4)
ttl = sum(T1)
print("Sum of all numbers using sum() function:", ttl)  # Output: 24

# Generating a tuple of random numbers
import random
t1 = ()
for i in range(5):
    x = random.randint(0, 100)
    t1 += (x,)
print("Random Tuple:", t1)  # Output: A tuple of 5 random numbers
