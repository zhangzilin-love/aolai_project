import random
from time import sleep

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"
    region_button = By.XPATH, "//*[@text = '请选择']"
    area_feature = By.ID, "com.yunmall.lc:id/area_title"
    save_button = By.XPATH, "//*[@text = '保存']"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    def input_info(self, text):
        self.input(self.info_edit_text, text)

    def input_post(self, text):
        self.input(self.post_code_edit_text, text)

    def click_default_address_button(self):
        self.click(self.default_address_button)

    def click_region_button(self):
        self.click(self.region_button)

    def choose_region(self):
        self.click_region_button()
        sleep(1)
        while True:
            if self.driver.current_activity == "com.yunmall.ymctoc.ui.activity.AddressAddActivity":
                break
            areas = self.find_elements(self.area_feature)
            areas_count = len(areas)
            areas_index = random.randint(0, areas_count - 1)
            areas[areas_index].click()
            sleep(2)

    def click_save_button(self):
        self.click(self.save_button)
