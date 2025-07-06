from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


# Test Case 1: Open Amazon Home Page
def test_open_amazon_home():
    driver.get("https://www.amazon.com")
    assert "Amazon" in driver.title, "Amazon home page did not load successfully"


# Test Case 2: Search for a Product
def test_search_product():
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot .s-result-item")))
    assert len(results) > 0, "Search results are not displayed"


# Test Case 3: Open a Product Detail Page
def test_open_product_detail():
    product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot .s-result-item h2 a")))
    product.click()
    product_title = wait.until(EC.presence_of_element_located((By.ID, "productTitle")))
    assert product_title.is_displayed(), "Product detail page did not load"


# Test Case 4: Add a Product to the Cart
def test_add_to_cart():
    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    cart_confirmation = wait.until(EC.presence_of_element_located((By.ID, "sw-gtc")))
    assert cart_confirmation.is_displayed(), "Product was not added to the cart"


# Test Case 5: Verify Cart Content
def test_verify_cart():
    cart_button = wait.until(EC.presence_of_element_located((By.ID, "nav-cart")))
    cart_button.click()
    cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.sc-list-item")))
    assert len(cart_items) > 0, "Cart is empty"


# Execute the test cases
try:
    test_open_amazon_home()
    print("Test 1: Open Amazon Home - Passed")

    test_search_product()
    print("Test 2: Search Product - Passed")

    test_open_product_detail()
    print("Test 3: Open Product Detail - Passed")

    test_add_to_cart()
    print("Test 4: Add to Cart - Passed")

    test_verify_cart()
    print("Test 5: Verify Cart - Passed")

finally:
    # Close the WebDriver
    driver.quit()
