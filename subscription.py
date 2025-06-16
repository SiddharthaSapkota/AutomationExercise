from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
website = "https://www.automationexercise.com"
driver.get(website)

subscribe_id = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "susbscribe_email"))
)
driver.execute_script("arguments[0].scrollIntoView();", subscribe_id)
subscribe_id.send_keys("sid@gmail.com")


subscribe_btn = driver.find_element(By.ID, "subscribe")
subscribe_btn.click()

input("Press it to end...")