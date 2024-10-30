import json

# Writing data to a JSON file
data = {"Name": "Alice", "Age": 24, "City": "New York"}
with open("example.json", "w") as file:
    json.dump(data, file, indent=4)  # 'indent' makes the JSON readable






# Adding new data to an existing JSON file
new_data = {"Name": "Bob", "Age": 19, "City": "Los Angeles"}

with open("example.json", "r") as file:
    data = json.load(file)  # Load existing data

if isinstance(data, list):
    data.append(new_data)  # Append to list
else:
    data = [data, new_data]  # Convert to list if necessary

with open("example.json", "w") as file:
    json.dump(data, file, indent=4)





# Reading data from a JSON file
with open("example.json", "r") as file:
    data = json.load(file)
    print(data)  # Output is a dictionary or list depending on JSON structure
