from bs4 import BeautifulSoup
import re


def get_strings_in_html_script(html):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all script tags in the HTML
    script_tags = soup.find_all('script')

    # Initialize a list to store the strings found in the scripts
    strings = []

    # Regular expression pattern to match strings within JavaScript code
    string_pattern = re.compile(r'("[^"\\]*(?:\\.[^"\\]*)*"|\'[^\'\\]*(?:\\.[^\'\\]*)*\')')

    # Loop through each script tag and extract strings using regular expressions
    for script_tag in script_tags:
        script_code = script_tag.string
        if script_code:
            strings.extend(re.findall(string_pattern, script_code))

    return strings


# Example HTML input
with open('Office.html', "r") as file:
    html_script = file.read()

# Get the strings in the HTML script
strings_in_script = get_strings_in_html_script(html_script)
print(strings_in_script)