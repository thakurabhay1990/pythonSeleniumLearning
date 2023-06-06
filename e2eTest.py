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

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("ind")

# Explicit Wait Implementation
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
successMessage = driver.find_element(By.CLASS_NAME, "alert-success").text
print(successMessage)

assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage

driver.close()