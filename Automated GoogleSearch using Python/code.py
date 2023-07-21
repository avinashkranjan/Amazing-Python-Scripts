from googlesearch import search
import sys


class googlesearch:

    def __init__(self):
        self.search_count = None
        self.keyword_to_search = None
        self.search_results = None

    def set_search_count(self):
        # Set the number of search results to display
        print("Enter the count of search results you want to display:")
        count = int(input())
        self.search_count = count

    def set_search_text(self):
        # Set the keyword to search on Google
        print("Enter the text you want to search on Google:")
        text = input()
        self.keyword_to_search = text

    def perform_search(self):
        try:
            # Perform the Google search
            results = search(self.keyword_to_search,
                             num_results=self.search_count)
            self.search_results = results
        except Exception as e:
            print(e)
            print("Google search faced an exception")

        print("Google search performed successfully")

    def print_search_res(self):
        print("The search results for {} keyword are:".format(
            self.keyword_to_search))

        count = 1
        for search_res in self.search_results:
            # Print the search results
            print("Search No {}: {}".format(count, search_res))
            count += 1


def main():
    google_search_bot = googlesearch()

    while True:
        print("Select any one of the valid operations which are listed below:")
        print("1. To set the number of searches we need to display for each Google Search.")
        print("2. To enter the keyword for the Google Search.")
        print("3. To perform Google Search for the keyword entered by the user.")
        print("4. To print the Google search results obtained after searching.")
        print("5. To exit from the code execution.")

        choice = int(input(''))

        if choice == 1:
            google_search_bot.set_search_count()
        elif choice == 2:
            google_search_bot.set_search_text()
        elif choice == 3:
            google_search_bot.perform_search()
        elif choice == 4:
            google_search_bot.print_search_res()
        else choice == 5:
            sys.exit()

        print("To continue with the code execution, enter 'y' or 'n':")
        continue_or_exit = input()

        if continue_or_exit == 'n' or continue_or_exit == 'N':
            sys.exit()


if __name__ == '__main__':
    main()
