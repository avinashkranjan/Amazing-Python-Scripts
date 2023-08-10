import wikipediaapi


def get_wikipedia_content(page_title):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(page_title)

    if page.exists():
        return page.text
    else:
        return f"Page '{page_title}' does not exist on Wikipedia."


def main():
    page_title = input("Enter the Wikipedia page title: ")
    content = get_wikipedia_content(page_title)

    print(f"\nContent from Wikipedia for '{page_title}':\n")
    print(content)


if __name__ == "__main__":
    main()
