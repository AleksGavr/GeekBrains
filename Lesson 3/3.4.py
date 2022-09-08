# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример: 45 -> 101101; 3 -> 11; 2 -> 10

def conv_dec_to_bin():
    try:
        var = int(input('Введите десятичное число: '))
    except ValueError:
        print('Некорректный ввод')
        print()
        conv_dec_to_bin()
    else:
        num = var
        binnum = ''
        while num > 0:
            binnum = str(num % 2) + binnum
            num = num // 2
        print(f'{var} в двоичной системе счисления: {binnum}')


conv_dec_to_bin()
