from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    add_address_button = By.XPATH, "//*[@text = '新增地址']"
    default_receipt_name_text_view = By.ID, "com.yunmall.lc:id/receipt_name"

    def click_add_address_button(self):
        self.find_element_with_scroll(self.add_address_button).click()

    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)
