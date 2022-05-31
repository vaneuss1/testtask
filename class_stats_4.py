import xml.etree.ElementTree as ET
import os
from sys import argv


def class_stats(f_name):
    root = ET.parse(f_name)
    cls_dict = {}
    for tag in root.findall('image'):
        for child_tag in list(tag):
            atr = child_tag.get('label')
            if atr in cls_dict:
                cls_dict[atr] += 1
            else:
                cls_dict[atr] = 1
    return cls_dict


def print_info(res):
    print('Статистика по классам:')
    for key, value in res.items():
        print(f"{key}: {value}")
    print()


if __name__ == '__main__':
    for file_name in argv[1:]:
        try:
            result = class_stats(file_name)
            print_info(result)
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")