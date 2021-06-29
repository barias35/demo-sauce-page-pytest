import sys

sys.path.append("../../")

from loguru import logger
from src.utils.path_helper import get_project_root
from src.config.config import ConfigEnum, Config



def setUpLogger():
    __log_file_name = "logs.log"

    config_file = Config()
    format_file = config_file.get_array_value(ConfigEnum.LOG_CONFIG, ConfigEnum.FORMAT)
    rotation = config_file.get_array_value(ConfigEnum.LOG_CONFIG, ConfigEnum.ROTATION)

    logs_file_dir = f"{get_project_root().parent}\\logs\\logs.log"
    logger.add(logs_file_dir, format=format_file, rotation=rotation)


setUpLogger()
