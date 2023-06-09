## csv and json modules are inbuilt, but if not present, install by typing these commands in the terminal
##   pip install csv
##   pip install json

#now import them
import csv
import json

#defining the function that actually does the work
def csv_to_json(csv_file_path, json_file_path):
    '''This function takes two parameters: csv file path and json file path
        Note that both file paths should be with proper extension'''
    data = []
    # Read the CSV file and read data as a dictionary
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Convert each row into a dictionary and add it to the data list
        for row in csv_reader:
            data.append(row)
    # Write the data list to a JSON file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))

# Provide the file paths for the CSV and JSON files
# If these files are not in the the present working directory, mention full path
csv_file_path = 'input.csv'
json_file_path = 'output.json'

# Call the function to convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)
