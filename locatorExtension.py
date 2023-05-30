from selenium import webdriver


# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/client/")

# Locator elements via Link Text
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gamil.com")

# driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")

driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")

# driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


# Important NOTE :-
# In Xpath : //form/div[2]/input
# In CSS : form div:nth-child(2) input