# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from re import search
from math import sin, radians

d = input('Введите значение от 0.1 до 0.0000000001: ')

while not search(r"^0\.0{0,9}1$", d):
    d = input("Неверный ввод. Убедитесь, что вводите число между 0.1 и 0.0000000001 "
              "и не используете никаких символов, кроме '0', '1' и '.': ")

pi = 999999 * sin(radians(180/999999))

print(round(pi, len(d) - 2))