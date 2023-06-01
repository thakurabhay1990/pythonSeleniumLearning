import time

from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

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

# User navigates to Cart summary screen. Enter invalid coupon code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulacademy")

# Click on Apply coupon
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Explicit Wait Implementation
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

# wait until code invalidates and then validate the "Invalid code" message
print(driver.find_element(By.CLASS_NAME, "promoInfo").text) # O/P in console : Invalid code ..!

