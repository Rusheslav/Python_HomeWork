from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tabulate import tabulate

# Сообщения бота
greeting = """
Вас рад приветствовать бот сложения многочленов.
Введите первый многочлен для сложения или ознакомьтесь с правилами ввода, нажав на кнопку.
"""

get_second_poly = "Введите второй многочлен:"


restart = "Введите первый многочлен:"

# Меню и кнопки
rules_menu = InlineKeyboardMarkup(row_width=1)
rules_btn = InlineKeyboardButton(text="Правила ввода", callback_data="rules")
rules_menu.add(rules_btn)

result_menu = InlineKeyboardMarkup(row_width=1)
restart_btn = InlineKeyboardButton(text="Вернуться в начало", callback_data="restart")
result_menu.add(restart_btn).add(rules_btn)

restart_menu = InlineKeyboardMarkup(row_width=1)
restart_menu.add(restart_btn)

calc_menu = InlineKeyboardMarkup(row_width=1)
btn_1 = InlineKeyboardButton(text="1", callback_data="1")
btn_2 = InlineKeyboardButton(text="2", callback_data="2")
btn_3 = InlineKeyboardButton(text="3", callback_data="3")
btn_4 = InlineKeyboardButton(text="4", callback_data="4")
btn_5 = InlineKeyboardButton(text="5", callback_data="5")
btn_6 = InlineKeyboardButton(text="6", callback_data="6")
btn_7 = InlineKeyboardButton(text="7", callback_data="7")
btn_8 = InlineKeyboardButton(text="8", callback_data="8")
btn_9 = InlineKeyboardButton(text="9", callback_data="9")
btn_0 = InlineKeyboardButton(text="0", callback_data="0")
btn_plus = InlineKeyboardButton(text="+", callback_data="+")
btn_minus = InlineKeyboardButton(text="-", callback_data="-")
btn_x = InlineKeyboardButton(text="x", callback_data="x")
btn_indeces = InlineKeyboardButton(text="Индексы", callback_data="indeces")
btn_send = InlineKeyboardButton(text="Отправить многочлен", callback_data="send")
calc_menu.row(btn_1, btn_2, btn_3).row(btn_4, btn_5, btn_6).row(btn_7, btn_8, btn_9).row(btn_0, btn_plus, btn_minus)\
    .row(btn_x, btn_indeces).add(btn_send).add(rules_btn).add(restart_btn)

calc_menu_ind = InlineKeyboardMarkup(row_width=1)
btn_i1 = InlineKeyboardButton(text="¹", callback_data="¹")
btn_i2 = InlineKeyboardButton(text="²", callback_data="²")
btn_i3 = InlineKeyboardButton(text="³", callback_data="³")
btn_i4 = InlineKeyboardButton(text="⁴", callback_data="⁴")
btn_i5 = InlineKeyboardButton(text="⁵", callback_data="⁵")
btn_i6 = InlineKeyboardButton(text="⁶", callback_data="⁶")
btn_i7 = InlineKeyboardButton(text="⁷", callback_data="⁷")
btn_i8 = InlineKeyboardButton(text="⁸", callback_data="⁸")
btn_i9 = InlineKeyboardButton(text="⁹", callback_data="⁹")
btn_i0 = InlineKeyboardButton(text="⁰", callback_data="⁰")
btn_digits = InlineKeyboardButton(text="Цифры", callback_data="digits")
calc_menu_ind.row(btn_i1, btn_i2, btn_i3).row(btn_i4, btn_i5, btn_i6).row(btn_i7, btn_i8, btn_i9).\
    row(btn_i0, btn_plus, btn_minus).row(btn_x, btn_digits).add(btn_send).add(rules_btn).add(restart_btn)


# Прочее
async def on_startup(_):
    print("Бот онлайн.")


def wrong_poly(number):
    return f"Неверный ввод. Введите {number} многочлен ещё раз"


def prepare_result(poly_one, poly_two, result):
    reply = [["Многочлен 1:", poly_one],
             ["Многочлен 2:", poly_two],
             ["Результат:", result]]

    return f'<pre>{tabulate(reply)}</pre>'


def get_rules(number):
    rules = f"""
Многочлен можно вводить в следующем виде:
• 1.1x^4 - x^3 + 5,3x^2 +3x - 5 = 0
• 1.1x**4 - x**3 + 5,3x**2 +3x - 5 = 0
• 1.1x⁴ - x³ + 5,3x² +3x - 5 = 0

В качестве переменной можно использовать только "x".

Можно вводить как с пробелами, так и без.

Можно вводить как с "= 0 " в конце, так и без.

Можно вводить многочлен вручную или с помощью встроенного кнопочного калькулятора.

Введите {number} многочлен:
"""
    return rules
