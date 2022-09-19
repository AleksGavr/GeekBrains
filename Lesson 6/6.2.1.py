# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

import random

lst = [random.randrange(1, 10, 1) for i in range(8)]
print(lst)
res = list(filter(lambda x: lst.count(x) == 1, lst))
print(res)
