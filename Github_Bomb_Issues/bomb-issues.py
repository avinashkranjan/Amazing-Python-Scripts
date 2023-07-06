from github import Github
import os
import getpass

username = input("Enter your username: ")
password = getpass.getpass("Enter your Github password: ")
g = Github(username, password)

repository = input(
    "Give the GitHub repository name that you want to bomb issues on (Example: Ayush7614/Hello-World-): "
)
number = int(input("Give the number of issues that you want to bomb: "))
repo = g.get_repo(repository)

for x in range(number):
    repo.create_issue(
        title="Lorem ipsum",
        body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    )
