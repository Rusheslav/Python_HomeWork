from tabulate import tabulate


def show_menu() -> None:
    print('''
    1. Показать контакты
    2. Добавить контакт
    3. Удалить контакт
    4. Загрузить контакты из файла
    5. Выйти
    ''')


def show_book(book: list) -> None:
    for contact in book:
        contact[-1] = contact[-1].replace(';', '\n')
    headers = ['id', 'Имя', 'Фамилия', 'Дата рождения', 'Место работы', 'Телефоны']
    print(tabulate(book, headers=headers, tablefmt='fancy_grid'))


def show_contact(contact: list) -> None:
    table = [
        ['Имя', contact['name']],
        ['Фамилия', contact['surname']],
        ['Дата рождения', contact['birthdate']],
        ['Место работы', contact['employer']],
        ['Телефоны', contact['phones']]
        ]
    print(tabulate(table, tablefmt='fancy_grid'))


def print_result(result:str) -> None:
    print(f'\n~~{result}~~')
