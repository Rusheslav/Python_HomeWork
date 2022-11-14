import csv


def get_phonebook() -> list:
    try:
        with open('contacts.csv', 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            contacts = sorted([row for row in reader], key=lambda x: (x[1] + x[2] + x[3]).lower())
            return contacts
    except FileNotFoundError:
        return []


def add_contact(contact: dict) -> str:
    try:
        with open('contacts.csv', 'r', encoding='UTF8') as f:
            reader = csv.reader(f)
            new_id = str(sum([1 for row in reader])+1)
    except FileNotFoundError:
        new_id = 1
    contact = list(contact.values())
    contact.insert(0, new_id)
    with open('contacts.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(contact)
    return f'Контакт "{contact[1]}" успешно добавлен'


def find_contact(contact_id: str) -> str or dict:
    with open('contacts.csv', 'r', encoding='UTF8') as f:
        rows = list(csv.reader(f))
        if len(rows) < int(contact_id):
            return f'Контакт с id {contact_id} не найден.'
        contact = {}
        for row in rows:
            columns_str = ['name', 'surname', 'birthdate', 'employer', 'phones']
            if row[0] == contact_id:
                for i in range(1, len(row)):
                    contact[columns_str[i - 1]] = row[i]
                break
        return contact


def delete_contact(contact_id: str) -> str:
    with open('contacts.csv', 'r', encoding='UTF8') as f:
        rows = list(csv.reader(f))
        contacts = []
        for row in rows:
            contact = {}
            columns_str = ['name', 'surname', 'birthdate', 'employer', 'phones']
            if row[0] != contact_id:
                for i in range(1, len(row)):
                    contact[columns_str[i-1]] = row[i]
                contacts.append(contact)
            else:
                name = row[1]

    with open('contacts.csv', 'w+', encoding='UTF8'):
        pass
    for contact in contacts:
        add_contact(contact)
    return f'Контакт "{name}" успешно удалён'


def upload_contacts(file_name: str) -> str:
    try:
        if not file_name[-4:] == '.csv':
            return 'Добавление контактов возможно только из файлов CSV'
        with open(file_name, 'r', encoding='UTF8') as f:
            rows = list(csv.reader(f))
            count = 0
            for row in rows:
                if len(row) == 5 and row[0] and row[4]:
                    contact = {}
                    columns_str = ['name', 'surname', 'birthdate', 'employer', 'phones']
                    for i in range(len(row)):
                        contact[columns_str[i]] = row[i]
                    add_contact(contact)
                    count += 1
            if count == len(rows):
                return f'Добавлено контактов: {len(rows)}'
            else:
                return f'Добавлено контактов: {count}. Строк отфильтровано: {len(rows) - count}'
    except FileNotFoundError:
        return f'Файл {file_name} не найден'
