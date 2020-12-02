from base.base_action import BaseAction
from page.address_list_page import AddressListPage
from page.edit_address_page import EditAddressPage
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.register_page import RegisterPage
from page.setting_page import SettingPage
from page.update_page import UpdatePage


class Page(BaseAction):
    def create_HomePage(self):
        return HomePage(self.driver)

    def create_LoginPage(self):
        return LoginPage(self.driver)

    def create_RegisterPage(self):
        return RegisterPage(self.driver)

    def create_MePage(self):
        return MePage(self.driver)

    def create_SettingPage(self):
        return SettingPage(self.driver)

    def create_UpdatePage(self):
        return UpdatePage(self.driver)

    def create_AddressListPage(self):
        return AddressListPage(self.driver)

    def create_EditAddressPage(self):
        return EditAddressPage(self.driver)
