# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(data):
    enconding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


with open('input_text.txt', 'w') as file:
    file.write(input('Введите текст необходимый для сжатия: '))
with open('input_text.txt', 'r') as file:
    text = file.readline()

print()
print(text)

compr_text = rle_encode(text)
print(compr_text)

with open('encode_text.txt', 'w') as file:
    file.write(f'{compr_text}')

with open('encode_text.txt', 'r') as file:
    text = file.readline()

decoded_text = rle_decode(text)
print(decoded_text)

with open('decoded_text.txt', 'w') as file:
    file.write(f'{decoded_text}')
