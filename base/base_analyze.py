import yaml
import os


def analyze_file(file_name, data_key):
    with open("./data/" + file_name, 'r', encoding='utf-8')as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        dict_data = data[data_key]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
        return list_data
