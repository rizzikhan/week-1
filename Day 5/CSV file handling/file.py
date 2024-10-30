import csv


print("-------------Writing to a .csv File")


# Writing to a CSV file
data = [["Name", "Age"], ["Alice", 24], ["Bob", 19]]
with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Writing to a CSV file as a dictionary
fieldnames = ["Name", "Age"]
rows = [{"Name": "Alice", "Age": 24}, {"Name": "Bob", "Age": 19}]
with open("file.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()  # Writing the header
    writer.writerows(rows)

    print("------------Appending CSV File ")

# Appending data to a CSV file
new_data = [["Charlie", 23], ["David", 29]]
with open("file.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)


print("-------------Reading to a .csv File")


print("reading file CSV file as List of Rows ")
# Reading a CSV file as a list of rows
with open("file.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("reading file CSV file as Dict of Rows ")
# Reading a CSV file as a dictionary
with open("file.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)  # Each row is a dictionary



