# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = float(input('Введите вещественное число: '))
sumnum = 0
for i in str(num):
    if i != ".":
        sumnum += int(i)
print(f'Сумма цифр = {sumnum}')
