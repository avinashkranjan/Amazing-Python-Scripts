from github import Github
import json
import sys
import re

# Regex Patterns
category = r"- \[x\] (.+)"
name = r"Title: (.+)"
path = r"Folder: (.+)"
requirments_path = r"Requirements: (.+)"
entry = r"Script: (.+)"
arguments = r"Arguments: (.+)"
contributor = r"Contributor: (.+)"
description = r"Description: (.+)"


def add_script(category, name, path, entry, arguments, requirments_path, contributor, description, pa_token):
    """ Add a Contributor script to database """
    new_data = {category: {name: [path, entry, arguments, requirments_path, contributor, description]}}
    data_store = read_data()
    
    try:
        # If category doesn't exist try will fail and except will ask to add a new category with the project
        if data_store[category]:                                          # Check for existing category or a new one
                data_store[category].update(new_data[category])           # Add script
    except:
        data_store.update(new_data)                                       # Add new category

    # <----- This part is to avoid a single/double quotes error when trying to update the database with PyGithub ----->
    with open("./Master Script/datastore.json", "w") as file:
        json.dump(data_store, file)
    print("Script added to database, pushing changes to repo...")

    with open("./Master Script/datastore.json", "r") as file:
        data_store = file.readlines()[0]

    # <----- Github Login & Database Update ----->
    git = Github(pa_token)
    user_object = git.get_user()
    print("[+] PyGithub Login Success!")
    
    repo = git.get_repo("avinashkranjan/Amazing-Python-Scripts")
    datastore_fileMaster = repo.get_contents("./Master Script/datastore.json", ref="master")
    datastore_fileWebsite = repo.get_contents("./datastore.json", ref="gh-pages")
    
    repo.update_file(datastore_fileMaster.path, "Updated datastore.json", data_store, datastore_fileMaster.sha, branch="master")
    repo.update_file("./datastore.json", "Updated datastore.json", data_store, datastore_fileWebsite.sha, branch="gh-pages")
    print("[+] Database Updated")


def read_data():
    """ Loads datastore.json """
    with open("./Master Script/datastore.json", "r") as file:
        data = json.load(file)
    return data


def extract_from_pr_body(pr_body, pa_token):
    """ Manipulates the provided PR body and extracts the required information """
    pr_body = pr_body.split("\n")
    for element in pr_body:
        pr_body[pr_body.index(element)] = element.rstrip("\r")

    # A special case for contributors in gh-pages branch and other dependency PRs
    try:
        pr_body = pr_body[pr_body.index("## Project Metadata"):]
    except:
        sys.exit()
    
    category_list = []
    for text in pr_body:
        # <----- Validate Category ----->
        cat = re.match(category, text)
        if cat is not None:
            category_list.append(cat[1])
        # <----- Validate Title ----->
        if re.match(name, text) is not None:
            title = re.match(name, text)[1]
        # <----- Validate Folder ----->
        if re.match(path, text) is not None:
            folder = re.match(path, text)[1]
        # <----- Validate requirments.txt ----->
        if re.match(requirments_path, text) is not None:
            requirements = re.match(requirments_path, text)[1]
        # <----- Validate Script.py ----->
        if re.match(entry, text) is not None:
            script = re.match(entry, text)[1]
        # <----- Validate Arguments ----->
        if re.match(arguments, text) is not None:
            argument = re.match(arguments, text)[1]
        # <----- Validate Contribute ----->
        if re.match(contributor, text) is not None:
            user = re.match(contributor, text)[1]
        # <----- Validate Description ----->
        if re.match(description, text) is not None:
            desc = re.match(description, text)[1]

    # For GitHub Actions logging
    print("<----- MetaData ----->")
    print("Categories:", category_list)
    print("Title:", title)
    print("Path:", folder)
    print("Requirements:", requirements)
    print("Entry:", script)
    print("Arguments:",argument)
    print("Contributer:", user)
    print("Description:", desc)
    print("<----- ----- ----->")

    # The loop is for scripts that will be added to multiple categories.
    for cat in category_list:
        add_script(cat, title, folder, script, argument, requirements, user, desc, pa_token)


# Start Checkpoint
if __name__ == "__main__":
    # Get PR body and pass pa_token
    data = sys.argv[1]
    extract_from_pr_body(data, sys.argv[2])
