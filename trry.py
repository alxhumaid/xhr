import csv

# Sample data
data = {
    "list": [
        {
            "otp_auth_count": "5541",
            "demo_auth_count": "1",
            "face_auth": "129",
            "type": "D",
            "ekyc_count": "33103",
            "pending_count": "0",
            "delivered_count": "1",
            "district_code": "465",
            "bio_auth_count": "22241",
            "block_code": "",
            "other_auth_count": "25483",
            "text": "DADRA AND NAGAR HAVELI",
            "state_code": "38",
            "rejected_count": "28",
            "iris_auth_count": "10",
            "approved_count": "33075"
        },
        {
            "otp_auth_count": "5872",
            "demo_auth_count": "5",
            "face_auth": "9",
            "type": "D",
            "ekyc_count": "17485",
            "pending_count": "0",
            "delivered_count": "1",
            "district_code": "463",
            "bio_auth_count": "10268",
            "block_code": "",
            "other_auth_count": "13208",
            "text": "DAMAN",
            "state_code": "38",
            "rejected_count": "12",
            "iris_auth_count": "10",
            "approved_count": "17473"
        },
        {
            "otp_auth_count": "1411",
            "demo_auth_count": "0",
            "face_auth": "103",
            "type": "D",
            "ekyc_count": "4699",
            "pending_count": "1",
            "delivered_count": "0",
            "district_code": "464",
            "bio_auth_count": "2745",
            "block_code": "",
            "other_auth_count": "2630",
            "text": "DIU",
            "state_code": "38",
            "rejected_count": "10",
            "iris_auth_count": "13",
            "approved_count": "4688"
        }
    ],
    "ts": "2024-08-09T04:50:41.363+05:41",
    "status": "true"
}

# Extract relevant data
extracted_data = [
    {
        "state_code": item["state_code"],
        "text": item["text"],
        "district_code": item["district_code"]
    }
    for item in data["list"]
]

# Specify the file name
filename = "district_data.csv"

# Write the data to a CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["state_code", "text", "district_code"])
    writer.writeheader()
    writer.writerows(extracted_data)

print(f"Data saved to {filename}")
