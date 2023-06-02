
from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

# Below method will grab all the open windows on the browser and put it in a list
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])  # Child window will open on the index 1
print(driver.find_element(By.TAG_NAME, "h3").text)  # Print the title appearing in child window. O/P : New Window
driver.close()

driver.switch_to.window(windowOpened[0]) # This is switch back to Parent Window and will open on index 0
parentWindowText = driver.find_element(By.TAG_NAME, "h3").text
print(parentWindowText) # O/P : Opening a new window

# Assertion : compare and validate the text value
assert parentWindowText == driver.find_element(By.TAG_NAME, "h3").text
