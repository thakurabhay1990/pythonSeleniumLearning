
from selenium import webdriver


# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Locating elements from : ID, XPath, CSS Selector, Classname, Name, Link Text
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Custom CSS Selector: input[type="submit"] for Submit CTA.
# #id value becomes a CSS selector
# .classname becomes a CSS selector
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Kreatos Test")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

# Custom Xpath : //input[@type="submit"] for Submit CTA
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

# Validating assertions
assert "Success" in message

# # Assertion Error: assert "Sucasdscess" in message
# assert "Sucasdscess" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello everyone")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

driver.close()


