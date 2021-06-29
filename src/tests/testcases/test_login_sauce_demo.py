import unittest

import allure

from src.pages.sauce_login_page import LoginSaucePage
from src.utils.datapool_handler import DataPoolHandler

@allure.feature("Shoping")
class LoginTestCase(unittest.TestCase):

    __datapool = None

    def setUp(self):
        self.__datapool = DataPoolHandler("sauce demo").load_datapool_single_row()

    def tearDown(self):
        if self.sauce_login_po is not None:
            self.sauce_login_po.cleanUp()

    @allure.story("Login Sauce")
    def test_login(self):
        self.sauce_login_po = LoginSaucePage()
        main_page = self.sauce_login_po.login(self.__datapool.user, self.__datapool.password)
        assert main_page is not None, "Login Test Failed"

