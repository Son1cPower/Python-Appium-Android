from os import path
import pytest
from appium import webdriver
from views.home_view import HomeView

CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, 'TheApp.apk')
IOS_APP = path.join(CUR_DIR, 'TheApp.apk.zip')
APPIUM = 'http://127.0.0.1:4723/wd/hub'

ANDROID_CAPS = {
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Pixel 6',
    'automationName': 'UIAutomator2',
    'app': ANDROID_APP,
}

IOS_CAPS = {
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Nexus 5X',
    'automationName': 'UIAutomator2',
    'app': ANDROID_APP,
}


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')


@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def driver(platform):
    caps = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    driver = webdriver.Remote(
        command_executor=APPIUM, desired_capabilities=caps
    )
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
