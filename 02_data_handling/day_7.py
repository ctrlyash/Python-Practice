"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import os
import csv
import json

INPUT_FILE = "raw_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return[]
    
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data
    


def save_as_json(data, filename):
    if not data:
        print("No data to convert")  
        return 
    
    with open(filename, "w", newline="", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Converted {len(data)} records to {filename}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))    


def main():
    data = load_csv_data(INPUT_FILE)
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()   


# [{'converted_data.csv contents:': 'id', None: ['name', 'email', 'location', 'is_active']}, {'converted_data.csv contents:': '201', None: ['Meena', 'meena@example.com', 'Pune', 'True']}, {'converted_data.csv contents:': '202', None: ['Rahul', 'rahul@example.com', 'Jaipur', 'False']}, {'converted_data.csv contents:': '203', None: ['Anu', 'anu@example.com', 'Chennai', 'True']}]
# ✅ Converted 4 records to converted_data.json
# {
#   "converted_data.csv contents:": "id",
#   "null": [
#     "name",
#     "email",
#     "location",
#     "is_active"
#   ]
# }
# {
#   "converted_data.csv contents:": "201",
#   "null": [
#     "Meena",
#     "meena@example.com",
#     "Pune",
#     "True"
#   ]
# }
# {
#   "converted_data.csv contents:": "202",
#   "null": [
#     "Rahul",
#     "rahul@example.com",
#     "Jaipur",
#     "False"
#   ]
# }    

# raw_data.csv content:
# id,name,email,location,is_active
# 201,Meena,meena@example.com,Pune,True
# 202,Rahul,rahul@example.com,Jaipur,False
# 203,Anu,anu@example.com,Chennai,True

# converted_data.json content:
# [
#     {
#         "converted_data.csv contents:": "id",
#         "null": [
#           "name",
#           "email",
#           "location",
#           "is_active"
#         ]
#     },
#     {
#         "converted_data.csv contents:": "201",
#         "null": [
#           "Meena",
#           "meena@example.com",
#           "Pune",
#           "True"
#         ]
#     },
#     {
#         "converted_data.csv contents:": "202",
#         "null": [
#           "Rahul",
#           "rahul@example.com",
#           "Jaipur",
#           "False"
#         ]
#     },
#     {
#         "converted_data.csv contents:": "203",
#         "null": [
#           "Anu",
#           "anu@example.com",
#           "Chennai",
#           "True"
#         ]
#     }
# ]
