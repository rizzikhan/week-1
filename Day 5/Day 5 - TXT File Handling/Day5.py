"""print("--------------File Handling ----------------")


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""


print("--------------File Writing----------------")


"""
write() - Writes a string to a file
writelines() - Writes a list of strings to a file

"""
with open("demofile.txt", "w") as file:
    file.write("This is a new line.\n")
    file.writelines(["Another line.\n", "And another.\n"])

print("--------------File appending----------------")


with open("demofile.txt", "a") as file:
    file.write("This line will be added to the end.\n")


print("--------------Binary PNG File reading----------------")

with open("riz.png", "rb") as file:

    data = file.read()  #reads whole file 
    print(data)


"""
tell() gives the current position of the file pointer.
seek() moves the pointer to a specified location within the file.

"""

print("--------------SEEK and TELL----------------")

with open("demofile.txt", "r") as file:
    print("Final position:", file.tell())
    file.seek(10)  # Moves to the 10th byte
    print("Final position:", file.tell())
    data = file.read()  # Reads from the 10th byte onward
    print(data)


print("--------------File handling with Exception Handling ----------------")

try:
    with open("demofile.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("The file was not found.")

"""
Use Python's os and shutil modules for tasks like renaming, deleting, copying, and moving files.

"""
import os
import shutil
os.rename("demofile.txt", "demofile.txt")  # old name and then new name 
# shutil.copy("demofile.txt", "copy_example.txt")
# os.remove("file.txt")  # Deletes the file





print("--------------File Reading----------------")


with open("demofile.txt", "r") as file:

    data = file.read()  #reads whole file 
    print(data)
    print("-------------")
    lines = file.readlines()  # Reads each line as an element in a list
    print(lines)

