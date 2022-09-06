# Реализуйте алгоритм перемешивания списка.

import random

lst = [random.randint(0, 10) for i in range(10)]

print(f'Случайный список: {lst}')

for i in range(len(lst) - 1, 0, -1):
    j = random.randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]

print(f'Перемешанный список: {lst}')
