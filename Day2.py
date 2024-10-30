# control_flow_statements.py

# Section 1: Control Flow Statements
# Control flow statements allow you to dictate the flow of execution in your programs.
# They are essential for making decisions, looping through data, and handling different conditions.

# 1.1 If, If-Else, Elif
# The if statement is used to evaluate a condition. If the condition is true, it executes the block of code within it.
# If the condition is false, it can optionally evaluate an else block or additional elif (else if) conditions.

marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print("Result based on marks:", result)

# 1.2 Nested If-Else
# Nested if-else statements are used when you want to check multiple conditions. 
# An if statement can be placed inside another if statement, allowing for more complex decision-making.

num = 8
print("\nnum =", num)
if num % 2 == 0:
    if num % 3 == 0:
        print("Divisible by 3 and 2")
    else:
        print("Divisible by 2, not divisible by 3")
else:
    if num % 3 == 0:
        print("Divisible by 3, not divisible by 2")
    else:
        print("Not divisible by 2 and not divisible by 3")

# Additional nested if-else example
var = 100
if var == 100:
    print("The number is equal to 100")
    if var % 2 == 0:
        print("The number is even")
    else:
        print("The given number is odd")
elif var == 0:
    print("The given number is zero")
else:
    print("The given number is negative")

# 1.3 Match Case Statement (Python 3.10+)
# The match-case statement allows for pattern matching, providing a more readable way to handle multiple conditions.
# It works similarly to switch-case statements found in other programming languages.

def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number"

print("\nWeekday examples:")
print(weekday(3))  # Output: Thursday
print(weekday(6))  # Output: Sunday
print(weekday(7))  # Output: Invalid day number

# Another match case example for user access levels
def access(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Limited access"
        case _: return "No access"

print("\nAccess examples:")
print(access("manager"))  # Output: Full access
print(access("Guest"))     # Output: Limited access
print(access("Ravi"))      # Output: No access

# Match case for checking vowels
def checkVowel(n):
    match n:
        case 'a': return "Vowel alphabet"
        case 'e': return "Vowel alphabet"
        case 'i': return "Vowel alphabet"
        case 'o': return "Vowel alphabet"
        case 'u': return "Vowel alphabet"
        case _: return "Simple alphabet"

print("\nVowel check examples:")
print(checkVowel('a'))  # Output: Vowel alphabet
print(checkVowel('m'))  # Output: Simple alphabet
print(checkVowel('o'))  # Output: Vowel alphabet

# 1.4 For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).
# It allows you to execute a block of code multiple times, once for each item in the sequence.

words = ["one", "two", "three"]
print("\nFor loop through list:")
for x in words:
    print(x)

# 1.5 For Loop in Dictionary
# You can also iterate through dictionaries using for loops. 
# By default, the loop iterates over the keys of the dictionary.

numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print("\nFor loop through dictionary keys:")
for x in numbers:
    print(x)

print("\nFor loop through dictionary items:")
for x in numbers:
    print(x, ":", numbers[x])

# 1.6 While Loop
# A while loop repeatedly executes a block of code as long as a specified condition is true.
# Be careful to ensure that the condition will eventually become false to avoid infinite loops.

print("\nWhile loop example:")
i = 1
while i < 6:
    print(i)
    i += 1

# 1.7 Break Statement
# The break statement is used to exit a loop prematurely. 
# It can be used in both for and while loops to terminate the loop when a certain condition is met.

print("\nBreak statement example:")
x = 0
while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x += 1

print("End of break statement example")

# 1.8 Continue Statement
# The continue statement is used to skip the current iteration of a loop and move to the next iteration. 
# It can be helpful when you want to ignore certain conditions.

print("\nContinue statement example:")
for letter in "Python":
    if letter == "h":
        continue
    print("Current Letter:", letter)

# 1.9 Pass Statement
# The pass statement is a null operation; it does nothing when executed. 
# It's used as a placeholder when a statement is required syntactically but you have nothing to execute.

print("\nPass statement example:")
for letter in 'Python':
    if letter == 'h':
        pass  # Placeholder for future code
        print('This is pass block')
    print('Current Letter:', letter)

print("Goodbye!")
