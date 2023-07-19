import requests
import decouple

req_headers = {}


def godaddy_credentials():
    """
    This functions reads your credentials from .env file
    """
    global req_headers

    print("\n\t::: Reading Godaddy Credentials :::")

    api_key = decouple.config("API_KEY")
    api_secret = decouple.config("API_SECRET")
    # api_key = input("\nEnter your API Key: ")
    # api_secret = input("Enter your SECRET Key: ")

    req_headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "accept": "application/json",
    }


def get_url(domain_name):
    """
    creating the required URL from domain name
    :param domain_name: (string) domain name
    :return: URL
    """
    return f"https://api.ote-godaddy.com/v1/domains/suggest?query={domain_name}&country=IN&waitMs=1000"


def available_domain_names():
    """
    This function takes godaddy credentials from the user and generates all the
    available domain names in a text file.
    """
    godaddy_credentials()
    domain_name = input("\nEnter required DOMAIN Name: ")
    url = get_url(domain_name)

    print("\nSearching for the available domains")
    res = requests.get(url, headers=req_headers)

    if res.status_code == 200:
        # Output is in JSON file so reading it.
        response = res.json()

        # Saving our available domains in a text file.
        print(f"\nSaving all the available domain names in {domain_name}.txt file")
        f = open(f"{domain_name}.txt", "a")
        for i in response:
            f.writelines(i["domain"] + "\n")
        f.close()
        print(f"\nFile {domain_name}.txt saved successfully in your current directory")

    else:
        print("Error Status Code")


if __name__ == "__main__":
    available_domain_names()