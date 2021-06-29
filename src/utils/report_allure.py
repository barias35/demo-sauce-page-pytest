import allure
import moment
import uuid
from allure_commons.types import AttachmentType, Severity

from src.utils.path_helper import get_screenshots_dir
from src.utils.webdriver_setup import WebDriverHandler


class ReportAllure:

    now = moment.now().strftime("%d-%m-%Y")

    def __init__(self, driver):
        self.driver = driver

    def attach_image_file_with_step(self, step_title: str, image_name: str = None, severity_level=Severity.NORMAL):
        if image_name is None:
            image_name = uuid.uuid1()
        self.__attach_image_to_report(step_title=step_title, image_name=image_name, severity_level=severity_level)

    def attach_image_file(self, image_name: str = None, severity_level: str = Severity.NORMAL):
        if image_name is None:
            image_name = uuid.uuid1()
        self.__attach_image_to_report(image_name=image_name, severity_level=severity_level)

    def attach_image_with_step(self, step_title: str, severity_level: str = Severity.NORMAL):
        self.__attach_image_to_report(step_title=step_title, severity_level=severity_level)

    def attach_image_(self, severity_level: str = Severity.NORMAL):
        self.__attach_image_to_report(severity_level=severity_level)

    def __attach_image_to_report(self, step_title: str = None, image_name: str = None,
                                 severity_level: str = Severity.NORMAL):

        if step_title is not None:
            with allure.step(step_title):
                self.__attach_image(image_name)
        else:
            self.__attach_image()

        allure.severity(severity_level=severity_level)

    def __attach_image(self, image_name: str = None):
        if image_name is not None:
            file_name = image_name + "-" + self.now
            file = f"{get_screenshots_dir()}\\{file_name}.jpg"
            self.driver.get_screenshot_as_file(file)
            allure.attach.file(file, attachment_type=AttachmentType.JPG)
        else:
            image = self.driver.get_screenshot_as_png()
            allure.attach(image, attachment_type=AttachmentType.PNG)


class ReportAllureBuilder:

    def set_title(self, title: str):
        allure.title(title)
        return self

    def set_suite(self, suite_name: str):
        allure.suite(suite_name)
        return self

    def set_description(self, description: str):
        allure.description(description)
        return self

    def set_description(self, description: str):
        allure.description(description)
        return self
