# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, где находится эта точка (или на какой оси она находится). Пример: - x=34; y=-30 -> 4 -
# x=2; y=4-> 1 - x=-34; y=-30 -> 3

def inputCoordinate(x):
    num = [0] * x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f'Введите {i+1} координату: '))
                num[i] = number
                is_OK = True
                if num[i] == 0:
                    is_OK = False
                    print('Координата не должна быть равна 0 ')
            except ValueError:
                print('Ошибка ввода данных')
    return num


def checkCoordinates(xy):
    text = 4
    if xy[0] > 0 and xy[1] > 0:
        text = 1
    elif xy[0] < 0 and xy[1] > 0:
        text = 2
    elif xy[0] < 0 and xy[1] < 0:
        text = 3
    print(f'Точка находится в {text} четверти плоскости')


Coordinate = inputCoordinate(2)
checkCoordinates(Coordinate)
