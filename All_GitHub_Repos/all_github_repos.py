#!/usr/bin/env python3

# to convert it into a script by running sudo chmod +x all_github_repos.py

import requests
import sys
from github import Github

# imports
# pip3/pip install PyGithub is installed to work with the contents of the Github repositories

username = sys.argv[1]
# reading the username as a commandline argument

url = f"https://api.github.com/users/{username}"

user_data = requests.get(url).json()
# to retrieve data contained in the url in json format


def repository_names(user):
    repo_names = []
    for repo in user.get_repos():
        repo_names.append(repo)
    return repo_names


# fetching the names of all the repositories


def repository_details(user):
    all_repo_details = []
    repo_names = repository_names(user)
    for repo in repo_names:
        repo_details = {}
        repo_details["Name"] = repo.full_name.split("/")[1]
        repo_details["Description"] = repo.description
        repo_details["Created on"] = repo.created_at
        repo_details["Programming language"] = repo.language
        repo_details["Forked"] = str(repo.forks) + " time(s)"
        all_repo_details.append(repo_details)
    return all_repo_details


# fetching the details of all the repositories


user = Github().get_user(username)

RD = repository_details(user)
# fetching the details of all repositories
# stored as a list of dictionaries

if __name__ == "__main__":
    for content in RD:
        # pprint.pprint(content)
        for title, description in content.items():
            print(title, ":", description)
        print(
            "\n-------------------------------------------------------------------------------------------------------------------\n"
        )
