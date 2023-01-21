import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

BASE_URL = "https://localhost:18429"

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')


driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(BASE_URL)


def addProductsToCart():
    # getting category links
    leds_link = driver.find_elements(By.CLASS_NAME, "dropdown-item")[1].get_attribute("href")
    lamps_link = driver.find_elements(By.CLASS_NAME, "dropdown-item")[2].get_attribute("href")

    product_links = []

    # getting 5 product links from category Leds
    driver.get(leds_link)
    for product_element in driver.find_elements(By.CLASS_NAME, "product-thumbnail")[:5]:
        product_links.append(product_element.get_attribute("href"))

    # getting 5 product links from category Lamps
    driver.get(lamps_link)
    for product_element in driver.find_elements(By.CLASS_NAME, "product-thumbnail")[:5]:
        product_links.append(product_element.get_attribute("href"))

    # adding each product from product_hrefs to shopping cart with quantity in range 1-5
    for link in product_links:
        driver.get(link)
        driver.find_element(By.ID, "quantity_wanted").send_keys(Keys.DELETE, str(random.randint(1, 5)))
        driver.find_element(By.CLASS_NAME, "add-to-cart").click()
        time.sleep(0.5)

def deleteFromCart():
    # starts from main page
    driver.get(BASE_URL)

    # going to the cart
    driver.find_element(By.ID, "_desktop_cart").find_element(By.CSS_SELECTOR, "a").click()

    time.sleep(2)
    # chooses product and deletes it
    driver.find_elements(By.CLASS_NAME, "remove-from-cart")[random.randint(0, 8)].click()
    time.sleep(2)

def register():
    # starts from shopping cart page

    driver.find_element(By.CLASS_NAME, "cart-summary").find_element(By.CLASS_NAME, "btn-primary").click()

    # fill personal information
    driver.find_element(By.ID, "field-id_gender-1").click()
    driver.find_element(By.ID, "field-firstname").send_keys("Jakub")
    driver.find_element(By.ID, "field-lastname").send_keys("Szymański")
    driver.find_element(By.ID, "field-email").send_keys("Corax01@wp.pl")
    driver.find_element(By.ID, "field-password").send_keys("password")
    driver.find_element(By.ID, "field-birthday").send_keys("2001-01-02")
    driver.find_element(By.NAME, "customer_privacy").click()
    driver.find_element(By.NAME, "psgdpr").click()

    time.sleep(5)

    driver.find_element(By.NAME, "continue").click()

    # fill address info
    driver.find_element(By.ID, "field-address1").send_keys("ul. Spokojna 23/13")
    driver.find_element(By.ID, "field-postcode").send_keys("84-240")
    driver.find_element(By.ID, "field-city").send_keys("Reda")

    time.sleep(5)

    driver.find_element(By.NAME, "confirm-addresses").click()

def chooseDeliveryAndPayment():
    # starts from delivery choose page

    # choose delivery option
    delivery_option = random.randint(11, 13) # 13 - InPost, 11 - DHL
    driver.find_element(By.ID, f"delivery_option_{delivery_option}").click()

    time.sleep(2)

    driver.find_element(By.NAME, "confirmDeliveryOption").click()

    # choose payment on delivery
    driver.find_element(By.ID, "payment-option-2").click()
    driver.find_element(By.NAME, "conditions_to_approve[terms-and-conditions]").click()

    time.sleep(2)

    # submit order
    driver.find_element(By.ID, "payment-confirmation").find_element(By.CSS_SELECTOR, "button").click()
    time.sleep(5)

def checkOrderStatus():
    # starting from main page
    driver.get(BASE_URL)

    driver.find_element(By.CLASS_NAME, "account").click()
    driver.find_element(By.ID, "history-link").click()
    order_status = driver.find_element(By.CLASS_NAME, "label-pill").text
    print(order_status)


addProductsToCart()

deleteFromCart()

register()

chooseDeliveryAndPayment()

checkOrderStatus()

time.sleep(2)
driver.quit()
