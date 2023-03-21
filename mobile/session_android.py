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
    wait = WebDriverWait(driver, 10)
    # print(driver.page_source)
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Login Screen')))
    driver.find_element(MobileBy.CLASS_NAME, 'android.widget.TextView')
    driver.find_element(
        MobileBy.XPATH, '//android.widget.TextView[@text="Webview Demo"]')
finally:
    driver.quit()
