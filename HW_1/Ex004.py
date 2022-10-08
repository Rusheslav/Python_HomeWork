quadrant = input('Введите номер четверти: ')

if quadrant == '1':
    print('x > 0, y > 0')
elif quadrant == '2':
    print('x < 0, y > 0')
elif quadrant == '3':
    print('x < 0, y < 0')
elif quadrant == '4':
    print('x > 0, y < 0')
else:
    print('Ошибка ввода')