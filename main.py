import sys
from os import chdir
from os.path import abspath, join
from json import load

# Used join() method here to build paths for different OS
PATH_TO_DATASTORE = join("Master Script","datastore.json")
INDEX = {"PATH" : 0, "SCRIPT" : 1, "ARGUMENT" : 2, "CONTRIBUTOR": 4, "DESCRIPTION" : 5}

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


def main():
    """Loads the script data, and runs the selected script"""

    # Load data from "datastore.json" file
    SCRIPTS = None
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

        with open(script_arr[INDEX["SCRIPT"]], 'r') as file:
            exec(file.read(), globals(), globals())


if __name__ == '__main__':
    main()