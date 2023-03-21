from os import path
import pytest
from appium import webdriver
from views.home_view import HomeView


CUR_DIR = path.dirname(path.abspath(__file__))
ANDROID_APP = path.join(CUR_DIR, 'TheApp.apk')
IOS_APP = path.join(CUR_DIR, 'TheApp.apk.zip')
# APPIUM = 'http://127.0.0.1:4723/wd/hub'
APPIUMS = ['http://127.0.0.1:4723/wd/hub', 'http://127.0.0.1:4724/wd/hub']


ANDROID_CAPS = [{
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Pixel 6',
    'automationName': 'UIAutomator2',
    'app': ANDROID_APP,
}, {
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Nexus 5X',
    'automationName': 'UIAutomator2',
    'app': ANDROID_APP,
}]

IOS_CAPS = {
    'platformName': 'Android',
    # 'platformVersion': '',
    'deviceName': 'Android Emulator',
    # 'deviceName': 'Pixel 6',
    'automationName': 'UIAutomator2',
    'app': ANDROID_APP,
}


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')


@pytest.fixture
def worker_num(worker_id):
    if worker_id == 'master':
        worker_id == 'gw0'
    return int(worker_id[2:])


@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def caps(platform, worker_num):
    cap_set = IOS_CAPS if platform == 'ios' else ANDROID_CAPS
    if worker_num >= len(cap_set):
        raise Exception('Too many workers for the num of cap sets')
    return cap_set[worker_num]


@pytest.fixture
def server(worker_num):
    if worker_num >= len(APPIUMS):
        raise Exception("Too many workers for the num of Appium servers")
    return APPIUMS[worker_num]


@pytest.fixture
def driver(server, caps, platform):

    driver = webdriver.Remote(command_executor=server,
                              desired_capabilities=caps)
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView.instance(driver)
