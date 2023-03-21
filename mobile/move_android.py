from os import path
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
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
    wait = WebDriverWait(driver, 5)

    wait.until(EC.presence_of_element_located(
        (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="List Demo"]'))).click()
    wait.until(EC.presence_of_element_located(
        (MobileBy.ACCESSIBILITY_ID, 'Altocumulus')))

    actions = ActionBuilder(driver)
    finger = actions.add_pointer_input(POINTER_TOUCH, 'finger')
    finger.create_pointer_move(duration=0, x=100, y=500)
    # finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_down(button=MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=0, y=-500, origin='pointer')
    # finger.create_pointer_up(MouseButton.LEFT)
    finger.create_pointer_up(button=MouseButton.LEFT)
    actions.perform()

    driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Stratocumulus')
finally:
    time.sleep(2.5)
    driver.quit()
