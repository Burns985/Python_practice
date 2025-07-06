from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import csv
import os


def count_files_in_folder(folder_path):
    # Get the list of all files in the folder
    files = os.listdir(folder_path)

    # Filter out directories from the list
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

    # Get the number of files
    num_files = len(files)

    return num_files


def exclude_first_column(input_file):
    with open(input_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        data = [row[1:] for row in reader]

    with open(input_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)


def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)

    # Extract the file extension from the URL
    file_extension = os.path.splitext(url)[1]
    print(os.path.splitext(url)[1])
    # Save the image to the specified path
    with open(save_path + file_extension, "wb") as f:
        f.write(response.content)


def create_folder_on_desktop(folder_name):
    desktop_path = "C:\\Users\muhai\OneDrive\Desktop\galax-mall"
    folder_path = os.path.join(desktop_path, folder_name)
    try:
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully on the desktop.")
        return folder_path
    except FileExistsError:
        os.mkdir(folder_path + " 1")
        print(f"Folder '{folder_name}' already exists on the desktop.")
        return folder_path + " 1"
    except Exception as e:
        print(f"Error occurred: {e}")


def get_items(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find(class_='products row row-small large-columns-4 medium-columns-3 small-columns-2')

        for item in table:
            tag = item.find('a')
            product_links.append(tag['href'])
            product_titles.append(str(item.find(class_='name product-title').get_text(strip=True)).replace('|', ''))
        return True

    except HTTPError:
        return False


def save_images():
    for link in product_links:
        response = requests.get(link)
        response.raise_for_status()
        bisque = BeautifulSoup(response.content, 'html.parser')
        tags = bisque.findAll(class_="attachment-woocommerce_thumbnail lazyload")

        title = product_titles[product_links.index(link)]
        folder = create_folder_on_desktop(title)
        if folder:
            folder = folder + '\\' + title
            print(folder)
            for i in range(len(tags)):
                download_image(tags[i]['data-src'], f"{folder}{i}")


if __name__ == "__main__":
    i = 1
    product_links = []
    product_titles = []
    while True:
        print(i)
        flag = get_items(f'https://galax-mall.com/shop/page/{i}')
        if not flag:
            print("All Done!")
            break
        i += 1

    save_images()
