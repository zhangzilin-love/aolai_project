from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegisterPage(BaseAction):
    login_button = By.XPATH, "//*[@text = '已有账号，去登录']"

    # 点击已有账号，去登陆
    def click_login_button(self):
        self.click(self.login_button)
