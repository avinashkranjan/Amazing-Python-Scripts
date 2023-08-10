import requests


def get_repository_contents(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to fetch repository contents. Status code: {response.status_code}")
        return None


def extract_parent_folder(script_path):
    return script_path.rsplit("/", 1)[0]


def filter_items_by_keyword(contents, keyword, repo_owner, repo_name):
    filtered_items = []
    repo_url = f"https://github.com/{repo_owner}/{repo_name}"

    for item in contents:
        item_name = item["name"].lower()
        item_type = item["type"]

        if keyword.lower() in item_name:
            if item_type == "file":
                filtered_items.append((item_name, item["html_url"]))
            elif item_type == "dir":
                filtered_items.append((item_name, item["html_url"]))

    return filtered_items


if __name__ == "__main__":
    # Replace with your GitHub repository details
    owner = "avinashkranjan"
    repo = "Amazing-Python-Scripts"

    # Get repository contents
    contents = get_repository_contents(owner, repo)

    if contents:
        search_keyword = input(
            "\nEnter the keyword to search for in the scripts: ")
        found_items = filter_items_by_keyword(
            contents, search_keyword, owner, repo)

        if found_items:
            print("\nFound items matching the keyword:\n")
            for idx, (item_name, item_url) in enumerate(found_items, start=1):
                print(f"{idx}) {item_name} ({item_url})")
            print("\n")
        else:
            print("No items found matching the keyword.")
