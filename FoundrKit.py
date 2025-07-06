def exclude_first_column(input_file):
    import csv

    # Read the data from the input file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = [row[1:] for row in reader]

    # Write the updated data back to the same input file
    with open(input_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def save_items_as_csv():
    import pandas as pd

    data = {
        "Name": names,
        "Company": companies,
        "Course": courses,
        "Location": locations,
        "Page": pages,
        "Success Story": sob_stories
    }

    df = pd.DataFrame(data)

    with open("Foundr Success Stories.csv", 'w') as file:
        file.write(df.to_csv())

    exclude_first_column("Foundr Success Stories.csv")

    from subprocess import Popen
    Popen('Foundr Success Stories.csv', shell=True)


def get_stories():
    from bs4 import BeautifulSoup
    import requests

    response = requests.get(
        "https://foundr.com/success-stories",
        headers={
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/115.0.0.0 Safari/537.36'
        }
    )

    response.raise_for_status()
    soup = BeautifulSoup(response.content, features='html.parser', from_encoding='ascii')
    content = soup.findAll(class_="row row-flex grid-row")

    a, b, location_soup = soup.findAll(class_='filter-select')
    location_dict = {}
    for location in location_soup:
        if str(location).__contains__('<option value='):
            location_dict[location['value'].replace('.', '')] = location.text

    for success_stories in content:
        for story in success_stories:
            if str(story).__contains__('<a class="story-item" href='):
                company = story.find(class_='media-name media-name--story').span.string

                names.append(story.find(class_='media-name media-name--story').text.replace(company, ""))

                companies.append(company)

                pages.append(story.find(class_='story-item')['href'])

                sob_stories.append(story.find(class_='story-description').text)

                courses.append(story.find(class_='course_name').text.replace('Course: ', ''))

                flag = True
                for key in location_dict.keys():
                    if str(story).__contains__(key):
                        locations.append(location_dict[key])
                        flag = False
                        break
                if flag:
                    locations.append('Unknown')

    save_items_as_csv()


if __name__ == '__main__':
    names = []
    pages = []
    companies = []
    courses = []
    locations = []
    sob_stories = []

    get_stories()
