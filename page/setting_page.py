from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    about_button = By.XPATH, "//*[@text = '关于百年奥莱']"
    clear_cache_button = By.XPATH, "//*[@text = '清理缓存']"
    address_list_button = By.XPATH, "//*[@text = '地址管理']"

    def click_about_button(self):
        self.find_element_with_scroll(self.about_button).click()

    def click_clear_cache_button(self):
        self.find_element_with_scroll(self.clear_cache_button).click()

    def click_address_list_button(self):
        self.find_element_with_scroll(self.address_list_button).click()
