from bs4 import BeautifulSoup


def search_html_file(file_path, tags, search_strings):
    with open(file_path, "r") as file:
        html_script = file.read()

    soup = BeautifulSoup(html_script, 'html.parser')

    results = {}
    for tag in tags:
        results[tag] = []
        elements = soup.find_all(tag)
        for element in elements:
            for search_string in search_strings:
                if search_string in element.get_text():
                    results[tag].append(element.get_text())
                    break

    return results


# User Input
file_path = "Office.html"
tags = input("Enter tags to search (separated by spaces): ").split()
search_strings = input("Enter search strings (separated by spaces): ").split()

# Get matching values
matching_values = search_html_file(file_path, tags, search_strings)

# Display the results
for tag, values in matching_values.items():
    print(f"Matching values for tag '{tag}':")
    for value in values:
        print(value)
    print()
