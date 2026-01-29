"""
Automated Web Login Script using Selenium WebDriver

This script automates the login process for a web application by:
1. Opening the login page in Chrome
2. Entering credentials (username and password)
3. Waiting for and clicking the login button
4. Retrying every 2 minutes

Author: subh700
Version: 2.0
Requirements: selenium, chromedriver.exe
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import time
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('autoLogin.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# --- Configuration Variables ---
# Update these values with your actual login credentials and URL
url = "http://10.100.20.1:8090/httpclient.html"  # Target login page URL
username = "UserName"  # Your username (keep secure)
password = "Password"  # Your password (keep secure)

# Timing configurations (in seconds)
WAIT_TIMEOUT = 10  # Maximum time to wait for elements
LOGIN_WAIT = 5  # Time to wait for login completion
RETRY_INTERVAL = 120  # Time between login attempts (2 minutes)

# Element IDs configuration
USERNAME_FIELD_ID = "username"
PASSWORD_FIELD_ID = "password"
LOGIN_BUTTON_ID = "loginbutton"

def initialize_driver():
    """
    Initialize and return a Chrome WebDriver instance.
    
    Returns:
        WebDriver: Chrome WebDriver object
        
    Raises:
        WebDriverException: If ChromeDriver cannot be initialized
    """
    try:
        logger.info("Initializing Chrome WebDriver...")
        driver = webdriver.Chrome("chromedriver.exe")
        logger.info("Chrome WebDriver initialized successfully")
        return driver
    except WebDriverException as e:
        logger.error(f"Failed to initialize WebDriver: {e}")
        raise

def perform_login(driver, url, username, password):
    """
    Perform the login operation.
    
    Args:
        driver (WebDriver): Selenium WebDriver instance
        url (str): URL of the login page
        username (str): Username for login
        password (str): Password for login
        
    Raises:
        TimeoutException: If elements are not found within timeout period
        NoSuchElementException: If elements are missing from the page
    """
    try:
        # Step 1: Navigate to login page
        logger.info(f"Navigating to {url}")
        driver.get(url)
        logger.info("Login page loaded successfully")
        
        # Step 2: Enter username
        logger.info("Entering username...")
        username_field = driver.find_element(By.ID, USERNAME_FIELD_ID)
        username_field.clear()
        username_field.send_keys(username)
        logger.info("Username entered successfully")
        
        # Step 3: Enter password
        logger.info("Entering password...")
        password_field = driver.find_element(By.ID, PASSWORD_FIELD_ID)
        password_field.clear()
        password_field.send_keys(password)
        logger.info("Password entered successfully")
        
        # Step 4: Wait for login button to be clickable and click it
        logger.info(f"Waiting up to {WAIT_TIMEOUT} seconds for login button to be clickable...")
        login_btn = WebDriverWait(driver, WAIT_TIMEOUT).until(
            EC.element_to_be_clickable((By.ID, LOGIN_BUTTON_ID))
        )
        logger.info("Login button is clickable. Clicking...")
        login_btn.click()
        logger.info("Login button clicked successfully")
        
        # Step 5: Wait for login to complete
        logger.info(f"Waiting {LOGIN_WAIT} seconds for login to complete...")
        time.sleep(LOGIN_WAIT)
        logger.info("Login completed successfully")
        
    except TimeoutException:
        logger.error(f"Timeout: Login button not found within {WAIT_TIMEOUT} seconds")
        raise
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred during login: {e}")
        raise

def main():
    """
    Main function that runs the infinite login loop with proper error handling.
    Attempts login every RETRY_INTERVAL seconds.
    """
    logger.info("="*60)
    logger.info("AutoLogin Script Started")
    logger.info(f"Target URL: {url}")
    logger.info("="*60)
    
    attempt = 0
    while True:
        attempt += 1
        driver = None
        
        try:
            logger.info(f"\n--- Login Attempt #{attempt} ---")
            
            # Initialize driver
            driver = initialize_driver()
            
            # Perform login
            perform_login(driver, url, username, password)
            
            logger.info(f"Successfully logged in. Next attempt in {RETRY_INTERVAL} seconds...\n")
            
        except WebDriverException as e:
            logger.error(f"WebDriver error on attempt #{attempt}: {e}")
        except TimeoutException:
            logger.error(f"Timeout error on attempt #{attempt}")
        except NoSuchElementException:
            logger.error(f"Element not found on attempt #{attempt}")
        except Exception as e:
            logger.error(f"Unexpected error on attempt #{attempt}: {e}")
        
        finally:
            # Ensure driver is properly closed
            if driver is not None:
                try:
                    logger.info("Closing browser...")
                    driver.quit()
                    logger.info("Browser closed successfully")
                except Exception as e:
                    logger.error(f"Error closing browser: {e}")
            
            # Wait before next attempt
            logger.info(f"Waiting {RETRY_INTERVAL} seconds before next attempt...")
            time.sleep(RETRY_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("\nScript interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Critical error: {e}")
        sys.exit(1)
