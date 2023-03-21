from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'

driver = webdriver.Firefox(
    executable_path='C:/myDrivers/geckodriver.exe', options=firefox_options)

try:

    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/')

    # driver.find_element(By.LINK_TEXT, 'Form Authentication')     ---without wait
    wait.until(EC.presence_of_all_elements_located(
        (By.LINK_TEXT, 'Form Authentication')))

    wait.until(EC.url_to_be('https://the-internet.herokuapp.com/'))


finally:
    driver.quit()
