import allure
from allure_commons.types import Severity
from seleniumpagefactory import PageFactory

from src.pages.base_page import BasePage
from src.pages.sauce_main_page import MainSaucePage
from src.utils.locators import Locators
from src.utils.report_allure import ReportAllure


class LoginSaucePage(BasePage, PageFactory):
    __url = "https://www.saucedemo.com"

    locators = {
        "textbox_username": (Locators.ID, "user-name"),
        "textbox_password": (Locators.ID, "password"),
        "button_login": (Locators.ID, "login-button")
    }

    def __init__(self):
        super().__init__("opera")
        self.setUp(self.__url, 5)
        self.reporter = ReportAllure(self.driver)

    @allure.step("Login")
    def login(self, user: str, password: str):
        try:
            self.textbox_username.set_text(user)
            self.textbox_password.set_text(password)
            self.button_login.click_button()
            main_page = MainSaucePage(self.driver)
            if main_page.link_shopping_cart.visibility_of_element_located(timeout=5):
                return main_page
        except:
            self.reporter.attach_image_(Severity.CRITICAL)
