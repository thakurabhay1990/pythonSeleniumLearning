# Handling Java popup's through Selenium
import time

from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Kreatos Abhay"
service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# Now a popup will appear and by default Selenium webdriver will not have knowledge about this popup/ Alert
# Hence, we have to switch from driver to alert mode
alert = driver.switch_to.alert # storing alert in a variable
alertText = alert.text # storing text from alert in a variable
print(alertText)
assert name in alertText
alert.accept() # this means to accept the alert
# alert.dismiss() # this means to cancel the alert


driver.close()