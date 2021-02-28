import repoInfo
from filechange import ischanged
from colors import logcolors
import pyfiglet
import logger
from utils import initCommands


def init():
    info = repoInfo.checkinfoInDir()
    url, branch = info
    logger.checkdata(url, branch)
    if ('n' in info):
        initCommands(info)
    else:
        print(
            f'{logcolors.BOLD}Retrieving info from git directory{logcolors.ENDC}'
        )
        print(
            f'{logcolors.CYAN}URL:{logcolors.ENDC} {url} , {logcolors.CYAN}Branch:{logcolors.ENDC} {branch}'
        )
        ischanged(url, branch)


if __name__ == '__main__':
    f = pyfiglet.figlet_format('G - AUTO', font='5lineoblique')
    print(f"{logcolors.BOLD}{f}{logcolors.ENDC}")
    init()
