from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_echo_box(driver):

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
