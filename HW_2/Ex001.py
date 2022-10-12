# Понимаю, что функция здесь используется лишь однажды, а потому является лишней,
# но без неё не получится поиграться с рекурсией.

def get_number():
    try:
        float(number := input('Введите число: '))
        return number
    except ValueError:
        print('Ошибка ввода. Допускается только ввод чисел.', end=' ')
        return get_number()

num = get_number().replace('.', '')
print(sum([int(i) for i in num]))
