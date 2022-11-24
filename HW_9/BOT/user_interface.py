from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from tabulate import tabulate


HEADERS = {'students': ['id', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Телефон', 'Класс'],
           'classes': ['Номер', 'Кабинет', 'Руководитель']}


# основное меню
main_menu = InlineKeyboardMarkup(row_width=1)

calc_btn = InlineKeyboardButton(text="Калькулятор", callback_data="calculator")
database_btn = InlineKeyboardButton(text="База данных", callback_data="database")

main_menu.add(calc_btn).add(database_btn)

# меню возврата
return_menu = InlineKeyboardMarkup(row_width=1)

return_btn = InlineKeyboardButton(text="<< Вернуться в главное меню", callback_data="return")

return_menu.add(return_btn)

# меню базы данных
db_menu = InlineKeyboardMarkup(row_width=1)

show_db_btn = InlineKeyboardButton(text="Отобразить базу", callback_data="show_db")
add_db_btn = InlineKeyboardButton(text="Добавить запись в базу", callback_data="add_record")
remove_db_btn = InlineKeyboardButton(text="Удалить запись из базы", callback_data="remove_record")
# find_db_btn = InlineKeyboardButton(text="Найти запись в базе", callback_data="find_db")

db_menu.add(show_db_btn).add(add_db_btn).add(remove_db_btn).add(return_btn)

# меню отображения базы
show_table_menu = InlineKeyboardMarkup(row_width=1)

show_students_btn = InlineKeyboardButton(text="Таблица учеников", callback_data="show_students")
show_classes_btn = InlineKeyboardButton(text="Таблица классов", callback_data="show_classes")
show_unified_btn = InlineKeyboardButton(text="Общая таблица", callback_data="show_unified")
return_db_btn = InlineKeyboardButton(text="<< Назад", callback_data="database")

show_table_menu.add(show_students_btn).add(show_classes_btn).add(show_unified_btn).add(return_db_btn)

# меню добавления записи
add_table_menu = InlineKeyboardMarkup(row_width=1)

add_students_btn = InlineKeyboardButton(text="Таблица учеников", callback_data="add_students")
add_classes_btn = InlineKeyboardButton(text="Таблица классов", callback_data="add_classes")
return_db_btn = InlineKeyboardButton(text="<< Назад", callback_data="database")

add_table_menu.add(add_students_btn).add(add_classes_btn).add(return_db_btn)

# меню возврата из добавления записи
return_db_menu = InlineKeyboardMarkup(row_width=1)

return_db_menu.add(return_db_btn)

# меню подтверждения записи
confirm_record_menu = InlineKeyboardMarkup(row_width=1)

yes_record_btn = InlineKeyboardButton(text="Сохранить", callback_data="make_record")

confirm_record_menu.add(yes_record_btn).add(return_db_btn)

# меню удаления записи
remove_table_menu = InlineKeyboardMarkup(row_width=1)

remove_students_btn = InlineKeyboardButton(text="Таблица учеников", callback_data="remove_students")
remove_classes_btn = InlineKeyboardButton(text="Таблица классов", callback_data="remove_classes")

remove_table_menu.add(remove_students_btn).add(remove_classes_btn).add(return_db_btn)

# меню подтверждения удаления
confirm_remove_menu = InlineKeyboardMarkup(row_width=1)

yes_remove_btn = InlineKeyboardButton(text="Удалить", callback_data="delete_record")

confirm_remove_menu.add(yes_remove_btn).add(return_db_btn)

async def on_startup(_):
    print("Бот онлайн.")


def show_table(data, table):
    """
    Вывод таблицы
    """
    headers = HEADERS['students'][1:] + HEADERS['classes'][1:] if table == 'unified' else HEADERS[table]
    values = list(data)
    res = []

    for row in values:
        for i in range(len(row)):
            line = [f'{headers[i]}:', row[i]]
            res.append(line)
        res.append([""])

    return f'<pre>{tabulate(res)}</pre>'


def show_record(record, table, start=0):
    """
    Вывод записи из таблицы
    """

    if len(record) < len(HEADERS[table]):
        start = 1
    result = list(zip(HEADERS[table][start:], record))
    return f'<pre>{tabulate(result)}</pre>'
