import json
import csv
import requests
import time 
from requests.auth import HTTPBasicAuth

# Define the API endpoint
url = "https://dashboard.pmjay.gov.in/pmjaytest14/api/pmjdashboard/carddrive/1.0"
filename = "district_data.csv"

header_written = False
# Define the basic authentication credentials
username = "stateuser"
password = "state@1234"

# Define the headers (if required)
headers = {
    "Content-Type": "application/json"
}

state = [
    {
        "Text": "JAMMU AND KASHMIR",
        "Code": 1
    },
    {
        "Text": "HIMACHAL PRADESH",
        "Code": 2
    },
    {
        "Text": "PUNJAB",
        "Code": 3
    },
    {
        "Text": "CHANDIGARH",
        "Code": 4
    },
    {
        "Text": "UTTARAKHAND",
        "Code": 5
    },
    {
        "Text": "HARYANA",
        "Code": 6
    },
    {
        "Text": "RAJASTHAN",
        "Code": 8
    },
    {
        "Text": "UTTAR PRADESH",
        "Code": 9
    },
    {
        "Text": "BIHAR",
        "Code": 10
    },
    {
        "Text": "SIKKIM",
        "Code": 11
    },
    {
        "Text": "ARUNACHAL PRADESH",
        "Code": 12
    },
    {
        "Text": "NAGALAND",
        "Code": 13
    },
    {
        "Text": "MANIPUR",
        "Code": 14
    },
    {
        "Text": "MIZORAM",
        "Code": 15
    },
    {
        "Text": "TRIPURA",
        "Code": 16
    },
    {
        "Text": "MEGHALAYA",
        "Code": 17
    },
    {
        "Text": "ASSAM",
        "Code": 18
    },
    {
        "Text": "JHARKHAND",
        "Code": 20
    },
    {
        "Text": "CHHATTISGARH",
        "Code": 22
    },
    {
        "Text": "MADHYA PRADESH",
        "Code": 23
    },
    {
        "Text": "GUJARAT",
        "Code": 24
    },
    {
        "Text": "MAHARASHTRA",
        "Code": 27
    },
    {
        "Text": "Andhra Pradesh",
        "Code": 28
    },
    {
        "Text": "KARNATAKA",
        "Code": 29
    },
    {
        "Text": "GOA",
        "Code": 30
    },
    {
        "Text": "LAKSHADWEEP",
        "Code": 31
    },
    {
        "Text": "KERALA",
        "Code": 32
    },
    {
        "Text": "TAMIL NADU",
        "Code": 33
    },
    {
        "Text": "PUDUCHERRY",
        "Code": 34
    },
    {
        "Text": "ANDAMAN AND NICOBAR ISLANDS",
        "Code": 35
    },
    {
        "Text": "TELANGANA",
        "Code": 36
    },
    {
        "Text": "Ladakh",
        "Code": 37
    },
    {
        "Text": "Dadra and Nagar Haveli and Daman and Diu",
        "Code": 38
    }
]
data = {"type":"CDEKYCD","state_code":"","district_code":"","block_code":"","rpttype":"D","urban_rural":"","fdate":"2020-07-24","tdate":"2024-08-07"}

for x in state:
    st = x['Code']
    print(st)
    data["state_code"] = st
    print(data)
    retry=10
    for i in range(retry):
        try:
            response = requests.post(url, headers=headers, json=data, auth=HTTPBasicAuth(username, password))
            break
        except requests.exceptions.ConnectionError:
            if i < retry-1:
                time.sleep(3)
            else:
                raise
            

    print(f"Status Code: {response.status_code}")
    print("Response Text:")
    print(response.text)
    try:
        response_json = response.json()
        # print("Response JSON:")
        # print(json.dumps(response_json, indent=4))
        pata = response_json
        
        extracted_data =    [   
                              {
                                             "state_code": district["state_code"],
                                             "text": district["text"],
                                             "district_code": district["district_code"]
                              }
                              for district in pata["list"]
        ]
                    
        # print(f"District: {district['text']}")
        # print(f"  District Code: {district['district_code']}")
        with open(filename, mode='a', newline='') as file:  # Use 'a' for append mode
            writer = csv.DictWriter(file, fieldnames=["state_code", "text", "district_code"])
            if not header_written:
                writer.writeheader()
                header_written = True
            writer.writerows(extracted_data)
       


        print(f"Data saved to {filename}")
        if not pata['list']:
            print("No data available in the list.")
    except ValueError:
            print("Response is not in JSON format.")
