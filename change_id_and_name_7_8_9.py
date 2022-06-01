import xml.etree.ElementTree as ET
import os
from sys import argv


def reverse_id(file_name):
    root = ET.parse(os.path.abspath(file_name))
    reverse_ids = list(reversed([tag.get('id') for tag in root.findall('image')]))
    for tag in root.findall('image'):
        new_format = 'png'
        tag.attrib['name'] = f"{tag.attrib['name'].split('/')[-1].split('.')[0]}.{new_format}"
        tag.attrib['id'] = reverse_ids[0]
        del reverse_ids[0]
    root.write(f"{file_name.split('.')[0]}_new.xml", encoding='utf-8')


if __name__ == '__main__':
    for file_name in argv[1:]:
        try:
            print(f"Файл {file_name}")
            reverse_id(file_name)
            print('Процедура прошла успешно!\n')
        except FileNotFoundError:
            print(f"Файл {file_name} не найден.")




