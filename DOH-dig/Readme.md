# DNS-over-HTTPS (DoH) Dig

DNS-over-HTTPS (DoH) Dig is a command-line tool for performing DNS queries using DNS-over-HTTPS with Cloudflare DNS.

## Features

- Query various DNS record types: A, MX, PTR, SRV, TXT, NS
- Perform reverse DNS lookups (PTR records) for IP addresses
- Retrieve DNS records securely using DNS-over-HTTPS
- Simple and easy-to-use command-line interface


## Options

- `-h --help`: Show the help screen.
- `--version`: Show the version.

## Usage

  doh-dig type <type> <record> 
  doh-dig ptr <ip>
  doh-dig (-h | --help)
  doh-dig --version

## requirements

  docopt
  requests

## Prerequisites

- Python 3.x

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository or download the `doh-dig.py` file to your local machine.

## Setup

1. Open a terminal or command prompt.
2. Navigate to the directory where `doh-dig.py` is located.




