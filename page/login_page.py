from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username = By.XPATH, "//*[@text = '请输入手机/昵称']"
    password = By.ID, 'com.yunmall.lc:id/logon_password_textview'
    login_button = By.XPATH, "//*[@text = '登录']"

    def input_username(self, text):
        self.input(self.username, text)

    def input_password(self, text):
        self.input(self.password, text)

    def click_login_button(self):
        self.click(self.login_button)
