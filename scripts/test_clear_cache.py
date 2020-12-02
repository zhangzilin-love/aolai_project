# from base.base_driver import init_driver
# from page.page import Page
# from time import sleep
#
#
# class TestClearCache:
#     def setup(self):
#         self.driver = init_driver(no_reset=False)
#         self.page = Page(self.driver)
#         self.settingpage = self.page.create_SettingPage()
#         self.homepage = self.page.create_HomePage()
#         self.mepage = self.page.create_MePage()
#
#     def teardown(self):
#         sleep(1)
#         self.driver.quit()
#
#     def test_clearCache(self):
#         self.homepage.click_close_button()
#         self.homepage.login_if_not(self.page)
#         self.mepage.click_setting_button()
#         self.settingpage.click_clear_cache_button()
#         self.settingpage.is_toast_exist("清理")