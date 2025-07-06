from bs4 import BeautifulSoup
import pandas as pd
import requests
import csv


def create_hyperlink(element):
    return f"https://{element}"


def convert_first_column_to_hyperlinks(input_file):
    with open(input_file, 'r') as file:
        # Read the CSV data into a list of dictionaries
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    # Modify the data in memory
    for row in data:
        row['Website'] = create_hyperlink(row['Website'])

    with open(input_file, 'w', newline='') as file:
        # Write the updated data back to the CSV file
        fieldnames = data[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def exclude_first_column(input_file):
    # Read the data from the input file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = [row[1:] for row in reader]

    # Write the updated data back to the same input file
    with open(input_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def save_url_as_csv(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find(class_="col-md-12 pt-3")
    table = element.find('table')

    df = pd.read_html(str(table))[0]

    if not df.empty:
        df = df.iloc[:-1]
        df = df.drop(df.columns[0], axis=1)
        # Drop the last column from the DataFrame
        df = df.iloc[:, :-1]
        # Step 1: Identify columns without headers
        columns_without_headers = [col for col in df.columns if col == ""]
        # Step 2: Drop columns without headers
        df.drop(columns_without_headers, axis=1, inplace=True)
        # Set the display options to show all rows and columns
        pd.set_option('display.max_rows', None)  # Show all rows
        pd.set_option('display.max_columns', None)  # Show all columns

    with open("tables.csv", 'w') as file:
        file.write(df.to_csv())

    exclude_first_column("tables.csv")
    convert_first_column_to_hyperlinks('tables.csv')

    from subprocess import Popen
    Popen('tables.csv', shell=True)

    #     print(tabulate(df, headers='keys', tablefmt='psql'))
    # else:
    #     print("No data found in the table.")


if __name__ == "__main__":
    try:
        save_url_as_csv('https://trends.builtwith.com/websitelist/Responsive-Tables')
    except FileNotFoundError:
        print("Error: The file 'Office.html' was not found.")
    except Exception as e:
        print("Error occurred:", e)
