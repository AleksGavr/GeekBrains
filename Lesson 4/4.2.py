# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

n = int(input('Введите число: '))
primes = [2]
for num in range(3, n + 1, 2):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        primes.append(num)
lst = []
for i in primes:
    while n % i == 0:
        n = n / i
        lst.append(i)
print(lst)





