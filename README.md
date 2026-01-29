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
