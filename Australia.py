import bs4
import requests


def australia_driver():
    from time import sleep
    from selenium import webdriver
    from selenium.common import TimeoutException
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Create a WebDriver instance (Chrome)
    driver = webdriver.Chrome()

    # Define the URL of the website to be accessed
    url = 'https://www.realestate.com.au/'
    driver.get(url)  # Open the URL in the browser

    # Set up a WebDriverWait instance with a timeout of 40 seconds
    wait = WebDriverWait(driver, 40)

    try:
        # Wait until the button with the specified aria-label attribute appears
        button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[@aria-label="Select suburb, postcode, or states to buy a property in"]'))
        )
        button.click()  # Click the found button
        print("Button has been clicked.")
    except TimeoutException:
        print("Timed out waiting for button to appear.")

    # Find the search bar element and enter "Sydney" in it
    search_bar = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            '//input[@class="styles__Input-sc-xqj8kc-0 cnVMzS Input"]')))
    search_bar.send_keys("Sydney")  # Input "Sydney" into the search bar
    sleep(2)  # Pause for 2 seconds

    # Wait for the suggestion box to be present
    suggestion_box = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//ul[@class="styles__Listbox-sc-12mofj4-1 hYBqgq Listbox"]')))
    sleep(3)  # Pause for 3 seconds

    # Click the first list item to select it using JavaScript
    driver.execute_script('arguments[0].querySelector("li").click();', suggestion_box)

    sleep(3)  # Pause for 3 seconds

    # Locate and click the search submit button
    element = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     '//button[@class="ButtonBase-sc-18zziu4-0 gnqHpN '
                                                     'SubmitSearchButton__StyledButton-sc-7ign35-0 iGwCPc"]')))
    element.click()
    sleep(5)  # Pause for 5 seconds

    # Get the URL of the current page
    current_url = driver.current_url
    print("Current URL:", current_url)

    sleep(2)  # Pause for 2 seconds

    # Close the WebDriver
    driver.quit()
    get_page_data(current_url)


def get_page_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    print(soup)
    # properties = soup.findAll('div', {'role': 'presentation'})
    # print(len(properties))


australia_driver()


import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.realestate.com.au/buy/list-1"
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     property_listings = soup.find_all("div", class_="listing-card")
#
#     for listing in property_listings:
#         property_title = listing.find("a", class_="listing-title-link").text.strip()
#         property_price = listing.find("span", class_="property-price").text.strip()
#         property_details = listing.find("div", class_="property-details")
#         property_address = property_details.find("span", class_="address").text.strip()
#         property_type = property_details.find("span", class_="property-type").text.strip()
#
#         print("Property:", property_title)
#         print("Price:", property_price)
#         print("Address:", property_address)
#         print("Property Type:", property_type)
#         print("=" * 30)
# else:
#     print("Failed to retrieve the webpage")