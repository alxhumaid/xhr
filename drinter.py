import json

# Load the data from dutput.json
with open('dutput.json', 'r') as file:
    data = json.load(file)

# Create a new list to store the transformed data
transformed_data = []

# Process each item in the original data
for item in data:
    p = item['p']
    l = item['l']
    
    # Create the new dictionary based on the given template
    new_entry = {
        "type": "CDEKYCD",
        "state_code": p,
        "district_code": l,
        "block_code": "",
        "rpttype": "B",
        "urban_rural": "",
        "fdate": "2020-07-24",
        "tdate": "2024-08-07"
    }
    
    # Append the new entry to the transformed_data list
    transformed_data.append(new_entry)

# Save the transformed data to a new JSON file
with open('transformed_data.json', 'w') as file:
    json.dump(transformed_data, file, indent=4)

print("Data transformation complete. Check transformed_data.json for the result.")
