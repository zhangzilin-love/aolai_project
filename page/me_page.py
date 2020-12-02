from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    nick_name_text_view = By.ID, 'com.yunmall.lc:id/tv_user_nikename'
    setting_button = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'

    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text

    def click_setting_button(self):
        self.find_element(self.setting_button).click()
