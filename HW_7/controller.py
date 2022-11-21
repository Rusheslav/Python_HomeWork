import view
import model
import logger
import ui


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
                contact = ui.get_contact()
                view.show_contact(contact)
                if ui.confirm('Сохранить контакт?'):
                    add_result = model.add_contact(contact)
                    view.print_result(add_result)
                    logger.make_record(f'Добавлен контакт "{contact["name"]}"')
                else:
                    view.print_result('Контакт не добавлен')

            case '3':
                phonebook = model.get_phonebook()
                view.show_book(phonebook)
                if phonebook:
                    contact_id = ui.get_contact_id()
                    contact = model.find_contact(contact_id)
                    if type(contact) == str:
                        view.print_result(contact)
                        logger.make_record(f'Поиск контакта по id. Контакт с id {contact_id} не найден.')
                    else:
                        view.show_contact(contact)
                        if ui.confirm('Удалить контакт?'):
                            delete_result = model.delete_contact(contact_id)
                            view.print_result(delete_result)
                            logger.make_record(f'Удалён контакт "{contact["name"]}".')
                        else:
                            view.print_result('Контакт не удалён')
            case '4':
                file_name = ui.get_file_name()
                upload_result = model.upload_contacts(file_name)
                view.print_result(upload_result)
                logger.make_record(f'Добавление контактов из файла {file_name}. {upload_result}')

            case '5':
                logger.make_record('Выход из системы')
                view.print_result('До скорых встреч!')
                running = False

            case _:
                view.print_result('Вводить можно только цифры от 1 до 5')
                continue
