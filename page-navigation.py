from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
website ="https://www.automationexercise.com"
driver.get(website)

wait = WebDriverWait(driver, 10)
# Products Page
product_page = driver.find_element(By.CSS_SELECTOR, "a[href='/products']")
product_page.click()

# Cart Page
view_cart = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
view_cart.click()

# Test case Page
test_case = driver.find_element(By.CSS_SELECTOR, "a[href='/test_cases']")
test_case.click()

# API Testing Page
api_test = driver.find_element(By.CSS_SELECTOR, "a[href='/api_list']")
api_test.click()

# Video Tutorial Page
video_tut = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.youtube.com/c/AutomationExercise']")
video_tut.click()
driver.get(website)
# wait = WebDriverWait(driver, 10)

# Contact Us Page
contact_us = driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']")
contact_us.click()

#Home page
home = driver.find_element(By.CSS_SELECTOR, "a[href='/']")
home.click()


# input("testing here..")