import csv
from src.utils.path_helper import get_project_root


class DataPoolHandler(object):

    def __init__(self, file_name: str):
        dir_name = "datapools"
        self.file_path = f"{get_project_root()}\\{dir_name}\\{file_name}.csv"

    def load_datapool_single_row(self):
        with open(self.file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            temp_dict = dict(list(csv_reader)[0])
            return PropertiesGenerator(temp_dict.keys(), temp_dict.values())

    def load_datapool_list(self):
        with open(self.file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            return dict(list(csv_reader))


class PropertiesGenerator(object):
    def __init__(self, keys, values):
        for (key, value) in zip(keys, values):
            self.__dict__[key] = value

    def __setattr__(self, name, value):
        raise Exception("It is read only!")
