from bs4 import BeautifulSoup


def get_strings_in_html_script(html):

    strings = []

    soup = BeautifulSoup(html, 'html.parser')
    script_tags = soup.find_all('script')

    for script_tag in script_tags:
        script_code = script_tag.string
        if script_code:
            strings.extend(extract_strings_from_js_code(script_code))

    return strings


def extract_strings_from_js_code(js_code):

    strings = []
    string_bounds = ['"', "'"]
    i = 0

    while i < len(js_code):
        char = js_code[i]
        if char in string_bounds:
            end_index = js_code.find(char, i + 1)
            if end_index != -1:
                extracted_string = js_code[i:end_index + 1]
                strings.append(extracted_string)
                i = end_index + 1
            else:
                i += 1
        else:
            i += 1

    return strings


with open('Office.html', "r") as file:
    html_script = file.read()

print(get_strings_in_html_script(html_script))

# strings_script = get_strings_in_html_script(html_script)
# for script in strings_script:
#     print(script, end="\n")
