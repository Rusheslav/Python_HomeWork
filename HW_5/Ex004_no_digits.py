# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Для случая без цифр

line = "wwwwwwWWWWWWWWWbBBBBBBBBBBBBB"


def encode(data):
    letter = data[0]
    res = ''
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        elif data[i] != data[i - 1]:
            res += str(count)
            res += letter
            letter = data[i]
            count = 1

    res += str(count) + letter
    return res


def decode(data):
    res = ''
    num = ''
    for i in range(len(data)):
        if data[i].isdigit():
            num += data[i]
        else:
            res += data[i] * int(num)
            num = ''
    return res


encoded = encode(line)
print(encoded)
print(decode(encoded))
print(line == decode(encoded))
