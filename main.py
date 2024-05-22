import requests
from bs4 import BeautifulSoup
from bs4.element import Comment


def extract_content(url):
    """Fetches and extracts information from a website, printing prettified HTML."""

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    print(soup.prettify())  # Print prettified HTML

    print(f"\nTitle: {soup.title.string}\n")

    print("Paragraphs:")
    for p in soup.find_all('p'):
        print(p.get_text())

    print("\n'Lead' Paragraphs:")
    for lead in soup.find_all('p', class_="lead"):
        print(lead.get_text())

    print("\nExternal Links:")
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('http'):
            print(href)

    # Comment Handling (Example)
    comment_example = soup.find(string=lambda text: isinstance(text, Comment))
    if comment_example:
        print("\nExample Comment:", comment_example)

    # Navigation Examples (using `find` and `select`)
    navbar = soup.find(id='navbarSupportedContent')
    if navbar:
        print("\nNavbar Contents:")
        for item in navbar.stripped_strings:
            print(item)
    else:
        print("\nNo navbar with id 'navbarSupportedContent' found.")

# --- Main Execution ---
if __name__ == "__main__":
    url = "https://www.codewithharry.com/"
    extract_content(url)

