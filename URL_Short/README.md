# UrlShortener 
[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)     
[![Build Status](https://travis-ci.org/p53ud0k0d3/UrlShortener.svg?branch=master)](https://travis-ci.org/p53ud0k0d3/UrlShortener)     [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A Django web app that shortens long urls. User may select from a list of available hosts. 

#### Available Hosts
- Tinyurl
- Is.gd
- Bit.ly
- Google URL Shortener
- Rebrand.ly

## Pre-reqs

[Virtualenv](https://virtualenv.pypa.io/en/stable/) - Install required packages in a virtual environment. Not necessary, but recommended. 

## Installation

1. `virtualenv YOURENVNAME` - Create new virtualenv for this project
2. Navigate to directory containing 'requirements.txt'
3. `pip install -r requirements.txt` - Install required packages

## Usage


On first usage you'll need to apply database migrations: `python manage.py migrate`

Otherwise run development server using: `python manage.py runserver`

## Testing

Tests are run using `pytest`

For more information: [pytest](https://docs.pytest.org/en/latest/contents.html)


## Contributions
### Getting Started
1. Create a fork and then clone your fork of the repo
2. Follow steps for [Installation](#installation)
3. Ensure project runs: [Usage](#usage)
4. Ensure tests pass: [Testing](#testing)
5. Implement your changes along with tests for your change
6. Push changes to your fork and submit a pull request


### Adding a new host
This project uses the pyshorteners library for url shortening, read their documentation for more information on implementing a new host: [pyshorteners](http://www.ellison.rocks/pyshorteners/)

### Docker
1. Clone repository
2. Make sure you have execute permission on run.sh and Docker is installed (Linux, 'chmod +x run.sh' in the repo)
3. Run run.sh like ' ./run.sh ' 
4. Visit localhost:8000 and watch it run
