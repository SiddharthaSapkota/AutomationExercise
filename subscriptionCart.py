from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

view_cart = driver.find_element(By.CSS_SELECTOR, "a[href='/view_cart']")
view_cart.click()

subscribe_id = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "susbscribe_email"))
)

driver.execute_script("arguments[0].scrollIntoView();", subscribe_id)

unique_email = f"testuser_{int(time.time())}@example.com"
driver.find_element(By.ID, "susbscribe_email").send_keys(unique_email)
# subscribe_id.send_keys("sid@gmail.com")

subscribe_btn = driver.find_element(By.ID, "subscribe")
subscribe_btn.click()

input("Press it to end...")