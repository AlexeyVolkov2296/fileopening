import re
from pprint import pprint


def read_cook_book_from_file(filename):
    with open(filename, encoding='utf8') as file:
        cook_book = {}
        last_dish = ''
        for line in file:
            line = line.strip()
            if '|' not in line and len(line) and re.match('\D', line):
                cook_book.setdefault(line, [])
                last_dish = line
            elif '|' in line:
                line = line.split(' | ')
                cook_book[last_dish].append({'ingredient_name': line[0], 'quantity': int(line[1]), 'measure': line[2]})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book_from_file('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name = ingredient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list[name] = {'measure': ingredient['measure'],
                                   'quantity': ingredient['quantity'] * person_count
                                   }
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))