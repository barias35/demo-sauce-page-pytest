from enum import Enum


class Locators(str, Enum):
    ID = "id",
    CSS = "css",
    NAME = "name",
    XPATH = "xpath",
    LINK_TEXT = "link_text",
    PARTIAL_LINK_TEXT = "partial_link_text",
    TAG_NAME = "tag",
    CLASS_NAME = "class_name"
