import csv
import json

# Define file paths
csv_file_path = 'Bank.csv'
json_file_path = 'output.json'

# Open and read the CSV file
with open(csv_file_path, 'r') as csv_file:
    # csv.DictReader automatically maps the header row to dictionary keys
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)
    print(data)


# Write the data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file)

with open(json_file_path) as file:
    dta = json.load(file)
    for account in dta:
        print(f'Name: {account['AccountId']},Balance:{account['Balance']}')