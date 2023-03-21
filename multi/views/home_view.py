from appium.webdriver.common.mobileby import MobileBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from views.base_view import BaseView
from views.echo_view import EchoView


class HomeView(BaseView):
    ECHO_ITEM = (MobileBy.XPATH,
                 '//android.view.ViewGroup[@content-desc="Echo Box"]')

    def nav_to_EchoBox(self):
        # wait = WebDriverWait(self.driver, 6)
        # wait.until(EC.presence_of_element_located(self.ECHO_ITEM)).click()
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView.instance(self.driver)
