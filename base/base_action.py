from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        """

        :param driver:
        """
        self.driver = driver

    def find_element(self, feature, timeout=5, poll=1):
        """

        :param feature:
        :param timeout:
        :param poll:
        :return:
        """
        a, b = feature
        # element = self.driver.find_element(a,b)
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(a, b))
        return element

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def clear(self, feature):
        self.find_element(feature).clear()

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)
