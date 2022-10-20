# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from random import randint

k = input("Введите натуральное число: ")
while not (k.isdigit() and k != '0'):
    k = input("Неверный ввод. Введите натуральное число: ")

k = int(k)
poly = ''
for i in range(k, -1, -1):
    coef = randint(0, 100)
    if coef == 0:
        continue
    elif i == 1:
        poly += f'{coef}x + '
    elif i > 0:
        poly += f'{coef}x^{i} + '
    else:
        poly += f'{coef} = 0'

if not poly:
    poly = 'Невероятно, но все коэффициенты равны нулю'
elif poly[-1] != '0':
    poly = poly[:-2] + '= 0'

with open('file.txt', 'w') as file:
    file.write(poly)



