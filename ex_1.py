#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
# Раз это генераторы, то сгенерируем списки
print(list(field(goods,'title','price')))
print(list(field(goods,'title')))
print(list(gen_random(1,3,5)))