from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

# Wait for a unique element on the homepage to be visible
driver.find_element(By.CSS_SELECTOR, "a[href='/contact_us']").click()

driver.find_element(By.CSS_SELECTOR, "input[data-qa='name']").send_keys("Testing Bro")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='email']").send_keys("automation@mail.com")
driver.find_element(By.CSS_SELECTOR, "input[data-qa='subject']").send_keys("For Testing Purpose")
driver.find_element(By.ID, "message").send_keys("I am just Testing Bro. HAHA")


# Find the file input element and send the file path and upload
file_input = driver.find_element(By.NAME, "upload_file")  
file_input.send_keys("S:\\AutomationExercise\\Siddhartha-Sapkota-cv.pdf")  

wait = WebDriverWait(driver, 10)
submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-qa='submit-button']")))
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

wait = WebDriverWait(driver, 10)
alert = driver.switch_to.alert
alert.accept()

driver.find_element(By.CSS_SELECTOR, "a[href='/']").click()

input("this is for tesing:  ")