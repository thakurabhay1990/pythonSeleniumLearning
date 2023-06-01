import time

from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

expectedList = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# There are 2 types of waits : Implicit and Explict waits, we should not use sleeps in our selenium code
# IMPLICIT WAIT : if an element doesn't appear in X seconds then the TC will fail
# Also, if element shows up with in 5 seconds then it will proceed with next added steps
driver.implicitly_wait(6)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)  # here is an exception case where sleep was needed hence added

# Here we are adding the logic to add n number of items that came post search result into the cart
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")  # list
count = len(results)
assert count > 0
for result in results:
    actualList.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()  # This is called Chaining of parent element with child element

assert expectedList == actualList

print("The expected list is same as actual list")

# Now click on "Add Cart" Icon for already added items in the cart
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# Now click on "PROCEED TO CHECKOUT" CTA from Add Cart popup
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)  # Iteration 1: 0 + 160 >> Iteration 2 : 160 + 180 >> Iteration 3 : 340 + 48
# Above, we have added int to price.text as the text will be coming in String format
# and to get it in int we have to use int

print(sum)

totalamount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == totalamount
print("The sum and the total amount are matching.")

# User navigates to Cart summary screen. Enter the valid coupon code
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Click on Apply coupon, wait until code applies and then validate the "Coupon applied" message
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# validate the "Coupon applied" message
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)  # O/P in console : Code applied ..!

discountedamount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)

assert totalamount > discountedamount