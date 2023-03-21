from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from views.base_view import BaseView


class EchoView(BaseView):
    MESSAGE_INPUT = (MobileBy.XPATH,
                     '//android.widget.EditText[@content-desc="messageInput"]')
    SAVE_BUTTON = (
        MobileBy.XPATH, '//android.view.ViewGroup[@content-desc="messageSaveBtn"]')
    MASSAGE_LABEL_TEXT = (
        MobileBy.XPATH, '//android.widget.TextView[@content-desc]')

    def save_message(self, message):
        # wait = WebDriverWait(self.driver, 6)
        # wait.until(EC.presence_of_element_located(
        #     self.MESSAGE_INPUT)).send_keys(message)
        # wait.until(EC.presence_of_element_located(self.SAVE_BUTTON)).click()
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        self.wait_for(self.SAVE_BUTTON).click()

    def read_message(self):
        # wait = WebDriverWait(self.driver, 6)
        # return wait.until(EC.presence_of_element_located(
        #     self.MASSAGE_LABEL_TEXT)).text
        try:
            return self.wait_for(self.MASSAGE_LABEL_TEXT).text
        except Exception:
            return None

    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView(self.driver)
