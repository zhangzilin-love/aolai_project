from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        """

        :param driver:
        """
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
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

    def find_elements(self, feature, timeout=10, poll=1.0):
        a, b = feature
        elements = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(a, b))
        return elements

    # 点击事件
    def click(self, feature):
        self.find_element(feature).click()

    # 输入事件
    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    # 清除事件
    def clear(self, feature):
        self.find_element(feature).clear()

    # 按键返回事件
    def press_back(self):
        self.driver.press_keycode(4)

    def get_text(self, feature):
        return self.find_element(feature).text

    # 按键回车事件
    def press_enter(self):
        self.driver.press_keycode(66)

    # toast是否存在，主要用作断言判断
    def is_toast_exist(self, message):
        feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        try:
            self.find_element(feature, 5, 0.5)
            return True
        except TimeoutException:
            return False

    # 如果想要的toast存在，返回该toast的text，否则报异常
    def get_toast_exist(self, message):
        feature = By.XPATH, "//*[contains(@text,'%s')]" % message
        if self.is_toast_exist(message):
            return self.find_element(feature).text
        else:
            raise Exception("toast未能模糊匹配进行搜索，请查看是否输入的文本相匹配或是否存在toast文本内容")

    # 滑动一次事件，存在默认值，从下往上滑动
    def scroll_one_time(self, direction):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]

        center_x = width / 2
        center_y = height / 2

        left_x = width / 4 * 1
        left_y = center_y
        right_x = width / 4 * 3
        right_y = center_y

        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_x
        bottom_y = height / 4 * 3

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确，up/down/left/right")

    # 边滑动变寻找想要的元素，如果滑动到底，未能发现该元素，直接异常，跳出循环
    def find_element_with_scroll(self, feature, direction="up"):
        """ 边滑边找某个元素的特征 :
        param
        feature:元素的特征 :
        param direction:
        方向 "up"：从下往上 "down"
        ：从上往下 "left"：从右往左
        "down"：从左往右
        :return: """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_one_time(direction)
                if self.driver.page_source == page_source:
                    break
                page_source = self.driver.page_source
