from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tabulate import tabulate

# Сообщения бота
greeting = """
Вас рад приветствовать бот сложения многочленов.
Введите первый многочлен для сложения или ознакомьтесь с правилами ввода, нажав на кнопку.
"""

rules = """
Многочлен можно вводить в следующем виде:
• 1.1x^4 - x^3 + 5,3x^2 +3x - 5 = 0
• 1.1x**4 - x**3 + 5,3x**2 +3x - 5 = 0
• 1.1x⁴ - x³ + 5,3x² +3x - 5 = 0

В качестве переменной можно использовать только "x".

Можно вводить как с пробелами, так и без.

Можно вводить как с "= 0 " в конце, так и без.

Введите первый многочлен:
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
