from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

# NOTE : For more details on Chrome Options
# please visit this website: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

# Start browser in maximize mode
chrome_options.add_argument("--start-maximized")

# Running Browser in Headless mode
chrome_options.add_argument("headless")

# To handle SSL certificate error
chrome_options.add_argument("--ignore-certificate-errors")

# To open browser in a specific resolution
chrome_options.add_argument("--window-size=1920x1080")


service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)  # O/P : ProtoCommerce
