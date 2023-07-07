import csv
import json


def csv_to_json(csv_file, json_file):
    # Open the CSV file
    with open(csv_file, 'r') as file:
        # Read the CSV data
        csv_data = csv.DictReader(file)

        # Convert CSV to JSON
        json_data = json.dumps(list(csv_data), indent=4)

        # Write the JSON data to a file
        with open(json_file, 'w') as json_file:
            json_file.write(json_data)


# Specify the CSV and JSON file paths
csv_file = 'input.csv'
json_file = 'output.json'

# Convert CSV to JSON
csv_to_json(csv_file, json_file)

print(f"CSV file '{csv_file}' has been converted to JSON file '{json_file}'.")
