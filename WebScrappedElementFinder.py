import re
from bs4 import BeautifulSoup
from tabulate import tabulate
import requests


def print_class_lines():
    with open("Office.html", 'r') as file:
        for line in file:
            if "col-md-12 pt-3" in line:
                print(line.strip())


def print_class_lines_using_regex():
    with open("Office.html", 'r') as file:
        office_content = file.read()

    # Use regex to find all occurrences of "col-md-12 pt-3" class
    pattern = r'class="col-md-12 pt-3"'
    matches = re.findall(pattern, office_content)

    # Print all matched lines
    for match in matches:
        print(match)


def print_class_lines_using_for():
    with open("Office.html", 'r') as file:
        office_content = file.read()

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(office_content, 'html.parser')

    # Find all elements with the class "col-md-12 pt-3"
    elements_with_class = soup.find_all(class_="col-md-12 pt-3")

    # Print the lines containing the class
    for element in elements_with_class:
        print(element)


def print_file_as_table():
    with open("Office.html", 'r') as file:
        office_content = file.read()

    soup = BeautifulSoup(office_content, 'html.parser')

    element = soup.find(class_="col-md-12 pt-3")

    table = element.find('table')

    rows = []
    headers = []

    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all(['th', 'td']):
            row_data.append(cell.text.strip())
        if not headers:
            headers = row_data
        else:
            rows.append(row_data)

    if headers and rows:
        if rows:
            rows = rows[:-1]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No data found in the table.")


def scrape_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# def crawl_webpage(url):
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         links = soup.find_all('a', href=True)
#
#         for link in links:
#             print(link['href'])
#
#     else:
#         print(f"Failed to fetch the webpage. Status code: {response.status_code}")


# crawl_webpage('https://webscraper.io/')


def parse_html_for_href_and_p_tags(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract href (anchor) tags
        href_links = []
        anchor_tags = soup.find_all('a')
        for tag in anchor_tags:
            if 'href' in tag.attrs:
                href_links.append(tag['href'])

        # Extract text content from p (paragraph) tags
        # paragraphs = [tag.get_text() for tag in soup.find_all('p')]

        # Printing the extracted data
        print("Anchor tags (href links):")
        for link in href_links:
            if link == 'javascript:void(0)':
                print()
            else:
                if '//' in link:
                    print('https://' + link[2:])
                else:
                    print(link)
        # web browser.open("https://www.thankyou.com/cms/thankyou/")
        # print("\nParagraph tags:")
        # for paragraph in paragraphs:
        #     print(paragraph)

    except Exception as e:
        print("Error occurred while parsing the HTML:", e)
        return
