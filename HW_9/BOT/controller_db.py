from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import model_db as db
import user_interface as ui
from bot_creator import bot
import logger


class FSMdb(StatesGroup):
    surname = State()
    name = State()
    patronym = State()
    birthdate = State()
    phone = State()
    class_ = State()
    class_id = State()
    room = State()
    teacher = State()
    make_record = State()
    students_id = State()
    classes_id = State()
    ask_remove = State()


fsm_dict = {
    "surname": {
        "state": FSMdb.name.set,
        "rus_word": "имя ученика"
    },
    "name": {
        "state": FSMdb.patronym.set,
        "rus_word": "отчество ученика"
    },
    "patronym": {
        "state": FSMdb.birthdate.set,
        "rus_word": "дату рождения ученика"
    },
    "birthdate": {
        "state": FSMdb.phone.set,
        "rus_word": "телефон ученика"
    },
    "phone": {
        "state": FSMdb.class_.set,
        "rus_word": "класс ученика"
    },
    "class_": None,
    "class_id": {
        "state": FSMdb.room.set,
        "rus_word": "кабинет класса"
    },
    "room": {
        "state": FSMdb.teacher.set,
        "rus_word": "ФИО классного руководителя"
    },
    "teacher": None
}


async def start_db(callback: types.CallbackQuery, state: FSMContext):
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} вошел в раздел базы данных")
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    db.db_connect('school.db')
    db.create_table('students')
    db.create_table('classes')
    await callback.message.edit_text("Выберите действие:", reply_markup=ui.db_menu)


async def show_table(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите таблицу для отображения:", reply_markup=ui.show_table_menu)


async def print_results(callback: types.CallbackQuery):
    table = callback.data.split("_")[1]
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} просмотрел таблицу {table}")
    data = db.get_data(table)
    reply = ui.show_table(data, table)
    if reply == '<pre></pre>':
        reply = 'База пуста'
    await callback.message.edit_text(reply, parse_mode="HTML", reply_markup=ui.db_menu)


async def add_record(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите таблицу для записи:", reply_markup=ui.add_table_menu)


async def start_record(callback: types.CallbackQuery, state: FSMContext):
    value = callback.data.split("_")[1]
    if value == "students":
        msg = await callback.message.edit_text("Введите фамилию ученика:", reply_markup=ui.return_db_menu)
        await FSMdb.surname.set()
    else:
        msg = await callback.message.edit_text("Введите номер класса:", reply_markup=ui.return_db_menu)
        await FSMdb.class_id.set()
    async with state.proxy() as data:
        data['msg'] = msg


async def get_value(message: types.message, state: FSMContext):
    cur_state = await state.get_state()
    value = cur_state.split(":")[1]
    async with state.proxy() as data:
        data[value] = message.text
        msg_id = data['msg']['message_id']
        chat_id = data['msg']['chat']['id']
    await message.delete()
    if value in ["class_", "teacher"]:
        if value == "class_":
            table = "students"
            full_data = tuple(data[i] for i in list(fsm_dict.keys())[:6])
        else:
            table = "classes"
            full_data = tuple(data[i] for i in list(fsm_dict.keys())[6:])
        record = ui.show_record(full_data, table)
        async with state.proxy() as data:
            data["record"] = (full_data, table)
        text = f"""
Сохранить запись?
{record}
        """
        await bot.edit_message_text(message_id=msg_id, chat_id=chat_id,
                                    text=text, parse_mode="HTML",
                                    reply_markup=ui.confirm_record_menu)
        await FSMdb.make_record.set()
    else:
        await fsm_dict[value]["state"]()
        await bot.edit_message_text(message_id=msg_id, chat_id=chat_id,
                                text=f"Введите {fsm_dict[value]['rus_word']}:", reply_markup=ui.return_db_menu)


async def make_record(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        record = data["record"][0]
        table = data["record"][1]
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} "
                        f"добавил запись {record} в таблицу {table}")
    if type(msg := db.add_record(table, record)) == str:
        await callback.message.edit_text(msg, reply_markup=ui.db_menu)
    else:
        await callback.message.edit_text("Запись успешно внесена", reply_markup=ui.db_menu)
    await state.finish()


async def remove_record(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите таблицу для удаления записи:", reply_markup=ui.remove_table_menu)


async def get_id(callback: types.CallbackQuery, state: FSMContext):
    value = callback.data.split("_")[1]
    if value == "students":
        msg = await callback.message.edit_text("Введите id ученика:", reply_markup=ui.return_db_menu)
        await FSMdb.students_id.set()
    else:
        msg = await callback.message.edit_text("Введите номер класса:", reply_markup=ui.return_db_menu)
        await FSMdb.classes_id.set()
    async with state.proxy() as data:
        data['msg'] = msg


async def check_id(message: types.message, state: FSMContext):
    cur_state = await state.get_state()
    table = cur_state.split(":")[1].split("_")[0]
    find_id = message.text
    async with state.proxy() as data:
        msg_id = data['msg']['message_id']
        chat_id = data['msg']['chat']['id']
    await message.delete()
    if not db.check_id(find_id, table):
        await bot.edit_message_text(message_id=msg_id, chat_id=chat_id,
                                    text=f'Записи с id "{find_id}" нет в базе.', reply_markup=ui.db_menu)
        await state.finish()
    else:
        full_data = db.search_record('1', find_id, table, compliance=True)
        record = ui.show_record(*full_data, table)
        async with state.proxy() as data:
            data['record'] = (find_id, table)
        text = f"""
Удалить запись?
{record}
                """
        await bot.edit_message_text(message_id=msg_id, chat_id=chat_id, parse_mode="HTML",
                                    text=text, reply_markup=ui.confirm_remove_menu)
        await FSMdb.ask_remove.set()


async def delete_record(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        find_id = data["record"][0]
        table = data["record"][1]
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id}"
                        f"удалил запись с id {find_id} из таблицы {table}")

    db.remove_record(find_id, table)
    await callback.message.edit_text("Запись успешно удалена", reply_markup=ui.db_menu)
    await state.finish()


def register_handlers_db(dp: Dispatcher):
    dp.register_callback_query_handler(start_db, state="*", text="database")
    dp.register_callback_query_handler(show_table, text="show_db")
    dp.register_callback_query_handler(print_results, text="show_students")
    dp.register_callback_query_handler(print_results, text="show_classes")
    dp.register_callback_query_handler(print_results, text="show_unified")
    dp.register_callback_query_handler(add_record, text="add_record")
    dp.register_callback_query_handler(start_record, text="add_students")
    dp.register_callback_query_handler(start_record, text="add_classes")
    dp.register_callback_query_handler(remove_record, text="remove_record")
    dp.register_callback_query_handler(get_id, text="remove_students")
    dp.register_callback_query_handler(get_id, text="remove_classes")
    dp.register_message_handler(check_id, state=FSMdb.students_id)
    dp.register_message_handler(check_id, state=FSMdb.classes_id)
    dp.register_callback_query_handler(delete_record, state=FSMdb.ask_remove, text="delete_record")
    dp.register_callback_query_handler(make_record, state=FSMdb.make_record, text="make_record")
    dp.register_message_handler(get_value, state="*")
