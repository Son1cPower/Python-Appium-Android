from os import path
import pytest
from appium import webdriver

CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://127.0.0.1:4723/wd/hub'


@pytest.fixture
def driver():

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

    yield driver
    driver.quit()
