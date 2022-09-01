# 1.1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот
# день выходным. Пример: 6 -> да 7 -> да 1 -> нет

try:
    day = int(input('Введите цифру, обозначающую день недели: '))
    if 0 < day < 8:
        if day == 6 or day == 7:
            print(f'{day} - да')
        else:
            print(f'{day} - нет')
    else:
        print('В неделе 7 дней')
except ValueError:
    print(f'Ошибка ввода данных')
