import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from time import sleep

from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.homepage = self.page.create_HomePage()
        self.mepage = self.page.create_MePage()
        self.settingpage = self.page.create_SettingPage()
        self.addresslistpage = self.page.create_AddressListPage()
        self.editaddresspage = self.page.create_EditAddressPage()

    def teardown(self):
        sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("test_address.yaml", "test_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]
        self.homepage.click_close_button()
        self.homepage.login_if_not(self.page)
        self.mepage.click_setting_button()
        self.settingpage.click_address_list_button()
        self.addresslistpage.click_add_address_button()
        self.editaddresspage.input_info(info)
        self.editaddresspage.input_name(name)
        self.editaddresspage.input_post(post_code)
        self.editaddresspage.input_phone(phone)
        self.editaddresspage.click_default_address_button()
        self.editaddresspage.choose_region()
        self.editaddresspage.click_save_button()
        if toast is None:
            assert self.addresslistpage.get_default_receipt_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.editaddresspage.is_toast_exist(toast)
