
from seleniumpagefactory import PageFactory

from src.pages.base_page import BasePage
from src.utils.locators import Locators


class MainSaucePage(BasePage, PageFactory):


    locators = {
        "link_shopping_cart": (Locators.CLASS_NAME, "shopping_cart_link")
    }

    def __init__(self, driver):
        self.driver = driver

    def go_to_shopping_cart(self):
        self.link_shopping_cart.click()
