# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Универсальный случай

def encode(data):
    repeat = False
    chars = data[0]
    res = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1] and not repeat and count == 1:
            repeat = True
            count += 1
        elif data[i] == data[i - 1] and not repeat:
            res += f'-{count - 1} {chars[:-1]} '
            count = 2
            chars = data[i]
            repeat = True
        elif data[i] == data[i - 1] and repeat:
            count += 1
        elif data[i] != data[i - 1] and repeat and count == 1:
            repeat = False
            count = 1
            chars += data[i]
        elif data[i] != data[i - 1] and repeat:
            repeat = False
            res += f'{count} {chars} '
            chars = data[i]
            count = 1
        elif data[i] != data[i - 1] and not repeat:
            chars += data[i]
            count += 1
    if not repeat:
        res += f'-{count} {chars}'
    else:
        res += f'{count} {chars}'

    return res


def decode(data):
    res = ''
    num = ''
    chars = ''
    char = False
    repeat = True
    i = 0

    while i < len(data):
        if data[i] == '-' and not char:
            repeat = False
            i += 1
        elif not char and data[i].isdigit():
            num += data[i]
            i += 1
        elif not char and data[i] == ' ':
            char = True
            i += 1
        elif char and repeat:
            res += int(num) * data[i]
            char = False
            i += 2
            num = ''
        elif char and not repeat:
            res += data[i:i + int(num)]
            char = False
            i += int(num) + 1
            repeat = True
            num = ''
    return res

with open('RLE_input.txt', 'r') as file:
    line = file.read()

encoded = encode(line)

with open('RLE_output1.txt', 'w') as file:
    file.write(encoded)

decoded = decode(encoded)

with open('RLE_output2.txt', 'w') as file:
    file.write(decoded)

# Оставляю для проверки правильности:
print(line)
print(encoded)
print(decoded)
print('Всё верно' if line == decoded else 'Макет оказался сильней...')
