import time

from selenium import webdriver

from selenium.webdriver import ActionChains

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

# Code to Handle iFrames
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate the iFrames")

# We need to switch back to default state outside iFrame to print below text
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)

