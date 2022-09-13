# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k. Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def create_polynomial():
    try:
        k = int(input('Введите натуральную степень: '))
        a = int(random.randint(0, 100))
        b = int(random.randint(0, 100))
        c = int(random.randint(0, 100))
    except ValueError:
        print('Некорректный ввод')
        print()
        create_polynomial()
    else:
        if a != 0:
            one = (str(a) + "x^" + str(k) + " + ")
        else:
            one = (str())

        if b != 0:
            two = (str(b) + "x" + " + ")
        else:
            two = (str())

        if c != 0:
            three = (str(c) + " = 0")
        else:
            three = (str())
        print(f'{one}{two}{three}')


create_polynomial()
