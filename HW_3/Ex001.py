# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from decimal import Decimal, InvalidOperation

while True:
    lst = input('Введите список чисел через запятую: ').split(',')
    try:
        lst = [Decimal(i.strip()) for i in lst]
        break
    except InvalidOperation:
        print('Ошибка ввода. Убедитесь, что вы вводите только числа.\n'
              'Дробная часть числа должна отделяться от целой части при помощи точки(".")')

print(sum(lst[i] for i in range(len(lst)) if i % 2 == 1))
