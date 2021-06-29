from src.config.config import Config, ConfigEnum


class Util:

    def get_driver_exe_path(self, driver_name: str):
        return self.__get_exe_path_config(driver_name)

    def __get_exe_path_config(self, driver_name: str):
        root_path = Config().get_array_value(ConfigEnum.DRIVER_PATHS.value, ConfigEnum.DRIVER_ROOT_PATH)
        exe_path = Config().get_array_value(ConfigEnum.DRIVER_PATHS.value, driver_name)
        return f"{root_path}\\{exe_path}"


