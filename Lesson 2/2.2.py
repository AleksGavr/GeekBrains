# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# извините, Сергей, использую рекурсию - с ней повеселее :-)
def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


try:
    multnum = []
    num = int(input('Введите любое натуральное число: '))
    if num == 0 or num < 0:
        print(f'К натуральным не относятся отрицательные числа, дроби и ноль.')
    elif num == 1:
        print(f'Факториал единицы это 1.')
    else:
        for i in range(1, num + 1):
            multnum.append(mult(i))
        print(f'Произведения чисел от 1 до {num}:  {multnum}.')
except ValueError:
    print('Вводить необходимо только целое число')
