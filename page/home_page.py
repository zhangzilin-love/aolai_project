from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):
    my_button = By.ID, 'com.yunmall.lc:id/tab_me'
    close_button = By.ID, 'com.yunmall.lc:id/img_close'

    # 点击“我的”按钮
    def click_my_button(self):
        self.click(self.my_button)

    # 点击弹窗关闭按钮
    def click_close_button(self):
        self.click(self.close_button)

    # 如果没有登录就进行登录操作
    def login_if_not(self, page):
        self.click_my_button()
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        else:
            page.create_RegisterPage().click_login_button()
            page.create_LoginPage().input_username("itheima_test")
            page.create_LoginPage().input_password("itheima")
            page.create_LoginPage().click_login_button()