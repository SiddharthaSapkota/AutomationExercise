from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

# Wait for a unique element on the homepage to be visible
driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

#trying to input already existing email
driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys("Testing Bro")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("sid@example.com")

# Click Signup button
driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']").click()

input("Press Enter to exit and close the browser...")