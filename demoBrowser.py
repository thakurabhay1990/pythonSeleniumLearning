
from selenium import webdriver


# Chrome driver cannot be invoked directly.
# We have to call chrome (proxy) driver which is an intermediate file.

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
# Approach 1 (let the driver download from web automatically.) -- Getting error
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj) # The driver objects here holds the Chrome browser


# Approach 2 (using local Chrome Driver):
service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj) # The driver objects here holds the Chrome browser

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