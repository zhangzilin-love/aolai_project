import yaml
import os


def analyze_file(data_key, file_name):
    with open("." + os.sep + "data" + os.sep + file_name, 'r')as f:
        data = yaml.load(f)
        dict_data = data[data_key]
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
        return list_data
