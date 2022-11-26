import sqlite3 as sl

TABLES = {
    '1': 'students',
    '2': 'classes',
    '3': 'unified'
}

FIELDS = {
    'students': ['id', 'surname', 'name', 'patronym',
                 'birthdate', 'phone', 'class'],
    'classes': ['id', 'room', 'teacher']
}

COLUMNS_SQL = {
    'students': """id INTEGER PRIMARY KEY,
                 surname TEXT NOT NULL,
                 name TEXT NOT NULL,
                 patronym TEXT NOT NULL,
                 birthdate TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 class TEXT NOT NULL""",

    'classes': """ id TEXT PRIMARY KEY,
                 room TEXT NOT NULL,
                 teacher TEXT NOT NULL"""
}

con = None


def db_connect(file):
    """
    Подключается к базе данных и возвращает объект Connect
    """

    global con

    try:
        con = sl.connect(file)
    except sl.Error as e:
        # TODO записать в log вместо консоли перед продакшеном
        print(f'Ошибка: {e}')


def execute_query(query, data=None):
    """
    Выполняет запрос к базе.
    Принимает sql запрос и кортеж значений для подстановки в VALUE(?,?) для исключения возможности SQL-инъекции.
    Возвращает объект Cursor.
    """

    try:
        with con:
            if data:
                if isinstance(data, list):
                    res = con.executemany(query, data)
                elif isinstance(data, tuple):
                    res = con.execute(query, data)
            else:
                res = con.execute(query)
            return res
    except sl.Error as e:
        # TODO записать в log вместо консоли перед продакшеном
        if str(e) == "UNIQUE constraint failed: classes.id":
            return 'Такой класс уже есть в базе'
        else:
            return f'Ошибка: {e}'


def create_table(table_name='students'):
    """
    Создаёт таблицу в базе данных
    """
    columns = COLUMNS_SQL[table_name]
    sql_query = f'''CREATE TABLE IF NOT EXISTS '{table_name}'(
                 {columns});'''
    execute_query(sql_query)


def get_data(table):
    """
    Возвращает все записи в таблице
    """
    if table == 'students':
        sql_query = "SELECT * FROM students ORDER BY surname"
    elif table == 'classes':
        sql_query = "SELECT * FROM classes ORDER BY id"
    elif table == 'unified':
        sql_query = """SELECT l.surname, l.name, l.patronym, l.birthdate, l.phone, l.class, r.room, r.teacher
                        FROM students l
                        LEFT JOIN classes r
                        ON l.class = r.id
                        ORDER BY surname;"""
    res = execute_query(sql_query)
    return res


def add_record(table, data):
    """
    Добавляет новую запись
    """

    columns = {
        'students': 'NULL, ?, ?, ?, ?, ?, ?',
        'classes': '?, ?, ?'
    }
    sql_query = f"INSERT INTO {table} VALUES({columns[table]})"
    return execute_query(sql_query, data)


def remove_record(s_id, table):
    """
    Удаляет запись
    """

    sql_query = f"DELETE FROM {table} WHERE id=?"
    data = (str(s_id),)
    execute_query(sql_query, data)


def search_record(field_ind, query, table, compliance=False):
    """
    Ищет запись в базе по параметру
    """

    field = FIELDS[table][int(field_ind) - 1]
    if compliance:
        sql_query = f"SELECT * FROM {table} WHERE {field}='{query}'; "
    else:
        sql_query = f"SELECT * FROM {table} WHERE {field} LIKE '%{query}%'; "
    return execute_query(sql_query).fetchall()


def check_id(r_id, table):
    """
    Проверяет, есть ли запись в введенным id в базе
    """

    data = (str(r_id),)
    sql_query = f"SELECT * FROM {table} WHERE id=?; "
    return execute_query(sql_query, data).fetchall()
