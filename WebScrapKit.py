import requests
from bs4 import BeautifulSoup


def scrape_text_from_url(url):
    try:
        # Fetch the web page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for invalid responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    bisque = scrape_text_from_url(input("Enter the URL to scrape text from: "))
    if bisque:
        # Step 1: Open the file in write mode
        with open("Office.html", "w") as file:
            try:
                # Step 2: Write the HTML content to the file
                file.write(str(bisque))
            except UnicodeEncodeError as e:
                print(f"Error printing scraped text: {e}")
