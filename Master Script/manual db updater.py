from optparse import OptionParser
import json
import sys
import os

usage = """
<Script> [Options]

[Options]
    -h, --help        Show this help message and exit.
    -a, --add         Goes straight to the add script phase
"""
# Load args
parser = OptionParser()
parser.add_option("-a", "--add", action="store_true", dest="add", help="Goes straight to the add script phase")


# The database is automatically updated after the PR is merged.
# ONLY Use this function if you were asked to, to manually add projects to the database.
def add_script():
    """ Add a Contributor script through a series of inputs """
    print("Double check inputs before pressing enter. If one input is incorrect press CTRL-C and re-run the script")
    category =          input("Enter What category does your script belongs to > ")
    name     =          input("Enter script title > ")
    path     =          input("Enter folder name that contains your script > ")
    requirments_path =  input("Enter requirements.txt path (else none) > ")
    entry    =          input("Enter name of the file that runs the script > ")
    arguments =         input("Enter scripts arugments if needed ( '-' seperated + no whitespaces) (else none) > ")
    contributor =       input("Enter your GitHub username > ")
    description =       input("Enter a description for your script > ")

    new_data = {category: {name: [path, entry, arguments, requirments_path, contributor, description]}}
    data_store = read_data()
    
    try:
        # If category doesn't exist try will fail and except will ask to add a new category with the project
        if data_store[category]:                                          # Check for existing category or a new one
                data_store[category].update(new_data[category])           # Add script
    except:
        sure = "Y"
        sure = input("A new category is about to be added. You sure? Y/n > ")
        if sure.lower() == "y" or sure == "":
            data_store.update(new_data)                                       # Add new category
        else:
            print("Data wasn't added please re-run the script and add the correct inputs.")
            sys.exit(1)
        
    with open("datastore.json", "w") as file:
        json.dump(data_store, file)
    print("Script added to database")


def read_data():
    """ Loads datastore.json """
    with open("datastore.json", "r") as file:
        data = json.load(file)
    return data


def check_data():
    """ Validates that all projects exists in the datastore and prints out those are not in the DB """
    data = read_data()
    paths = []
    for category in data:
        for project in data[category]:
            paths.append(data[category][project][0])
    i=0
    repo_dir = os.listdir("../")
    ignore = [".deepsource.toml", ".git", ".github", ".gitignore",
              "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "LICENSE",
              "README.md", "SCRIPTS.md", "script_updater.py",
              "Template for README.md", "Master Script", ]
    for element in repo_dir:
        if (not element in paths) and (not element in ignore):
            print(element)
            i+=1

    print(f"Total of {i} non-added projects.")
            
    


# Start checkpoint
if __name__ == "__main__":
    (options, args) = parser.parse_args()

    # Inputs
    add = options.add

    if add:
        add_script()
    #add_script()
    check_data()
