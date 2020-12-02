# # coding=utf-8
# import pytest
#
# from base.base_analyze import analyze_file
# from base.base_driver import init_driver
# from page.page import Page
# from time import sleep
#
#
# class TestLogin:
#     # 前置方法
#     def setup(self):
#         self.driver = init_driver(no_reset=False)
#         self.page = Page(self.driver)
#         self.loginpage = self.page.create_LoginPage()
#         self.homepage = self.page.create_HomePage()
#         self.registerpage = self.page.create_RegisterPage()
#         self.mepage = self.page.create_MePage()
#
#     # 后置方法
#     def teardown(self):
#         sleep(1)
#         self.driver.quit()
#
#     @pytest.mark.parametrize("args", analyze_file("test_login.yaml",'test_login'))
#     def test_login01(self, args):
#         self.homepage.click_close_button()
#         self.homepage.click_my_button()
#         self.registerpage.click_login_button()
#         self.loginpage.input_username(args["username"])
#         self.loginpage.input_password(args["password"])
#         self.loginpage.click_login_button()
#         if args["toast"] is None:
#             assert self.mepage.get_nick_name_text() == args["username"]
#         else:
#             assert self.loginpage.is_toast_exist(args["toast"])
