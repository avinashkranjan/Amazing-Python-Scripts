import sys
from os import chdir
from os.path import abspath, join, split
from json import load
from subprocess import run

# Used join() method here to build paths for different OS
PATH_TO_DATASTORE = join("Master Script","datastore.json")
INDEX = {"PATH" : 0, "SCRIPT" : 1, "ARGUMENT" : 2, "REQUIREMENTS":3, "CONTRIBUTOR": 4, "DESCRIPTION" : 5}

version = sys.version.split(' ')[0][0]
interpretor = "3" if version == "3" else ""

def print_menu(script_ob, level):
    """Prints a menu based on the available choices present in the script_ob dict object"""

    keys = [*script_ob]

    # Add option to exit from the menu
    keys.append("Exit")

    # Print all the available choices
    count = 1
    for key in keys:
        print("{}. {}".format(count, key))
        count += 1

    choice = int(input("Enter your choice: "))
    print()

    # Check for invalid input
    while choice < 0 or choice > len(keys):
        print("\nError: Invalid Choice")
        return print_menu(script_ob, level)

    # Recursive case
    if level > 1:
        return print_menu(script_ob[keys[choice-1]], level-1)

    # Base case
    return script_ob[keys[choice-1]]

def install_requirements(path):
    """Installs the necessary packages for a particular script"""
    try:
        print("Installing necessary packages\n")
        res = run(f"pip{interpretor} install -r {path}", shell=True)
    except Exception as e:
        print(f"Erro: There was a problem in installing the packages from {abspath(join('.', path))} file")
        print(f"Error: {str(e)}")
        sys.exit(1)

def main():
    """Loads the script data, and runs the selected script"""

    # Load data from "datastore.json" file
    SCRIPTS = None
    ARGUMENTS = []
    with open(PATH_TO_DATASTORE, "r") as f:
        SCRIPTS = load(f)

    script_arr = print_menu(SCRIPTS, 2)
    print()
    if script_arr == "Exit":
        exit(0)

    #Print Script description
    print(f"SCRIPT BY: {script_arr[INDEX['CONTRIBUTOR']]}")
    print(f"DESCRIPTION: {script_arr[INDEX['DESCRIPTION']]}\n")
    
    # Load arguments
    if script_arr[INDEX["ARGUMENT"]] != "none": 
        # TODO: Input arguments as required from the user
        pass
    else:
        sys.path.append(abspath(script_arr[INDEX["PATH"]]))
        chdir(script_arr[INDEX["PATH"]])

        # Install packages form requirements.txt if any
        if script_arr[INDEX["REQUIREMENTS"]] != "none":
            install_requirements(split(script_arr[INDEX["REQUIREMENTS"]])[-1])
            print("\nPackages installed!!\n")

        script_name = script_arr[INDEX["SCRIPT"]]

        if script_name == "manage.py":
            ARGUMENTS.append("runserver")

        output = run(f"python{interpretor} {script_name} {' '.join(ARGUMENTS)}", shell=True, capture_output=True)
        if output.returncode != 0:
            error = output.stderr.decode("utf-8")
            print(f"There occurred an error while processing your request:\n\n{error}")
            if "No module named" in error:
                print("One or more modules are missing. Make sure the following:\n"
                "1. There exists a requirements.txt file in your project.\n"
                "2. All the necessary external modules are listed in the requirements.txt file.")


if __name__ == '__main__':
    main()