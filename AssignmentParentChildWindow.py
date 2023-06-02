from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.find_element(By.CLASS_NAME, "blinkingText").click()

# Below method will grab all the open windows on the browser and put it in a list
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])  # Child window will open on the index 1
childWindowText = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
print(childWindowText) # O/P : Please email us at mentor@rahulshettyacademy.com with below template to receive response
grabEmailID = childWindowText.split("at")[1].strip().split(" ")[0]
print(grabEmailID) # O/P : mentor@rahulshettyacademy.com

driver.close()

driver.switch_to.window(windowOpened[0]) # This is switch back to Parent Window and will open on index 0
driver.find_element(By.ID, "username").send_keys(grabEmailID)
driver.find_element(By.ID, "password").send_keys(grabEmailID)
driver.find_element(By.ID, "signInBtn").click()

# Explicit Wait Implementation
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text) # O/P : Incorrect username/password