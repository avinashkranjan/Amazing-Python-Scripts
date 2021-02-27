# Search_Username

This script of code, using `request` module, will  help to determine weather, a username exists on a platform or not.

## Setup

The script uses universal libraries. Still it is recommended to cross check by using command:

```bash
pip3 install argparse requests
```

- Setup a virtual environment.
- Run the command as stated above.
- Ready to launch.

## Usage

```bash
usage: search_user.py [-h] -u USERNAMES -t TARGETS [TARGETS ...]

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAMES, --usernames USERNAMES
                        Enter the username.
  -t TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
                        Enter the website(s). Use Lowercase only
```

## Sample Usage and Output

On the command line interface, use the following command 

```bash
$ python search_user.py -u vybhav_72954 -t instagram

Got it vybhav_72954 in https://www.instagram.com/vybhav_72954

$ python search_user.py -u vybhav_72954 -t instagram github

Got it vybhav_72954 in https://www.instagram.com/vybhav_72954
Error 404, Not Found vybhav_72954 at https://www.github.com/vybhav_72954

$ python search_user.py -u vybhav_72954 -t github

Error 404, Not Found vybhav_72954 at https://www.github.com/vybhav_72954
```

## Supported Platforms

The list of supported platforms can be found [here](./platfrom.txt)

## Author(s)

Made by [Vybhav Chaturvedi](https://www.linkedin.com/in/vybhav-chaturvedi-0ba82614a/)

### Disclaimer

Multiple request to a certain host within a short period of time can lead to a ban,
the author and the maintainers of the Repository condemn such usage of this script and in no way are responsible
for any mishaps.

With the increasing number of DDOS attacks, multiple hosts have started using their own APIs as a strict mode of
request transfer and communication, multiple of the supported platforms in future, might shift to APIs. (e.g. LinkedIN)

We recommend people to use APIs as they are the official means of communication, and follow the rules and guidelines.
