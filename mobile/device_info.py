from os import path
from appium import webdriver


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
    app = path.join(CUR_DIR, 'ApiDemos.apk')
    app_id = 'io.appium.android.apis'

    deviceInfo = driver.execute_script(
        "mobile: deviceInfo")    # выведет дивайс инфо
    driver.remove_app(app_id)
    driver.install_app(app)
    driver.activate_app(app_id)
    driver.terminate_app(app_id)
finally:
    driver.quit()
