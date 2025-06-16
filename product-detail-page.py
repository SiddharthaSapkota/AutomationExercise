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

view_product_btn_element = driver.find_element(By.CSS_SELECTOR, "a[href='/product_details/1']")
driver.execute_script("window.scrollBy(0,500)", view_product_btn_element)
view_product_btn_element.click()

input("Enter...")