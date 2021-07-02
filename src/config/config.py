import json
from enum import Enum
from src.utils.path_helper import get_project_root


class ConfigEnum(str, Enum):
    # Driver Keys
    DRIVER_PATHS = "selenium_drivers_paths",
    DRIVER_ROOT_PATH = "root_path"
    OPERA_DRIVER = "opera",
    CHROME_DRIVER = "chrome",
    EDGE_DRIVER = "edge",

    # Log config
    LOG_CONFIG = "log_config",
    FORMAT = "format",
    ROTATION = "rotation"


class Config:
    __CONFIG_FILE_JSON = None

    def __init__(self):
        __CONFIG_FILE = f"{get_project_root()}\\config.json"
        with open(__CONFIG_FILE) as json_data_file:
            self.__CONFIG_FILE_JSON = json.load(json_data_file)

    def get_value(self, key_name: str):
        value = ""
        try:
            value = self.__CONFIG_FILE_JSON[key_name]
        except KeyError as ex:
            print(f"Key {key_name} not found in a config.json")

        return value

    def get_array_value(self, array_key_name: str, filter_value: str):
        return self.__CONFIG_FILE_JSON[array_key_name][filter_value]
