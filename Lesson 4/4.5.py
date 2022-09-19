# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file_1.txt', 'w', encoding='utf-8') as file:
    file.write('x^2 + 2*x^2')
with open('file_2.txt', 'w', encoding='utf-8') as file:
    file.write('x^3 + 3*x^3')

with open('file_1.txt', 'r') as file:
    file_1 = file.readline()
    lst_of_file_1 = file_1.split()

with open('file_2.txt', 'r') as file:
    file_2 = file.readline()
    lst_of_file_2 = file_2.split()

print(f'{lst_of_file_1} + {lst_of_file_2}')
sum_files = lst_of_file_1 + lst_of_file_2

with open('sum_files.txt', 'w', encoding='utf-8') as file:
    file.write(f'{lst_of_file_1} + {lst_of_file_2}')
