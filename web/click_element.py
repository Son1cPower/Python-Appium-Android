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
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')))

    form_auth_link.click()

    user_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')))
    user_name.send_keys('tomsmith')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout'))).click()
    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')))

    assert 'logged out' in flash.text
finally:
    driver.quit()
