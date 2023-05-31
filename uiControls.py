from selenium import webdriver

# -- This is for Chrome Browser --
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("/Users/abhaythakur/Downloads/drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Different ways to click option 2 in the above site:
# # Way 1: by using id
# driver.find_element(By.ID, "checkBoxOption2").click()
#
# # Way 2: by using Xpath
# driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]").click()

# Way 3 : by using find_elements, iterate it with for loop and select the option 2 how we did it in findElementTest.py
# Below will return 3 checkboxes in the form of list and for that we will store that in "checkboxes" variable.
checkboxes = driver.find_elements(By.XPATH, '//input[@type="checkbox"]')
print(len(checkboxes)) # O/P : 3

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() # This assertion will return boolean value(True/ False)
        break

driver.close()
