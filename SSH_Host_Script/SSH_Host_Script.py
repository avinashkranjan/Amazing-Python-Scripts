import argparse
import os

SSH_TEMPLATE = """
HOST {name}
    HostName {hostname}
    User {user}
    Port {port}
"""


def args_to_obj(args):
    return SSH_TEMPLATE.format(**args.__dict__)


def add_to_conf(conf, obj):
    conf = os.path.expanduser(conf)
    with open(conf, 'a') as f:
        f.write(obj)


def main():
    parser = argparse.ArgumentParser(
        prog="Adds ssh hosts to the ssh config file.")
    parser.add_argument('name', help="Name of the Host to add to the config.")
    parser.add_argument('hostname', help="Hostname/IP address of the host.")
    parser.add_argument('--user', default='root',
                        help="The user to connect with. Defaults to root.")
    parser.add_argument('--port', default=22, type=int,
                        help="The port to connect to. Defaults to 22.")
    parser.add_argument('--conf', default='~/.ssh/config',
                        help="The path to the ssh config file. Defaults to ~/.ssh/config.")

    args = parser.parse_args()
    obj = args_to_obj(args)
    add_to_conf(args.conf, obj)


if __name__ == '__main__':
    main()
