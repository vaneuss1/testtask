import xml.etree.ElementTree as ET
from sys import argv
import os


def figure_stats(file_path):
    root = ET.parse(file_path).getroot()
    figure_stats_dict = {}
    for tag in root.findall('image'):
        for figure in list(tag):
            if figure.tag in figure_stats_dict:
                figure_stats_dict[figure.tag] += 1
            else:
                figure_stats_dict[figure.tag] = 1
    return figure_stats_dict


def print_info(figure_stats_dict):
    print('Статистика по фигурам:')
    for key, value in figure_stats_dict.items():
        print(f'{key}: {value}')
    print()


if __name__ == '__main__':
    for file_name in argv[1:]:
        try:
            print(f"Файл {file_name}")
            f_path = os.path.abspath(file_name)
            f_stats = figure_stats(f_path)
            print_info(f_stats)
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")
