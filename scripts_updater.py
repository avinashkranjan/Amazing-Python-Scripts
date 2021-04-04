# h3avren

# imports
import sys
from github import Github
from bs4 import BeautifulSoup
import requests

if(len(sys.argv) >  1):
    # access token
    token = sys.argv[1] # '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'
    repo_name = 'avinashkranjan/Amazing-Python-Scripts'
    files_to_be_excluded = sys.argv[2:]
    repo_contents = {}

    try:
        # creating an instance of Github
        gitHub = Github(token)
        repo = gitHub.get_repo(repo_name)
        # making a request for the Scripts.md file
        response = requests.get('https://github.com/avinashkranjan/Amazing-Python-Scripts/blob/master/SCRIPTS.md')
        if(response.status_code == 200):
            soup = BeautifulSoup(response.text,'lxml')
            # selecting the required table rows
            rows = soup.find_all('tr')[1:]
            # appending the data to a list
            projects_listed = [data.find_all('td')[1].text for data in rows]

            contents = repo.get_contents("")
            while(contents):
                script = contents.pop(0)
                if((script.type == 'dir') and (script.name not in projects_listed) and (script.name != '.github')):
                    file_names = {}
                    
                    file_names['description'] = script.repository.description
                    
                    top_contributor = script.repository.get_contributors()[0]    # gets an iterator with all details of the topmost contributor
                    # contributor details
                    contributor_profile_link =  top_contributor.html_url
                    file_names['contributor'] = contributor_profile_link
                    file_names['name'] = top_contributor.name

                    # other file links
                    for file in repo.get_contents(script.path):
                        file_names[file.name] = file.html_url
                    repo_contents[script.name] = file_names
            
            # removing files to be excluded from the repo_contents
            for key in files_to_be_excluded:
                repo_contents.pop(key,None)
            
            # writing to the SCRIPTS.md file
            start = len(projects_listed)
            end = len(projects_listed) 
            with open('SCRIPTS.md','a') as file:
                for serial_number,key in enumerate(repo_contents.keys(),start + 1):
                    project_description = repo_contents[key]['description']
                    name = repo_contents[key]['name']
                    profile_url = repo_contents[key]['contributor']
                    for filename in repo_contents[key]:
                        if(filename[-3:] == '.py'):
                            script_url = repo_contents[key][filename]
                            break
                    line_template = f'''| {serial_number}\. | {key} | {project_description}\. | [Take Me]({script_url}) | [{name}]({profile_url}) |''' 
                    file.write(line_template + '\n')
                    print('\r' + f'Added {key} to SCRIPT.md')
                    end = serial_number
            print(f'Successful with {end - start} addition(s)..!')
        else:
            print('Check your internet connection..!')
    except:
        print('Either wrong token entered or poor internet connection..!')
else:
    print('Please pass the token (and the files to be excluded if any).')