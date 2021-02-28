import requests
import argparse


def main(args):
    GITHUB_URL = f" https://api.github.com/repos/{args.o}/{args.n}"
    res = requests.get(GITHUB_URL).json()
    response_collaborators = requests.get(f"{GITHUB_URL}/contributors").json()

    response_text = f"Size of repository is {res.get('size')}"

    list_of_contributors = []

    for x in response_collaborators:
        list_of_contributors.append(x.get("login"))

    with open("output.txt", "w") as text:
        text.write(response_text + "\n" +
                   "List of contributors is as follows: " +
                   str(list_of_contributors))


parser = argparse.ArgumentParser(
    "This script displays the size and list of contributors for a specific repo"
)
parser.add_argument("-o", help="The name of the user", type=str, required=True)
parser.add_argument("-n", help="The name of the repo", type=str, required=True)

args = parser.parse_args()

main(args)
