"""
CP1404/CP5639 Practical
Wikipedia API program
"""

import wikipedia

def main():
    search_phrase = input("Enter a page title or search phrase: ")

    try:
        # Search and get the best match page
        page = wikipedia.page(search_phrase)

        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation error. There are multiple pages matching your input.")
        print("Here are some possible options:")
        for option in e.options[:5]:
            print("-", option)

    except wikipedia.exceptions.PageError:
        print("Page not found. Try another search phrase.")

if __name__ == "__main__":
    main()
