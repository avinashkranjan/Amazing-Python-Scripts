import os
import git
import requests
import shutil

# Configuration
local_solution_folder = r'/path/to/your/solution/folder'  # Path to your local solutions folder
repo_url = "https://github.com/YourUsername/YourRepo.git"  # URL of the GitHub repository
local_repo_folder = r'/path/to/your/local/repo/folder'  # Path to your local repository folder
github_api_url = "https://api.github.com/repos/YourUsername/YourRepo/contents/"  # GitHub API URL for the repository contents

# Function to clone the repository if it does not exist
def clone_repo_if_needed(repo_url, local_repo_folder):
    """
    Clone the repository if it does not already exist locally.
    
    :param repo_url: URL of the GitHub repository.
    :param local_repo_folder: Local folder where the repository will be cloned.
    """
    # Ensure the parent directory exists
    parent_dir = os.path.dirname(local_repo_folder)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    
    if not os.path.exists(local_repo_folder):
        print(f"Cloning repository from {repo_url} to {local_repo_folder}")
        git.Repo.clone_from(repo_url, local_repo_folder)
    else:
        print(f"Repository already exists at {local_repo_folder}")

# Function to fetch the list of files in the GitHub repository
def get_github_files(api_url):
    """
    Fetch the list of files in the GitHub repository.
    
    :param api_url: GitHub API URL for the repository contents.
    :return: List of file names in the repository.
    """
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to get the repository contents: {response.status_code}")
    return [file['name'] for file in response.json()]

# Function to copy new files to the local repository folder
def copy_new_files_to_repo(solution_folder, repo_folder, github_files):
    """
    Copy new files from the local solution folder to the local repository folder.
    
    :param solution_folder: Path to the local solutions folder.
    :param repo_folder: Path to the local repository folder.
    :param github_files: List of file names already in the GitHub repository.
    :return: List of new files copied.
    """
    new_files = []
    for file_name in os.listdir(solution_folder):
        if file_name not in github_files:
            src_path = os.path.join(solution_folder, file_name)
            dst_path = os.path.join(repo_folder, file_name)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
                new_files.append(file_name)
    return new_files

# Function to commit and push new files to the repository
def commit_and_push_changes(repo, files_to_commit):
    """
    Commit and push new files to the GitHub repository.
    
    :param repo: The Git repository object.
    :param files_to_commit: List of new files to commit.
    """
    if files_to_commit:
        repo.index.add(files_to_commit)
        repo.index.commit('Add new solutions')
        origin = repo.remotes.origin
        origin.push()
        print(f"Committed and pushed {len(files_to_commit)} files.")
    else:
        print("No new files to commit.")

# Main execution
def main():
    """
    Main function to execute the script workflow:
    1. Clone the repository if needed.
    2. Fetch the list of files in the GitHub repository.
    3. Copy new files from the local solution folder to the local repository folder.
    4. Commit and push new files to the GitHub repository.
    """
    clone_repo_if_needed(repo_url, local_repo_folder)
    repo = git.Repo(local_repo_folder)
    github_files = get_github_files(github_api_url)
    new_files = copy_new_files_to_repo(local_solution_folder, local_repo_folder, github_files)
    commit_and_push_changes(repo, new_files)

if __name__ == "__main__":
    main()
