# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def diff_max_min_frac():
    try:
        lst = list(map(float, input('Введите числа через запятую: ').split(',')))
    except ValueError:
        print('Некорректный ввод')
        print()
        diff_max_min_frac()
    else:
        least = 1
        peak = 0
        for i in lst:
            if (i - int(i)) <= least:
                least = i - int(i)
            if (i - int(i)) >= peak:
                peak = i - int(i)
        print(f'Разница между максимальным и минимальным значением дробной части элементов: {round(peak - least, 5)}')


diff_max_min_frac()
