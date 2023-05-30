
from selenium import webdriver

# Chrome driver cannot be invoked directly.
# We have to call chrome (proxy) driver which is an intermediate file.

from selenium.webdriver.chrome.service import Service

service_obj = Service("/Users/abhaythakur/Downloads/chromedriver/chromedriver")

driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com")
print(driver.title)
driver.close()