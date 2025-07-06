# Terminal Run command: chcp 65001
# coding: utf-8
from requests import get
from bs4 import BeautifulSoup


def get_response():
    response = get(url='https://cricut.com/en/shop')
    soup = BeautifulSoup(response.content, 'html.parser')

    areas = {
        'North America': soup.find(class_='cwg-vendorList-country cwg-accordionGroup col-xl-6 col-md-12 col-lg-12'),
        'Latin America': soup.find(class_='cwg-vendorList-country cwg-accordionGroup justify-content-center '
                                          'col-xl-6 col-md-12 col-lg-12'),
        'Middle East': soup.find(class_='cwg-vendorList-countries--europe justify-content-center col-xl-3 col-lg-4'),
        'Asia': soup.find(class_='cwg-vendorList-countries--asia justify-content-center col-xl-3 col-lg-4')
    }

    area_sites = {}

    for area_name, area in areas.items():
        rough = area.findAll(class_='country-list cwg-accordion-content')
        area_sites[area_name] = []

        for dough, countries in zip(rough, area.findAll(class_='cwg-iconWithCopy-copy')):
            links = dough.findAll('a')
            country_names = [country.text.strip() for country in countries]

            if len(links) > len(country_names):
                country_names = country_names * len(links)

            for link, country_name in zip(links, country_names):
                if 'href' in link.attrs:
                    area_sites[area_name].append((link['href'], country_name.strip()))

    return area_sites


def to_string(area_sites):
    try:
        for area, sites in area_sites.items():
            print(f"Sites in {area} area:")
            for site, country in sites:
                print(f"{site} - {country}")
            print()
    except Exception as e:
        print(f'\n\n{e}')


if __name__ == "__main__":
    area_country_sites = get_response()


def circuit_ca(url):
    from time import sleep
    from requests import get
    from bs4 import BeautifulSoup
    from selenium import webdriver

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
            "Name": item_names,
            "Badge": item_badges,
            "Rating": item_ratings,
            "No. of Reviews": item_reviews,
            "Price": item_prices,
            "Page": item_pages
        }

        df = pd.DataFrame(data)

        with open("CriCut Canada.csv", 'w') as file:
            file.write(df.to_csv())

        exclude_first_column("CriCut Canada.csv")

        from subprocess import Popen
        Popen('CriCut Canada.csv', shell=True)

    def get_response():
        response = get(url='https://cricut.com/en-ca/shop',
                       headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

        soup = BeautifulSoup(response.content, 'html.parser')
        tabs = soup.find(class_='nav-main__nav nav navbar-nav')

        urls = []
        for tab in tabs.find_all('li'):
            if str(tab.find('a')['href']).count('/') < 3:
                urls.append('https://cricut.com' + str(tab.find('a')['href']))

        urls.pop(1)
        # [print(url) for url in urls]

        return urls

    def scrap_url(url):
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(10)

        page_source = driver.page_source
        bisque = BeautifulSoup(page_source, 'html.parser')

        items = bisque.findAll(class_='product-grid__item js-product-grid__item')

        for item in items:
            badge_element = item.find(class_='product-badge product-badge--new')
            if badge_element:
                item_badges.append(badge_element.text.strip())
            else:
                item_badges.append("No Badge")

            name_element = item.find(class_='product-tile__title-link js-product-link')
            if name_element:
                item_names.append(name_element.text.strip())
            else:
                item_names.append("No Name")

            link_element = item.find(class_='product-tile__title-link js-product-link')
            if link_element:
                item_pages.append('https://cricut.com' + str(link_element['href']))
            else:
                item_pages.append("No Link")

            price_element = item.find(class_='price__value')
            if price_element:
                item_prices.append(price_element.text.strip())
            else:
                item_prices.append("No Price")

            rating_element = item.find(class_='bv_avgRating_component_container notranslate')
            if rating_element:
                item_ratings.append(rating_element.text.strip())
            else:
                item_ratings.append("No Rating")

            review_element = item.find(class_='bv_numReviews_text')
            if review_element:
                reviews_text = review_element.text.strip().replace('(', '').replace(')', '')
                item_reviews.append(reviews_text)
            else:
                item_reviews.append("No Reviews")

    def scrap_urls(urls):
        for ur in urls:
            scrap_url(ur)
        save_items_as_csv()

    if __name__ == '__main__':
        item_badges, item_names, item_pages, item_prices, item_ratings, item_reviews = [], [], [], [], [], []
        scrap_urls(get_response())


def br_imports():
    from requests import get
    from bs4 import BeautifulSoup

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
            "Name": item_names,
            "Price": item_prices,
            "Discount": item_discounts,
            "Page": item_pages
        }

        df = pd.DataFrame(data)

        with open("BR imports.csv", 'w') as file:
            file.write(df.to_csv())

        exclude_first_column("BR imports.csv")

        from subprocess import Popen
        Popen('BR imports.csv', shell=True)

    def scrap_url(url):
        import requests
        from bs4 import BeautifulSoup
        from time import sleep
        import math

        session = requests.Session()

        response = session.get(url)
        sleep(3)
        page_source = response.content
        soup = BeautifulSoup(page_source, 'html.parser')
        if len(soup.findAll(class_='toolbar-number')) == 2:
            loops = math.ceil(int(soup.findAll(class_='toolbar-number')[1].text) / 100)
        else:
            loops = math.ceil(int(soup.findAll(class_='toolbar-number')[2].text) / 100)

        for i in range(1, loops + 1):
            page_url = f'{url}?p={i}'
            print(page_url)
            response = session.get(page_url)
            sleep(3)

            page_source = response.content
            bisque = BeautifulSoup(page_source, 'html.parser')

            items = bisque.findAll(class_=['product-item'])
            count = 0
            for item in items:
                if count == 100:
                    break
                item_pages.append(item.find(class_='product-item-link')['href'])
                item_names.append(item.find(class_='product-item-link').text.strip())
                if len(item.findAll(class_='price-wrapper')) == 2:
                    item_prices.append(str(item.findAll(class_='price-wrapper')[1].text) + '-' + str(
                        item.findAll(class_='price-wrapper')[0].text))
                else:
                    item_prices.append(item.find(class_='price').text)
                if item.find(class_='product-label'):
                    item_discounts.append(item.find(class_='product-label').text)
                else:
                    item_discounts.append('None')
                count += 1

    def scrap_urls(urls):
        for url in urls:
            scrap_url(url)
        save_items_as_csv()

    def get_response():
        response = get(url='https://brimportaciones.com.uy/',
                       headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        tabs = soup.findAll(class_='ms-level0')

        urls = []
        for tab in tabs:
            urls.append('https://brimportaciones.com.uy/' + str(tab.find(class_='ms-label')['href']))

        return urls

    if __name__ == '__main__':
        try:
            item_discounts, item_names, item_pages, item_prices = [], [], [], []
            scrap_urls(get_response())
        except Exception as e:
            print(e)


def amazon_ae():
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
            "Name": item_names,
            "Price": item_prices,
            "Discount": item_ratings,
            "Shipping time": item_shipping_times,
            "REviews": item_reviews,
            "Page": item_pages
        }

        df = pd.DataFrame(data)

        with open("Amazon Ae.csv", 'w') as file:
            file.write(df.to_csv())

        exclude_first_column("Amazon Ae.csv")

        from subprocess import Popen
        Popen('Amazon Ae.csv', shell=True)

    def scrap_url(url):
        from selenium import webdriver
        from bs4 import BeautifulSoup
        from time import sleep

        driver = webdriver.Chrome()
        driver.get(url)

        sleep(10)

        page_source = driver.page_source
        bisque = BeautifulSoup(page_source, 'html.parser')

        items = bisque.findAll(class_=['sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin '
                                       'sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20'])

        if len(items) == 0:
            return False
        else:
            for item in items:
                item_names.append(item.find(class_='a-size-base-plus a-color-base a-text-normal').text.strip())

                item_ratings.append(item.find(class_='a-icon-alt').text.strip()) \
                    if item.find(class_='a-icon-alt') else item_ratings.append("None")

                item_reviews.append(item.find(class_='a-size-base s-underline-text').text.strip()) \
                    if item.find(class_='a-size-base s-underline-text') else item_reviews.append("None")

                item_prices.append(item.find(class_='a-price-symbol').text.strip() + ' ' + item.find(
                    class_='a-price-whole').text.strip()
                                   + item.find(class_='a-price-fraction').text.strip())

                item_shipping_times.append(item.find(class_='a-color-base a-text-bold').text.strip().title()) \
                    if item.find(class_='a-color-base a-text-bold') else item_shipping_times.append("None")

                item_pages.append('https://www.amazon.ae' + item.find(
                    class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']
                                  )

            return True

    if __name__ == '__main__':
        try:
            item_names, item_ratings, item_reviews, item_prices, item_shipping_times, item_pages = [], [], [], [], [], []
            i = 1
            while True:
                if not scrap_url(f'https://www.amazon.ae/s?k=cricut&rh=p_n_prime_domestic%3A20642115031%2Cp_n_'
                                 f'fulfilled_by_amazon%3A16258112031&dc&page={i}&qid=1691734456&rnid=16258111031&ref=sr_pg_{i}'):
                    break
                i += 1
                print(len(item_names), len(item_ratings), len(item_reviews), len(item_prices), len(item_shipping_times),
                      len(item_pages))
            save_items_as_csv()
        except Exception as e:
            print(item_names[len(item_names) - 1])
            print(e)
