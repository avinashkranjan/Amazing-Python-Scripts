# IMPORTS
import requests
import argparse
import sys


def parser_input():
    """
    Function for Parsing the CLI input
    :return: parser.parse_args()  Parsed Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-u",
                        "--usernames",
                        help="Enter the username.",
                        type=str,
                        required=True)
    parser.add_argument("-t",
                        "--targets",
                        help="Enter the website(s). Use Lowercase only",
                        type=str,
                        required=True,
                        nargs='+')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()


def inputs(usernames, targets):
    """
    Takes the various Inputs, Iterates over dictionary and invokes the search_web function
    :param usernames: Username to be searches across the platforms
    :param targets: The target websites. [nargs = '+', takes multiple inputs]
    """
    username = usernames
    target = targets

    websites = {
        "instagram": f'https://www.instagram.com/{username}',
        "facebook": f'https://www.facebook.com/{username}',
        "twitter": f'https://twitter.com/{username}',
        "youtube": f'https://www.youtube.com/{username}',
        "reddit": f'https://www.reddit.com/user/{username}',
        "blogger": f'https://{username}.blogspot.com',
        "github": f'https://www.github.com/{username}',
        "steam": f'https://steamcommunity.com/id/{username}',
        "soundcloud": f'https://soundcloud.com/{username}',
        "medium": f'https://medium.com/@{username}',
        "spotify": f'https://open.spotify.com/user/{username}',
        "patreon": f'https://www.patreon.com/{username}',
        "bitbucket": f'https://bitbucket.org/{username}',
        "goodreads": f'https://www.goodreads.com/{username}',
        "wikipedia": f'https://www.wikipedia.org/wiki/User:{username}',
        "slack": f'https://{username}.slack.com'
    }

    for key in websites.keys():
        keys = str(key)
        if keys == target:
            search_web(username, websites[keys])


def search_web(username, target_website):
    """
    The search web function
    :param username: Username to be searches across the platforms
    :param target_website: The targetted website
    """
    r = requests.get(target_website)
    if r.status_code == 200:
        print('Got it ' + username + ' in ' + target_website)
    elif r.status_code == 400:
        print('Error 400, Bad Request for ' + username + ' at ' +
              target_website + ' check the Syntax of the URL')
    elif r.status_code == 404:
        print('Error 404, Not Found ' + username + ' at ' + target_website)
    else:
        print('There seems to be a issue ' + username + ' at ' +
              target_website + ' is not responding. Check the'
              ' syntax of the URL.')


if __name__ == '__main__':
    print(
        "Hello User, Using this script, yu can search for usernames across social media networks.\n"
        "Important, enter only one username at once.\n"
        "Enter as many as required supported platforms (SEE README).\n"
        "Enter the platform in lower case. ONLY.\n")
    arg = parser_input()
    for i in range(len(arg.targets)):
        inputs(arg.usernames, arg.targets[i])
