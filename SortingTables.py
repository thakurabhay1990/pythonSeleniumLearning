import time

from selenium import webdriver

from selenium.webdriver import ActionChains

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggie=[]

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Click column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# Collect all the vegetable's name into a list
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggie.append(ele.text)

originalBrowserSortedList = browserSortedVeggie.copy() # we can also use .slice() method too

# Sort the list, get the new sorted list and both the lists should be equal check it by adding assertion
browserSortedVeggie.sort()

assert browserSortedVeggie == originalBrowserSortedList