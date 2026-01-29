from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# --- Your config ---
url = "http://10.100.20.1:8090/httpclient.html" #put hare Url
username = "UserName" #put UserName hare
password = "Password" #put Password hare


while True:
    # Create Chrome driver
    driver = webdriver.Chrome("chromedriver.exe")

    try:
        # Open the login page
        driver.get(url)

        # Enter username and password
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)

        # Wait for login button to be clickable and click it
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loginbutton"))
        )
        login_btn.click()

        # Optional: wait to ensure login completes
        time.sleep(5)

    finally:
        # Close the browser
        driver.quit()

    # Wait 2 minutes before the next login
    time.sleep(120)



