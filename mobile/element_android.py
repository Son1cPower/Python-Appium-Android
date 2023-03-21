import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://127.0.0.1:4723/wd/hub'


CAPS = {
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Pixel 6',
    'automationName': 'UIAutomator2',
    'app': APP,
}


driver = webdriver.Remote(
    command_executor=APPIUM, desired_capabilities=CAPS
)
try:
    wait = WebDriverWait(driver, 5)

    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.EditText[@content-desc="messageInput"]'))).send_keys('Hello my friend!')
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="messageSaveBtn"]'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@content-desc="Hello my friend!"]'))).is_displayed()

    driver.back()
    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]'))).click()
    save_test = wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.widget.TextView[@content-desc="Hello my friend!"]'))).text
    assert save_test == 'Hello my friend!'
finally:
    time.sleep(2.5)
    driver.quit()
