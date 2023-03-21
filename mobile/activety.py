from os import path
from appium import webdriver
import time

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
    app_act1 = '.graphics.TouchPaint'  # io.appium.android.apis.graphics.TouchPaint
    app_act2 = ".text.Marquee"

    driver.install_app(app)
    driver.start_activity(app_id, app_act1)
    time.sleep(2)
    driver.start_activity(app_id, app_act2)
    time.sleep(2)
finally:
    driver.quit()
