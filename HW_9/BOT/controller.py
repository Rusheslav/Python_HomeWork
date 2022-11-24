from aiogram.utils import executor
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
import user_interface as ui
import controller_calc as calc
import controller_db as db
from bot_creator import dp, bot
import model_db
import logger


def run():
    register_handlers(dp)
    calc.register_handlers_calc(dp)
    db.register_handlers_db(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=ui.on_startup)


async def start_handler(message: types.message):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} подключился к боту")
    await bot.send_message(message.from_user.id, 'Выберите режим работы:', reply_markup=ui.main_menu)
    await message.delete()


async def return_handler(callback: types.CallbackQuery, state: FSMContext):
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} вышел в главное меню")
    if model_db.con:
        model_db.con.close()
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await callback.message.edit_text('Выберите режим работы:', reply_markup=ui.main_menu)


async def unknown_message(message: types.message):
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(return_handler, state='*', text="return")
    dp.register_message_handler(start_handler, commands=["start", "help"])
    dp.register_message_handler(unknown_message)
