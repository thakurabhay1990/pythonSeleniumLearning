
from selenium import webdriver


# Chrome driver cannot be invoked directly.
# We have to call chrome (proxy) driver which is an intermediate file.

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# -- This is for Firefox Browser --
# from selenium.webdriver.firefox.service import Service
# service_obj = Service("/Users/abhaythakur/Downloads/drivers/geckodriver")
# driver = webdriver.Firefox(service=service_obj)

# -- This is for Edge Browser --
# from selenium.webdriver.edge.service import Service
# service_obj = Service("/Users/abhaythakur/Downloads/drivers/msedgedriver")
# driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/practice-project")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()