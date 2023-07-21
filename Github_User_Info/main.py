import requests
import argparse


def main(args):
    URL = f"https://api.github.com/users/{args.u}"
    res = requests.get(URL).json()
    output = ""
    output += "Username: "+res['login']
    if (res['name']):
        output += "\nName: "+res['name']
    if (res['bio']):
        output += "\nBio: "+res['bio']
    if (res['email']):
        output += "\nEmail: "+res['email']
    output += "\nFollowers: "+str(res['followers'])
    output += "\nFollowing: "+str(res['following'])

    print(output)
    with open(f"{res['login']}.txt", "w") as f:
        f.write(output)
        print(f"Output written in {res['login']}.txt")


parser = argparse.ArgumentParser(
    "This Script lists info about the github user"
)
parser.add_argument("-u", help="The name of the user", type=str, required=True)

args = parser.parse_args()
main(args)
