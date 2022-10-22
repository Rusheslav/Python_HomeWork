# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from random import randint

k = input("Введите натуральное число: ")
while not (k.isdigit() and k != '0'):
    k = input("Неверный ввод. Введите натуральное число: ")

coefs = [randint(0, 100) for i in range(int(k) + 1)]
lst = coefs.reverse()
print(lst)

poly = ''

for i in range(len(coefs) - 1, -1, -1):
    if not coefs[i]:
        continue
    elif coefs[i] == 1 and i == 1:
        poly += ' + x'
    elif coefs[i] == 1 and i == 0:
        poly += ' + 1'
    elif coefs[i] == 1:
        poly += f' + x^{i}'
    elif i == 0:
        poly += f' + {coefs[i]}'
    else:
        poly += f' + {coefs[i]}x^{i}'

poly = poly[3:] + ' = 0'

print(poly)

with open('file.txt', 'w') as file:
    file.write(poly)



