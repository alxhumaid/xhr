import csv
import json

# Path to the CSV file
csv_filename = 'anotherone.csv'

# Path to the output JSON file
json_filename = 'dutput.json'

# Initialize an empty list to store the JSON objects
json_data = []

# Open and read the CSV file
with open(csv_filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Loop through each row in the CSV
    for row in csv_reader:
        # Create a JSON object for each row
        json_object = {
            "p": row['state_code'],
            "k": row['text'],
            "l": row['district_code']
        }
        # Append the JSON object to the list
        json_data.append(json_object)

# Write the JSON data to a file
with open(json_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"Data has been successfully converted to {json_filename}")
