from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import user_interface as ui
import model_calc as mc
from bot_creator import bot
from decimal import DivisionByZero
import logger


class FSMExpr(StatesGroup):
    expr = State()


async def start_calc(callback: types.CallbackQuery, state: FSMContext):
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} открыл калькулятор")
    msg = await callback.message.edit_text("Введите и отправьте мне выражение.", reply_markup=ui.return_menu)
    await FSMExpr.expr.set()
    async with state.proxy() as data:
        data['msg'] = msg


async def process_expression(message: types.message, state: FSMContext):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} ввел "
                        f"в калькулятор выражение {message.text}")
    try:
        result, expr = mc.calculate(message.text)
        reply = f'{expr} = {result}'
    except DivisionByZero:
        reply = f'{message.text}: Вы пытаетесь поделить на ноль'
    except:
        reply = """
        Неверный ввод.
Ко вводу принимаются только цифры и символы:
"," или "." - для отделения целой части от дробной
"/" - для деления
"*" или "x" - для умножения
"+" - для сложения
"-" - для вычитания
"(", ")" - для определения очерёдности действий.
    
Выражение должно быть корректным с точки зрения математической записи.
        """
    async with state.proxy() as data:
        data['name'] = message.text
        msg_id = data['msg']['message_id']
        chat_id = data['msg']['chat']['id']
    await bot.edit_message_text(message_id=msg_id, chat_id=chat_id, text=reply, reply_markup=ui.return_menu)
    await message.delete()


def register_handlers_calc(dp: Dispatcher):
    dp.register_callback_query_handler(start_calc, text="calculator")
    dp.register_message_handler(process_expression, state=FSMExpr.expr)
