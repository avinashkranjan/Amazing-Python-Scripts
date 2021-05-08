import sys
from os import chdir, system
from os.path import abspath, join, split
from json import load
from subprocess import run, CalledProcessError

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
    if choice == len(keys):
        print("Exiting")
        sys.exit(0)

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
        res = run(f"pip{interpretor} install -r {path}", shell=True, check=True)
    except KeyboardInterrupt:
        print("\nExecution halted manually. Exiting script")
        exit(0)
    except CalledProcessError:
        print(f"\nError: There was a problem in installing the packages from {abspath(join('.', path))} file")
        print(f"Error: {str(e)}")
        sys.exit(1)

def execute_selected(script_arr):
    ARGUMENTS = []

    script_name = script_arr[INDEX["SCRIPT"]]

    if script_name == "manage.py":
        ARGUMENTS.append("runserver")

    # Load arguments
    if script_arr[INDEX["ARGUMENT"]] != "none":
        print("The script accepts the following arguments: ", end=" ")
        print(script_arr[INDEX["ARGUMENT"]], end="\n\n")

        # Print help menu if any
        try:
            run(f"python{interpretor} {script_name} -h", check=True, shell=True)
        except CalledProcessError:
            print("\nError: There was a problem running -h command on your script")
            sys.exit(3)

        # Take in command-line arguments if any
        print(f"\nEnter the command line argument(s) [if any] space separated in a single line\n: ", end=" ")

        arguments = input()
        ARGUMENTS.append(arguments)

    # Install packages from requirements.txt if any
    if script_arr[INDEX["REQUIREMENTS"]] != "none":
        install_requirements(split(script_arr[INDEX["REQUIREMENTS"]])[-1])
        print("\nPackages installed!!\n")        

    try:
        arguments = ' '.join(ARGUMENTS)
        script = f"python{interpretor} {script_name} {arguments}"
        
        # Using system here in the case of large output
        status = system(script)
        if status != 0:
            raise Exception("Non zero exit code")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure the following about your scripts:\n"
        "1. There exists a requirements.txt file in your project.\n"
        "2. All the necessary external modules are listed in the requirements.txt file.")

        sys.exit(0)


def main():
    """Loads the script data, and runs the selected script"""

    # Load data from "datastore.json" file
    SCRIPTS = None
    with open(PATH_TO_DATASTORE, "r") as f:
        SCRIPTS = load(f)

    script_arr = print_menu(SCRIPTS, 2)
    if script_arr == "Exit":
        exit(0)

    # Change path of the system to point to the selected script
    sys.path.append(abspath(script_arr[INDEX["PATH"]]))
    chdir(script_arr[INDEX["PATH"]])

    #Print Script Contributor
    print(f"SCRIPT NAME: {script_arr[INDEX['PATH']]}")
    print(f"SCRIPT BY: {script_arr[INDEX['CONTRIBUTOR']]}")
    print(f"DESCRIPTION: {script_arr[INDEX['DESCRIPTION']]}\n")

    execute_selected(script_arr)

if __name__ == '__main__':
    main()