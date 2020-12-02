from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class UpdatePage(BaseAction):
    update_button = By.XPATH, "//*[@text = '版本更新']"

    def click_update_button(self):
        self.click(self.update_button)