import xml.etree.ElementTree as ET
import os
from sys import argv


def max_size(file_path):
    root = ET.parse(file_path)
    max_figure_size = 0
    max_figures = []
    for tag in root.findall('image'):
        try:
            figure_size = int(tag.get('width')) * int(tag.get('height'))
            if figure_size > max_figure_size:
                max_figure_size = figure_size
        except AttributeError:
            pass
    for tag in root.findall('image'):
        try:
            if int(tag.get('width')) * int(tag.get('height')) == max_figure_size:
                figure_name = tag.get('name')
                figure_width = tag.get('width')
                figure_height = tag.get('height')
                max_figures.append((figure_name, figure_width, figure_height))
        except AttributeError:
            pass
    return max_figures


def get_stats(file_path):
    root = ET.parse(file_path)
    total_images = 0
    fill_images = 0
    empty_images = 0
    count_figure = 0
    figure_stats = {}
    for tag in root.findall('image'):
        total_images += 1
        if list(tag):
            for figure in list(tag):
                count_figure += 1
                if figure.tag in figure_stats:
                    figure_stats[figure.tag] += 1
                else:
                    figure_stats[figure.tag] = 1
            fill_images += 1
        else:
            empty_images += 1
    return total_images, fill_images, empty_images, count_figure, figure_stats


def print_info(total_images, fill_images, empty_images, count_figure, figure_stats):
    print(f'Всего изображений: {total_images}\n'
          f'Всего изображений размечено: {fill_images}\n'
          f'Всего изображений не размечено: {empty_images}\n')

    print(f'Количество фигур всего: {count_figure}')

    print(f'\nКоличество изображений с самым большим размером: {len(max_figures)}')
    figure_name = max_figures[0][0]
    figure_width = max_figures[0][1]
    figure_height = max_figures[0][2]
    print(f'Название: {figure_name}\n'
          f'Ширина: {figure_width}\n'
          f'Высота: {figure_height}')
    print()


if __name__ == '__main__':
    for file_name in argv[1:]:
        try:
            print(f"Файл {file_name}")
            max_figures = max_size(os.path.abspath(file_name))
            total_images, fill_images, empty_images, count_figure, figure_stats = get_stats(file_name)
            print_info(total_images, fill_images, empty_images, count_figure, figure_stats)
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")