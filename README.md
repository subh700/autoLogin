# Required installations
You need:
​

Python 3

Selenium Python package

Google Chrome browser

ChromeDriver that matches your Chrome version

# Install Python 3
Download from the official Python site and install.

During install on Windows, check “Add Python to PATH”.
​

# Check it:
python --version
(or python3 --version on Linux/macOS).
​

# Install Selenium
Open Command Prompt (Windows) or terminal (Linux/macOS) and run:
​
### python -m pip install selenium
If your system uses python3, then:

### python3 -m pip install selenium
You can verify Selenium is installed by importing it in Python or checking the version with:


## Better Practices

### Use a Virtual Environment
It's recommended to use a Python virtual environment to keep dependencies isolated.

### Handle Exceptions
Always wrap Selenium operations in try-except blocks to handle potential errors gracefully.

### Wait for Elements
Use WebDriverWait instead of time.sleep() for more reliable element detection.

### Keep ChromeDriver Updated
Regularly update your ChromeDriver to match your Chrome browser version to avoid compatibility issues.

### Avoid Hardcoding Credentials
Never hardcode login credentials in your scripts. Use environment variables or configuration files instead.

### Clean Up Resources
Always close the browser after you're done to prevent memory leaks and ensure proper cleanup.


## Usage - auto.py

### Quick Start

1. **Update Configuration Variables**
   - Edit the `auto.py` file and update these variables with your values:
     ```python
     url = "http://your-login-url.com"  # Your login page URL
     username = "your_username"          # Your login username
     password = "your_password"          # Your login password
     ```

2. **Configure Element IDs (if needed)**
   - Update these if your login form uses different element IDs:
     ```python
     USERNAME_FIELD_ID = "username"      # ID of username input field
     PASSWORD_FIELD_ID = "password"      # ID of password input field
     LOGIN_BUTTON_ID = "loginbutton"     # ID of login button
     ```

3. **Run the Script**
   ```bash
   python auto.py
   ```

### Features

✅ **Automated Login** - Automatically logs in with provided credentials
✅ **Error Handling** - Comprehensive try-except blocks for error management
✅ **Logging** - Detailed logging to both console and `autoLogin.log` file
✅ **Retry Logic** - Continuously retries login every 2 minutes
✅ **Resource Management** - Properly closes browser to prevent memory leaks
✅ **Explicit Waits** - Uses WebDriverWait for reliable element detection
✅ **Configurable Timeouts** - Adjust wait times and retry intervals as needed

### Configuration Options

You can customize timing parameters in the script:

- `WAIT_TIMEOUT` (default: 10 seconds) - Maximum time to wait for elements
- `LOGIN_WAIT` (default: 5 seconds) - Time to wait for login completion
- `RETRY_INTERVAL` (default: 120 seconds) - Time between login attempts

### Logging

The script generates logs in two places:

1. **Console Output** - Real-time status messages
2. **autoLogin.log** - Persistent log file in the script directory

Log entries include:
- Script initialization
- Login attempts and results
- Element interactions
- Errors and exceptions
- Browser cleanup operations

### Security Recommendations

⚠️ **Security Best Practices:**
- Never commit credentials to version control
- Use environment variables or a separate config file for credentials
- Consider using `.env` files with `python-dotenv` for production
- Regularly update ChromeDriver to match your Chrome browser version
- Test the script in a development environment first

### Troubleshooting

**Issue: "chromedriver.exe not found"**
- Ensure `chromedriver.exe` is in the same directory as `auto.py`
- Or specify the full path to ChromeDriver in the script

**Issue: "Element not found"**
- Verify element IDs match your login form
- Check if the website has changed its HTML structure
- Inspect the page to find correct element IDs

**Issue: "Timeout waiting for element"**
- Increase `WAIT_TIMEOUT` value if the page loads slowly
- Check your internet connection
- Verify the URL is accessible

### Example Log Output

```
2026-01-29 17:30:00,123 - INFO - ============================================================
2026-01-29 17:30:00,123 - INFO - AutoLogin Script Started
2026-01-29 17:30:00,123 - INFO - Target URL: http://10.100.20.1:8090/httpclient.html
2026-01-29 17:30:00,123 - INFO - ============================================================
2026-01-29 17:30:00,200 - INFO - --- Login Attempt #1 ---
2026-01-29 17:30:00,250 - INFO - Initializing Chrome WebDriver...
2026-01-29 17:30:02,400 - INFO - Chrome WebDriver initialized successfully
2026-01-29 17:30:02,450 - INFO - Navigating to http://10.100.20.1:8090/httpclient.html
2026-01-29 17:30:03,600 - INFO - Login page loaded successfully
2026-01-29 17:30:03,700 - INFO - Entering username...
2026-01-29 17:30:03,800 - INFO - Username entered successfully
2026-01-29 17:30:03,900 - INFO - Entering password...
2026-01-29 17:30:04,000 - INFO - Password entered successfully
2026-01-29 17:30:04,050 - INFO - Waiting up to 10 seconds for login button to be clickable...
2026-01-29 17:30:04,150 - INFO - Login button is clickable. Clicking...
2026-01-29 17:30:04,200 - INFO - Login button clicked successfully
2026-01-29 17:30:04,250 - INFO - Waiting 5 seconds for login to complete...
2026-01-29 17:30:09,300 - INFO - Login completed successfully
2026-01-29 17:30:09,400 - INFO - Successfully logged in. Next attempt in 120 seconds...
2026-01-29 17:30:09,500 - INFO - Closing browser...
2026-01-29 17:30:09,600 - INFO - Browser closed successfully
2026-01-29 17:30:09,650 - INFO - Waiting 120 seconds before next attempt...
```
