import argparse

import pandas as pd
import requests
from bs4 import BeautifulSoup
from lxml import html
from tabulate import tabulate


class Fetch_PullRequests:
    """
    Fetches the pull requests of a user in a organization.
    """

    def __init__(self, username, organization, filename):
        """
        :param username: github user
        :param organization: Organisation name
        :param filename: filename, it's optional
        """
        self.ORG_URL = f"https://github.com/orgs/{organization}/repositories"
        self.URL = f"https://github.com/{organization}"
        self.organization = organization
        self.username = username
        self.filename = filename

    def _list_of_repositories(self):
        """
        Function lists the repositories of the organisation.

        Returns
        -------
        list
                lists the repositories

        """
        page = requests.get(self.ORG_URL)
        tree = html.fromstring(page.content)
        number_of_pages = tree.xpath(
            '//*[@id="org-repositories"]/div/div/div[2]/div/em/@data-total-pages')
        Repositories = []
        if len(number_of_pages) == 0:
            Repositories.extend(tree.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "wb-break-all", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "d-inline-block", " " ))]/text()'))
        else:
            for number in range(1, int(number_of_pages[0]) + 1):
                page_ = requests.get(self.ORG_URL + f"?page={number}")
                tree = html.fromstring(page_.content)
                Repositories.extend(tree.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "wb-break-all", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "d-inline-block", " " ))]/text()'))

        return list(pd.Series(list(set(Repositories))).str.strip().values)

    def _extract_pullrequests(self, repo):
        """
        Function fetches the pull request of a repo.

        Parameters
        ----------
        repo: str
                repository name

        Returns
        -------
        pandas dataframe
                dataframe consists of columns - "Title to PR", "Link of PR", "Status(Merged/Closed/Open)"

        """
        # initializing the lists to store the title, link and status of the pull request
        Title = []
        Link = []
        Status = []
        URL = self.URL + f"/{repo}/pulls?q=is%3Apr+author%3A{self.username}"
        page = requests.get(URL)
        tree = html.fromstring(page.content)
        # to determine the number of pages
        number_of_pages = tree.xpath(
            '//*[@id="repo-content-pjax-container"]/div/div[6]/div/em/@data-total-pages')

        if len(number_of_pages) == 0:
            # Title.extend(tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "markdown-title", " " ))]/text()'))
            soup = BeautifulSoup(page.text, 'html.parser')
            # "Title may contain text in <code> tags. So,to handle it we use beautiful soup.
            for tag in soup.find_all('a', attrs={'class': 'markdown-title'}):
                Title.append(tag.text.strip())
            Link.extend(
                tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "markdown-title", " " ))]/@href'))
            Status.extend(tree.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "pl-3", " " ))]/span/@aria-label'))

        else:
            for number in range(1, int(number_of_pages[0]) + 1):
                URL = self.URL + \
                    f"/{repo}/pulls?page={number}&q=is%3Apr+author%3A{self.username}"
                page = requests.get(URL)
                tree = html.fromstring(page.content)

                # Title.extend(tree.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "markdown-title", " " ))]/text()'))
                soup = BeautifulSoup(page.text, 'html.parser')
                # Names = tree.xpath(
                #     '//*[contains(concat( " ", @class, " " ), concat( " ", "opened-by", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "Link--muted", " " ))]/text()')

                for tag in soup.find_all('a', attrs={'class': 'markdown-title'}):
                    Title.append(tag.text.strip())
                Link.extend(tree.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "markdown-title", " " ))]/@href'))
                Status.extend(tree.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "pl-3", " " ))]/span/@aria-label'))

        Data = {
            "Title to PR": Title,
            "Link of PR": Link,
            "Status(Merged/Closed/Open)": Status
        }

        # creating a dataframe with the above dictionary
        dataframe = pd.DataFrame.from_dict(Data)
        # dataframe.head()

        # make necessary changes to the columns of dataframe before returning it
        dataframe['Status(Merged/Closed/Open)'] = dataframe['Status(Merged/Closed/Open)'].astype(str).str.replace(
            " pull request",
            "", regex=False)
        if dataframe['Link of PR'].dtype != 'O':
            dataframe['Link of PR'] = dataframe['Link of PR'].astype(str)
        dataframe['Link of PR'] = 'https://github.com' + \
            dataframe['Link of PR']

        return dataframe

    def get_pullrequests(self):
        """
        Function pass the repo parameter to the "_extract_pullrequests" to fetch the pull requests of the particular repo.

        Returns
        -------
        str
                return str saying that the file is stored if markdown is not empty.

        """
        dataframe = pd.DataFrame()
        for repo in self._list_of_repositories():
            dataframe = dataframe.append(
                self._extract_pullrequests(repo), ignore_index=True)

        markdown = dataframe.to_markdown()

        if len(markdown) > 0:
            # creating a markdown file
            # markdown_file = open(f"{self.filename}.md", "w")
            with open(f"{self.filename}.md", "w") as markdown_file:
                markdown_file.write(markdown)

            return "Markdown File is successfully stored"

        return "No pull requests found !!"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", action="store_true")
    parser.add_argument(
        "user", type=str, help="The name of the user to get the pull requests")
    parser.add_argument("-o", "--organization", action="store_true")
    parser.add_argument("organization_name", type=str,
                        help="the organisation where user made the pull requests")
    parser.add_argument("-f", "--file", nargs="?")
    parser.add_argument("filename", type=str, nargs="?",
                        help="filename to store the markdown table")
    args = parser.parse_args()
    if args.filename:
        file_name = args.filename
    else:
        file_name = "Markdown_file"
    if args.username and args.organization:
        response = Fetch_PullRequests(
            args.user, args.organization_name, file_name)
        print(response.get_pullrequests())
    else:
        print("Please pass atleast two arguments: '--username', '--organisation'")
