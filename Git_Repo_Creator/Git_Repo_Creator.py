import requests


def create_github_repo():
    user_name = input("Enter your GitHub user name: ")
    github_token = input("Enter your GitHub token: ")
    repo_name = input("Enter your repo Name: ")
    repo_description = input("Enter your repo description: ")

    payload = {'name': repo_name,
               'description': repo_description, 'auto_init': 'true'}
    repo_request = requests.post(
        f'https://api.github.com/user/repos', auth=(user_name, github_token), json=payload)

    if repo_request.status_code == 422:
        print("GitHub repo already exists. Try with another name.")
    elif repo_request.status_code == 201:
        print("GitHub repo has been created successfully.")
    elif repo_request.status_code == 401:
        print("You are an unauthorized user for this action.")
    else:
        print(
            f"Error creating GitHub repo. Status code: {repo_request.status_code}")


if __name__ == "__main__":
    print("GitHub Repo Creator\n")
    create_github_repo()
