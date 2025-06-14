'''Here i am asked to login with already created account.
But i wanted to explore more and tried registering , logging out
and then logging in with the created account and then deleting it.'''

import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

# Wait for a unique element on the homepage to be visible
driver.find_element(By.CSS_SELECTOR, "a[href='/login']").click()


# Fill in name and email
unique_name = ''.join(random.choices(string.ascii_lowercase, k=8))
driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-name']").send_keys(unique_name)
unique_email = f"testuser_{int(time.time())}@example.com"
driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys(unique_email)
# driver.find_element(By.CSS_SELECTOR, "input[data-qa='signup-email']").send_keys("honasdoess2104@example.com")   'If only you want to send static email'.

# Click Signup button
sign_up_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='signup-button']")
sign_up_btn.click()

# Click Gender via ID
driver.find_element(By.ID, "id_gender1").click()

# Input the other fields

'''name = driver.find_element(By.ID ,"name")
name.send_keys("Testing")'''

pwd = driver.find_element(By.ID, 'password')
pwd.send_keys("Password")

days = driver.find_element(By.ID, 'days')
days.send_keys("5")

months = Select(driver.find_element(By.ID, 'months'))   #Selecting via value
months.select_by_value("5")

years = driver.find_element(By.ID, 'years')
years.send_keys("2000")

# Tick Box Selection

driver.find_element(By.ID , "newsletter").click()
driver.find_element(By.ID , "optin").click()

# Address Information

first_name = driver.find_element(By.ID , "first_name")
first_name.send_keys(unique_name)

last_name = driver.find_element(By.ID , "last_name")
last_name.send_keys("Tester")

driver.find_element(By.ID , "company").send_keys("Bidhee Pvt.Ltd")
driver.find_element(By.ID, "address1").send_keys("Kathmandu")
driver.find_element(By.ID, "address2").send_keys("Bhaktapur")

country = Select(driver.find_element(By.ID, "country") )
country.select_by_value("Canada")

driver.find_element(By.ID, "state").send_keys("Testing State")
driver.find_element(By.ID, "city").send_keys("TestingCity")
driver.find_element(By.ID, "zipcode").send_keys("012012")
driver.find_element(By.ID, "mobile_number").send_keys("9845000000")

# Create Button
create_btn = driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']")
create_btn.click()

driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

# Logout account
driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()

# Login Account
email = driver.find_element(By.CSS_SELECTOR , "[data-qa = 'login-email']")
email.send_keys(unique_email)
login_pwd = driver.find_element(By.CSS_SELECTOR, "[data-qa = 'login-password']")
login_pwd.send_keys("Password")

login = driver.find_element(By.CSS_SELECTOR , "button[data-qa = 'login-button']")
login.click()


# Delete account
driver.find_element(By.CSS_SELECTOR, "a[href='/delete_account']").click()
driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

# This is to let the screen open for my own purpose.
input("Enter any thing to close..")


