a = input('Введите координаты точки A через пробел: ').split()
b = input('Введите координаты точки B через пробел: ').split()

distance = ((int(a[0]) - int(b[0])) ** 2 + (int(a[1]) - int(b[1])) ** 2) ** 0.5
result = round(distance, 2)

print(result)