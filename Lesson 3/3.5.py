# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример: для k = 8 список
# будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def lst_fibonacci_num():
    try:
        num = int(input('Введите любое натуральное число: '))
    except ValueError:
        print('Некорректный ввод')
        print()
        lst_fibonacci_num()
    else:
        fib = []
        a, b = 1, 1
        for i in range(num):
            fib.append(a)
            a, b = b, a + b
        a, b = 0, 1
        for j in range(num + 1):
            fib.insert(0, a)
            a, b = b, a - b
        print(f'Список чисел Фибоначчи для {num}: {fib}')


lst_fibonacci_num()
