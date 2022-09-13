# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

import random

lst = [random.randint(0, 10) for i in range(10)]
print(lst)
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(new_lst)
