import subprocess
import argparse

parser = argparse.ArgumentParser(description="Troubleshoot Network errors")
group = parser.add_mutually_exclusive_group()
group.add_argument('-i', '--ipreset', type=bool, help="Reset TCP/IP configs")
group.add_argument('-s', '--sockreset', type=bool, help="Fix socket errors")
parser.add_argument('-r', '--restart', action='store_true')
args = parser.parse_args()


def resetIp():
    subprocess.run('netsh int ip reset')


def socketFix():
    subprocess.run('netsh winsock reset')


def restart():
    subprocess.run(["shutdown", "-r"])


if __name__ == '__main__':
    if args.ipreset:
        resetIp()
    elif args.sockreset:
        socketFix()
    if args.restart:
        restart()
