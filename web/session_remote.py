from selenium import webdriver
from selenium.webdriver import FirefoxOptions

options = FirefoxOptions()
options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'


caps = {
    'browserName': 'firefox'
}

driver = webdriver.Remote(
    command_executor='http://localhost:4444', desired_capabilities=caps, options=options)
driver.get('https://google.com')
driver.quit()
