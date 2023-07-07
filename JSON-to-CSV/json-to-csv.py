# json and csv modules are installed by default, no need to install

import json
import csv


# specify file path , along with extension
input_json_file = 'input.json'
csv_file = 'output.csv'

# Load JSON data from a file
with open(input_json_file) as json_file:
    data = json.load(json_file)

# Open the CSV file in write mode
with open(csv_file, 'w', newline='') as csvfile:
    # Create a CSV writer
    writer = csv.writer(csvfile)

    # Write the header row based on the keys of the first JSON object
    writer.writerow(data[0].keys())

    # Write the data rows
    for item in data:
        writer.writerow(item.values())

printf("Conversion successfull. The output file is saved as : " + csv_file)
