import time

from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# There are 2 types of waits : Implicit and Explict waits, we should not use sleeps in our selenium code
# IMPLICIT WAIT : if an element doesn't appear in X seconds then the TC will fail
# Also, if element shows up with in 5 seconds then it will proceed with next added steps
driver.implicitly_wait(6)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2) # here is an exception case where sleep was needed hence added

# Here we are adding the logic to add n number of items that came post search result into the cart
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()  # This is called Chaining of parent element with child element

# Now click on "Add Cart" Icon for already added items in the cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# Now click on "PROCEED TO CHECKOUT" CTA from Add Cart popup
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# User navigates to Cart summary screen. Enter the valid coupon code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Click on Apply coupon, wait until code applies and then validate the "Coupon applied" message
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# validate the "Coupon applied" message
print(driver.find_element(By.CLASS_NAME, "promoInfo").text) # O/P in console : Code applied ..!