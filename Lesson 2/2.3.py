# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
try:
    n = int(input('Введите число: '))
    lst = [round((1 + 1 / i) ** i, 5) for i in range(1, n + 1)]
    print(f'Список: {lst}')
    print(f'Сумма чисел списка: {round(sum(lst), 5)}')
except ValueError:
    print('Вводить необходимо только целое число')
