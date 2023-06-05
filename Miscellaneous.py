import time

from selenium import webdriver

from selenium.webdriver import ActionChains

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service

# Running Browser in Headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

# To handle SSL certificate error
chrome_options.add_argument("--ignore-certificate-errors")

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")

# For headless mode we have to send "options" argument
# once done then browser will not open and it will work headless
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Suppose we want to move to bottom of the screen. We will use Javascript functions which Selenium
# allow us to inject in the testing script through which we can perform Scroll on a particular page.
# NOTE : Selenium do not provide any inbuild function to scroll
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# Taking Screenshots
driver.get_screenshot_as_file("screen.png")
