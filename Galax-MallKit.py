from bs4 import BeautifulSoup
import requests
import pandas as pd
from requests.exceptions import HTTPError
import csv


def exclude_first_column(input_file):
    # Read the data from the input file
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = [row[1:] for row in reader]

    # Write the updated data back to the same input file
    with open(input_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def save_items_as_csv():
    for link in product_links:
        response = requests.get(link)
        response.raise_for_status()
        bisque = BeautifulSoup(response.content, 'html.parser')
        if bisque.find(class_='tab-panels'):
            product_descriptions.append(bisque.find(class_='tab-panels').get_text(strip=True))
        else:
            product_descriptions.append("None")

    data = {
        "Product Title": product_titles,
        "Product Type": product_types,
        "Price": product_prices,
        "Description": product_descriptions,
        "Link": product_links
    }

    df = pd.DataFrame(data)

    with open("Galax-mall.csv", 'w', encoding="utf-8") as file:
        file.write(df.to_csv())

    exclude_first_column("Galax-mall.csv")

    from subprocess import Popen
    Popen('Galax-mall.csv', shell=True)


def get_items(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find(class_='products row row-small large-columns-4 medium-columns-3 small-columns-2')

        for item in table:
            tag = item.find('a')
            product_links.append(tag['href'])
            product_types.append(item.find('p').get_text(strip=True))
            product_prices.append(item.find(class_='woocommerce-Price-amount amount').get_text(strip=True))
            product_titles.append(item.find(class_='name product-title').get_text(strip=True))
        return True
    except HTTPError as e:
        print(e)
        return False


if __name__ == "__main__":
    i = 1
    product_links = []
    product_types = []
    product_prices = []
    product_titles = []
    product_descriptions = []
    while True:
        print(i)
        flag = get_items(f'https://galax-mall.com/shop/page/{i}')
        if not flag:
            print("All Done!")
            break
        i += 1

    save_items_as_csv()
