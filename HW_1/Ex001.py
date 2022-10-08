day = input('Введите день недели (цифрой): ')

if day in '12345':
    print('Нет')
elif day in '67':
    print('Да')
else:
    print('Неверный ввод')