# DNS VERIFIER

import json
import sys
from collections import OrderedDict

import dns.resolver


def checker(dns_val=None) -> OrderedDict:

    ip_values = None
    avail = False

    if dns_val is None:
        raise ValueError("Sorry DNS not found, DNS is needed")
    if isinstance(dns_val, str) is False:
        raise TypeError("Sorry, \'DNS\' must be type \'str\'")
    try:
        output = dns.resolver.resolve(dns_val, 'A')
        ip_values = [ipval.to_text() for ipval in output]
    except dns.resolver.NXDOMAIN:
        avail = True

    return OrderedDict([
        ("DNS", dns_val),
        ("IP", ip_values),
        ("AVAIL", avail),
    ])


if __name__ == '__main__':
    dns_val = None
    option = None

    if len(sys.argv) > 1:
        if '--dns' in sys.argv:
            d_index = sys.argv.index('--dns')
            if d_index == sys.argv.index(sys.argv[-1:][0]):
                print("Error, DNS was not specified")
                sys.exit(1)
            dns_val = sys.argv[sys.argv.index('--dns') + 1]
        else:
            print("help:\nuse \'--dns\' for DNS specification")
            sys.exit(1)
    try:
        response = checker(dns_val=dns_val)
    except Exception as err:
        print(f"error: {err}")
        sys.exit(1)

    print(json.dumps(response, indent=4))
    sys.exit(0)