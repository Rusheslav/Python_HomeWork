# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


num = 110
res = ''

while num:
    res = str(num % 2) + res
    num = num // 2

print(res if res else '0')
