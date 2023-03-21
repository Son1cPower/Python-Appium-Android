from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

driver = webdriver.Firefox(
    executable_path='C:/myDrivers/geckodriver.exe', options=firefox_options)

try:
    driver.get('https://the-internet.herokuapp.com/')
finally:
    driver.quit()
