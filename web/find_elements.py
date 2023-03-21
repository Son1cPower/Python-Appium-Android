from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

driver = webdriver.Firefox(
    executable_path='C:/myDrivers/geckodriver.exe', options=firefox_options)

try:
    driver.get('https://the-internet.herokuapp.com/')

    driver.find_element(By.LINK_TEXT, 'Form Authentication')

    els = driver.find_elements(By.TAG_NAME, 'a')
    print(f'There were {len(els)} anchor elements')

    els = driver.find_elements(By.TAG_NAME, 'foo')
    print(f'There were {len(els)} FOO elements')

finally:
    driver.quit()


# document.querySelector(button[type=submit])
# document.querySelector('#password')
