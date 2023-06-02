import time

from selenium import webdriver

from selenium.webdriver import ActionChains
# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(6)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Action on Mouse Hover CTA
action = ActionChains(driver)
# action.double_click(driver.find_element(By.))
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()  # this is used for right click
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
