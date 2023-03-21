from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
