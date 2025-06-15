from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

# Wait for a unique element on the homepage to be visible
driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()

driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-email']").send_keys("sid@example.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='login-password']").send_keys("Password123!@#")

driver.find_element(By.CSS_SELECTOR, "button[data-qa='login-button']").click()

#logging out
driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()


input("Enter any key to exit.....")