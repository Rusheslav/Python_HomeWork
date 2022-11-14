import view
import model
import logger


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
    columns_str = ['name', 'surname', 'birthdate', 'employer', 'phones']
    contact = {}
    for i in range(len(columns)):
        contact[columns_str[i]] = columns[i] if columns[i] else '-'
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


def run() -> None:
    logger.make_record('Вход в систему')
    running = True
    while running:
        view.show_menu()
        user_choice = ''
        while not user_choice:
            user_choice = input('Выберите действие: ')

        match user_choice:
            case '1':
                phonebook = model.get_phonebook()
                if not phonebook:
                    view.print_result('Список контактов пуст')
                else:
                    logger.make_record('Вызов списка контактов')
                    view.show_book(phonebook)

            case '2':
                contact = get_contact()
                view.show_contact(contact)
                if confirm('Сохранить контакт?'):
                    add_result = model.add_contact(contact)
                    view.print_result(add_result)
                    logger.make_record(f'Добавлен контакт "{contact["name"]}"')
                else:
                    view.print_result('Контакт не добавлен')

            case '3':
                phonebook = model.get_phonebook()
                view.show_book(phonebook)
                if phonebook:
                    contact_id = get_contact_id()
                    contact = model.find_contact(contact_id)
                    if type(contact) == 'str':
                        view.print_result(contact)
                        logger.make_record(f'Поиск контакта по id. Контакт с id {contact_id} не найден.')
                    else:
                        view.show_contact(contact)
                        if confirm('Удалить контакт?'):
                            delete_result = model.delete_contact(contact_id)
                            view.print_result(delete_result)
                            logger.make_record(f'Удалён контакт "{contact["name"]}".')
                        else:
                            view.print_result('Контакт не удалён')
            case '4':
                file_name = get_file_name()
                upload_result = model.upload_contacts(file_name)
                view.print_result(upload_result)
                logger.make_record(f'Добавление контактов из файла {file_name}. {upload_result}')

            case '5':
                logger.make_record('Выход из системы')
                view.print_result('До скорых встреч!')
                running = False

            case _:
                continue
