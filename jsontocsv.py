import csv
import json

# Load data from x.json
with open('blockdata.json', 'r') as json_file:
    data = json.load(json_file)

# Define the CSV file name
csv_file = 'blockdata.csv'

# Get the CSV header from the keys of the first dictionary
header = data[0].keys()

# Write to the CSV file
with open(csv_file, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=header)

    # Write the header
    writer.writeheader()

    # Write the data rows
    for entry in data:
        writer.writerow(entry)

print(f"Data has been written to {csv_file}")
