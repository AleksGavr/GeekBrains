# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = list(input('Введите текст содержащий последовательность "абв": ').split())
result = ' '.join(filter(lambda x: 'абв' not in x, text))
print(result)
