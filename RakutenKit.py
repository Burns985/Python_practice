from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser
import csv
import requests
import re


def exclude_first_column(input_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = [row[1:] for row in reader]

    with open(input_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def save_items_as_csv():
    data = {
        "Name": item_names,
        "Price": item_prices,
        "Reviews": item_reviews,
        "Page": item_pages
    }

    df = pd.DataFrame(data)
    # Save DataFrame to an Excel file
    excel_filename = "Rakuten.xlsx"
    df.to_excel(excel_filename, index=False)

    # Open the Excel file using the default program associated with .xlsx files
    webbrowser.open(excel_filename)


def scrap_url(url):
    session = requests.Session()

    response = session.get(url)
    page_source = response.content
    soup = BeautifulSoup(page_source, 'html.parser')

    if soup.find(class_='risfAllPages'):
        pages = soup.find(class_='risfAllPages').text.strip()
        start, end, total = map(int, re.findall(r'\d+', pages))
        items_per_page = end - start + 1
        num_pages = (total + items_per_page - 1) // items_per_page

        if num_pages == 1:
            tables = soup.find(id='risFil').findAll('table')[1].findAll('tr')[1::2]

            for item_set in tables:
                for item in item_set:
                    if item.find(class_='category_itemnamelink'):
                        item_names.append(item.find(class_='category_itemnamelink').text.strip())
                        item_pages.append(item.find(class_='category_itemnamelink')['href'])
                        item_prices.append(item.find(class_='category_itemprice').text.strip())
                        if item.find(class_='risfClfx'):
                            item_reviews.append(item.find(class_='risfClfx').text.strip())
                        else:
                            item_reviews.append('N/A')
                    else:
                        return
        else:
            session.close()
            count = 0
            for i in range(1, num_pages + 1):
                session = requests.Session()

                response = session.get(url + f'?p={i}&s={i}#risFil')

                page_source = response.content
                bisque = BeautifulSoup(page_source, 'html.parser')

                tables = bisque.find(id='risFil').findAll('table')[1].findAll('tr')[1::2]

                for item_set in tables:
                    if count == 85:
                        break
                    for item in item_set:
                        if count == 85:
                            break
                        count += 1
                        item_names.append(item.find(class_='category_itemnamelink').text.strip())
                        item_pages.append(item.find(class_='category_itemnamelink')['href'])
                        item_prices.append(item.find(class_='category_itemprice').text.strip())
                        if item.find(class_='risfClfx'):
                            item_reviews.append(item.find(class_='risfClfx').text.strip())
                        else:
                            item_reviews.append('N/A')
    else:
        return


def scrap_urls(urls):
    for url in urls:
        print(url)
        scrap_url(url)
    save_items_as_csv()


def get_response():
    response = get(url='https://www.rakuten.ne.jp/gold/cricut/cricut.html',
                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    tabs = soup.findAll(class_='header-cat-item')
    urls = []
    for tab in tabs:
        urls.append(tab.find('a')['href'])
    return urls


if __name__ == '__main__':
    item_names, item_reviews, item_prices, item_pages = [], [], [], []
    try:
        scrap_urls(get_response())
    except Exception as e:
        print(len(item_names), len(item_reviews), len(item_prices), len(item_pages))
        print('Error Message:', e)
