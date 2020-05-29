from ContextManager import OpenTimeLog
from pprint import pprint


def get_cookbook(file_input, file_output):
    """
    Принимает и читает список рецептов из файла в формате:
    Название блюда
    Количество ингредиентов в блюде
    Название ингредиента | Количество | Единица измерения
    Название ингредиента | Количество | Единица измерения
    ...
    Получает словарь в формате:
    {Название блюда: [{'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    {'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    ...],
    Название блюда: [{'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    {'ingredient_name': ' ', 'quantity': ' ', 'measure': ' '},
                    ...],
    ...}
    """
    cookbook = {}
    with OpenTimeLog(file_output):
        with open(file_input, encoding='utf8') as file:
            for line in file:
                dish = line.strip()
                if dish:
                    cookbook[dish] = []
                    count = int(file.readline())
                    for i in range(count):
                        items = file.readline().strip().split(' | ')
                        temp_dict = {'ingredient name': items[0],
                                     'quantity': items[1],
                                     'measure': items[2]}
                        cookbook[dish].append(temp_dict)
                else:
                    return cookbook
                file.readline()
    pprint(cookbook)


get_cookbook('recipes.txt', 'log.txt')
