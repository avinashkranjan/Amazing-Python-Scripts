# Fetch contributions

It's a Python script to fetch the pull requests made by a github user in an Organization. It helps organization members to keep record of a particular 
github user requests and also helps the github user to record the pull requests made to the organization. 

- Script can be executed as a CLI.
- Takes arguments username and organization.
- Returns the pull requests made by user to the organization into a Markdown file. 	
	- Markdown file consists a table having - "Title of PR" , "Link of PR" , "Status(Merged/Closed/Open)"

## Example Markdown File:

|    | Title of PR                                               | Link of PR                                                            | Status(Merged/Closed/Open)   |
|---:|:----------------------------------------------------------|:----------------------------------------------------------------------|:-----------------------------|
|  0 | Title of the pull request made by user   | Link to the Pull request                | Status of the pull request                       |
***
## Setup Instructions:

```bash
git clone <link>
cd Fetch_contributions/
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 fetch_contributions.py --username <Username> --organization <Organization>
```
