# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('input_text.txt', 'w') as file:
    file.write(input('Введите текст содержащий последовательность "абв": '))
with open('input_text.txt', 'r') as file:
    text = file.readline()
    conv_text = text.split()
print()
print(text)
print(conv_text)

result = ' '.join(filter(lambda x: 'абв' not in x, conv_text))
with open('final_text.txt', 'w') as file:
    file.write(f'{result}')
print(result)
