from selenium import webdriver
from src.config.config import ConfigEnum
from src.utils.util import Util
from selenium.webdriver.opera.options import Options


class WebDriverHandler:
    driver = None

    def __init__(self, driver=None):
        self.driver = driver

    def set_driver_by_name(self, driver_name: str):
        if driver_name == ConfigEnum.OPERA_DRIVER:
            opera_options = Options()
            # chrome_options.add_argument("--disable-extensions")
            # chrome_options.add_argument("--disable-gpu")
            # chrome_options.add_argument("--no-sandbox") # linux only
            # opera_options.headless = True
            # chrome_options.headless = True # also work
            self.driver = webdriver.Opera(executable_path=Util().get_driver_exe_path(driver_name))
        elif driver_name == ConfigEnum.CHROME_DRIVER:
            self.driver = webdriver.Chrome(executable_path=Util().get_driver_exe_path(driver_name))
        elif driver_name == ConfigEnum.EDGE_DRIVER:
            self.driver = webdriver.Edge(executable_path=Util().get_driver_exe_path(driver_name))

    def setUp(self, url: str, wait_load_time_seconds: int = 0):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(wait_load_time_seconds)

    def cleanUp(self):
        self.driver.close()
        self.driver.quit()

