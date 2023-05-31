import time

from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

# NOTE: There is a difference between find_element and find_elements. find_element will identify the element for
# singular match and find_elements will identify all (plural) the matching elements
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

# Now we are iterating for loop to select India option from a list of options. The below condition will
# select only the India option.
for country in countries:
    if country.text == "India":
        country.click()
        break

# Now lets put assertion on the above condition
    # print(driver.find_element(By.ID, "autosuggest").text()) --> Here with .text() we will not be able to
    # retrieve the value in the text box as it was dynamically generated. Hence we will user .attribute("value")
    # example : - print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"

# FYI : Suppose we value does not matches with assertion then the O/P will be : AssertionError
# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "india"

driver.close()