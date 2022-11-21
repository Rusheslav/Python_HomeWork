import model

def get_contact() -> dict:
    name = input('Введите имя: ')
    while not name:
        name = input('Имя обязательно для ввода: ')
    surname = input('Введите фамилию: ')
    birthdate = input('Введите дату рождения: ')
    employer = input('Введите место работы: ')
    more_phones = True
    phones = input('Введите телефон: ')
    while not phones:
        phones = input('Введите хотя бы один номер телефона: ')
    while more_phones:
        reply = input('Введите еще один номер (для выхода введите "н"): ')
        while not reply:
            reply = input('Вы ничего не ввели. Введите номер телефона (для выхода введите "н"): ')
        if reply.lower() == 'н':
            more_phones = False
        else:
            phones += f';{reply}'
    columns = [name, surname, birthdate, employer, phones]
    contact = {}
    for i in range(len(columns)):
        contact[model.column_names[i]] = columns[i] if columns[i] else '-'
    return contact


def get_contact_id() -> str:
    contact_id = ''
    while not contact_id:
        contact_id = input('Введите id контакта, который нужно удалить: ')
        while not all(ch.isdigit() for ch in contact_id):
            contact_id = input('id должен быть положительным целым числом: ')
    return contact_id


def get_file_name() -> str:
    file_name = ''
    while not file_name:
        file_name = input('Введите имя файла: ')
    return file_name


def confirm(text: str) -> bool:
    reply = input(f'{text} ("д", если да; любой другой ввод, если нет): ')
    return reply.lower() == 'д'
