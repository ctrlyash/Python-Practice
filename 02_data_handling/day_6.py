"""
 Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import os
import json
import csv
INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_jason_data(filename):
    if not os.path.exists(filename):
        print("JSON file not found")
        return[]
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            print("Invalid JSON format")

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert")  
        return          
    
    fieldname = list(data[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldname)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    print(f"Converted {len(data)} records to {output_file}")  

def main():
    print("Converting JSON to CSV...")      
    data = load_jason_data(INPUT_FILE)   
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()

# Converting JSON to CSV...
# Converted 3 records to converted_data.csv

# api_data.json content:
# [
#     {
#         "id": "101",
#         "name": "Riya",
#         "email": "riya@example.com",
#         "location": "Delhi",
#         "is_active": true
#     },
#     {
#         "id": "102",
#         "name": "Aman",
#         "email": "aman@example.com",
#         "location": "Mumbai",
#         "is_active": false
#     },
#     {
#         "id": "103",
#         "name": "Neha",
#         "email": "neha@example.com",
#         "location": "Banglore",
#         "is_active": true
#     }
# ]

# converted_data.csv contents:
# id,name,email,location,is_active
# 101,Riya,riya@example.com,Delhi,True
# 102,Aman,aman@example.com,Mumbai,False
# 103,Neha,neha@example.com,Banglore,True