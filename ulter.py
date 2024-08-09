import requests 
import time
from requests.auth import HTTPBasicAuth
import json

# Define the API endpoint
url = "https://dashboard.pmjay.gov.in/pmjaytest14/api/pmjdashboard/carddrive/1.0"

# Define the basic authentication credentials

retry=10
finaldata=[]

# Define the headers (if required)
headers = {
    "Content-Type": "application/json"
}

# Load the data from the JSON file
with open('transformed_data.json', 'r') as file:
    data_list = json.load(file)

# Iterate through each entry in the data list and make a POST request
for data in data_list:
    # Make the POST request with basic authentication
    for i in range(retry):
        try:
            response = requests.post(url, headers=headers, json=data, auth=HTTPBasicAuth(username, password))
            break
        except requests.exceptions.ConnectionError:
            if i < retry-1:
                time.sleep(3)
            else:
                raise
    # Print the status code and response text for each request
    print(f"Request Data: {data}")
    print(f"Status Code: {response.status_code}")
    print("Response Text:")
    
    pata=response.json()
    
    try:
        extracted_data =    [   
                              {
                                             "state_code": x["state_code"],
                                             "text": x["text"],
                                             "district_code": x["district_code"],
                                             "block_code" : x["block_code"]
                             }
                              for x in pata["list"]
        ] 
        finaldata = finaldata + extracted_data
        print(extracted_data)   
        if not pata['list']:
            print("No Data in List")
        
            
    except ValueError:
        print("Response is not in JSON format.")
        
        
    print("\n")  # Print a newline for better readability
with open('blockdata.json', 'w') as file:
            json.dump(finaldata, file, indent=4)    
