# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

def mult_two_num():
    try:
        lst = list(map(int, input('Введите числа через запятую: ').split(',')))
    except ValueError:
        print('Некорректный ввод')
        print()
        mult_two_num()
    else:
        newlst = []
        for i in range((len(lst) + 1) // 2):
            newlst.append(lst[i] * lst[len(lst) - 1 - i])
        print(f'Произведение пар чисел списка: {newlst}')


mult_two_num()
