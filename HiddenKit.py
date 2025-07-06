from bs4 import BeautifulSoup


def get_strings_in_html_script(bisque):
    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(bisque, 'html.parser')

    # Find all script tags in the HTML
    script_tags = soup.find_all('script')

    # Initialize a list to store the strings found in the scripts
    strings = []

    # Loop through each script tag and extract strings using string manipulation
    for script_tag in script_tags:
        script_code = script_tag.string
        if script_code:
            strings.extend(extract_strings_from_js_code(script_code))

    return strings


def extract_strings_from_js_code(js_code):
    # Initialize a list to store the extracted strings
    strings = []

    # Characters that can indicate the start of a string
    string_delimiters = ['"', "'"]

    # Loop through the code to find strings
    i = 0
    while i < len(js_code):
        char = js_code[i]

        if char in string_delimiters:
            # Find the end of the string
            end_index = js_code.find(char, i + 1)

            if end_index != -1:
                # Extract the string and add it to the list
                extracted_string = js_code[i:end_index + 1]
                strings.append(extracted_string)
                i = end_index + 1

            else:
                # If the end of the string is not found, move to the next character
                i += 1

        else:
            # Move to the next character
            i += 1

    return strings


# Example HTML input
with open('Office.html', "r") as file:
    html_script = file.read()

# Get the strings in the HTML script
strings_script = get_strings_in_html_script(html_script)
print(strings_script)
