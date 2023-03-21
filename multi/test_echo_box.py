# from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from views.home_view import HomeView
from views.echo_view import EchoView


def test_echo_box(home):

    # home = HomeView(driver)
    # echo = EchoView(driver)
    MASSAGE = 'Hello my friend, Jeka!!!'

    # wait = WebDriverWait(driver, 5)
    # wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]'))).click()
    echo = home.nav_to_EchoBox()

    # wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.widget.EditText[@content-desc="messageInput"]'))).send_keys('Hello my friend!')
    # wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="messageSaveBtn"]'))).click()
    echo.save_message(MASSAGE)

    # wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.widget.TextView[@content-desc="Hello my friend!"]'))).is_displayed()
    assert echo.read_message() == MASSAGE

    # driver.back()
    home = echo.nav_back()

    # wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="Echo Box"]'))).click()
    echo = home.nav_to_EchoBox()

    # save_test = wait.until(EC.presence_of_element_located(
    #     (MobileBy.XPATH, '//android.widget.TextView[@content-desc="Hello my friend!"]'))).text
    # assert save_test == 'Hello my friend!'
    assert echo.read_message() == MASSAGE


def test_saved_message_is_empty(home):
    echo = home.nav_to_EchoBox()
    assert echo.read_message() is None
