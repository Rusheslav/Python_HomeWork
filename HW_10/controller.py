from aiogram.utils import executor
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import user_interface as ui
import model as m
from bot_creator import dp, bot
import logger


class FSMpolynome(StatesGroup):
    expect_poly_one = State()
    expect_poly_two = State()


def run():
    register_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=ui.on_startup)


async def start_handler(message: types.message):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} "
                        f"подключился к боту")
    await bot.send_message(message.from_user.id, ui.greeting, reply_markup=ui.calc_menu)
    await FSMpolynome.expect_poly_one.set()


async def show_rules(callback: types.CallbackQuery, state: FSMContext):
    logger.logging.info(f"Пользователь {callback.from_user.first_name} c id {callback.from_user.id} "
                        f"просмотрел правила ввода многочленов")
    cur_state = await state.get_state()
    rules = ui.get_rules('первый' if cur_state == 'FSMpolynome:expect_poly_one' else 'второй')
    await bot.send_message(callback.from_user.id, rules, reply_markup=ui.calc_menu)


async def get_first_poly(message: types.message, state: FSMContext):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} "
                        f"ввёл первый многочлен: {message.text}")
    if m.check_poly(message.text):
        async with state.proxy() as data:
            data["poly_one"] = message.text
        await FSMpolynome.expect_poly_two.set()
        await bot.send_message(message.from_user.id, ui.get_second_poly, reply_markup=ui.calc_menu)
    else:
        await bot.send_message(message.from_user.id, ui.wrong_poly("первый"), reply_markup=ui.calc_menu)


async def get_second_poly(message: types.message, state: FSMContext):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} "
                        f"ввёл второй многочлен: {message.text}")
    poly_two = m.decode(message.text)
    if m.check_poly(poly_two):
        async with state.proxy() as data:
            poly_one = m.decode(data["poly_one"])
        result = m.encode(m.sum_poly(poly_one, poly_two))
        reply = ui.prepare_result(m.encode(poly_one), m.encode(poly_two), result)
        await bot.send_message(message.from_user.id, reply, parse_mode="HTML", reply_markup=ui.result_menu)
        await FSMpolynome.expect_poly_one.set()
    else:
        await bot.send_message(message.from_user.id, ui.wrong_poly("второй"), reply_markup=ui.calc_menu)


async def restart_handler(message: types.message):
    logger.logging.info(f"Пользователь {message.from_user.first_name} c id {message.from_user.id} "
                        f"запустил программу снова")
    await bot.send_message(message.from_user.id, ui.restart, reply_markup=ui.calc_menu)
    await FSMpolynome.expect_poly_one.set()


async def use_calculator(callback: types.CallbackQuery, state: FSMContext):
    value = callback.data
    cur_state = await state.get_state()
    async with state.proxy() as data:
        data.setdefault('polyn', 'Многочлен: ')
        match value:
            case 'indeces':
                await bot.send_message(callback.from_user.id, text=data['polyn'], reply_markup=ui.calc_menu_ind)
            case 'send':
                if (poly_one := data['polyn'].split(': ')[1]) and cur_state == 'FSMpolynome:expect_poly_one':
                    if m.check_poly(poly_one):
                        data["poly_one"] = poly_one
                        data['polyn'] = 'Многочлен: '
                        await FSMpolynome.expect_poly_two.set()
                        await bot.send_message(callback.from_user.id, ui.get_second_poly, reply_markup=ui.calc_menu)
                    else:
                        await bot.send_message(callback.from_user.id, ui.wrong_poly("первый"),
                                               reply_markup=ui.calc_menu)
                        data['polyn'] = 'Многочлен: '
                elif (poly_two := data['polyn'].split(': ')[1]) and cur_state == 'FSMpolynome:expect_poly_two':
                    poly_two = m.decode(poly_two)
                    if m.check_poly(poly_two):
                        poly_one = m.decode(data["poly_one"])
                        result = m.encode(m.sum_poly(poly_one, poly_two))
                        reply = ui.prepare_result(m.encode(poly_one), m.encode(poly_two), result)
                        await bot.send_message(callback.from_user.id, reply, parse_mode="HTML",
                                               reply_markup=ui.result_menu)
                        await FSMpolynome.expect_poly_one.set()
                        data['polyn'] = 'Многочлен: '
                    else:
                        await bot.send_message(callback.from_user.id, ui.wrong_poly("второй"),
                                               reply_markup=ui.calc_menu)
            case 'digits':
                await bot.send_message(callback.from_user.id, text=data['polyn'], reply_markup=ui.calc_menu)
            case _:
                data['polyn'] += f' {value} ' if value in '+-' else value
                await bot.send_message(callback.from_user.id, text=data['polyn'], reply_markup=ui.calc_menu)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, state="*", commands=["start", "help"])
    dp.register_callback_query_handler(show_rules, state="*", text="rules")
    dp.register_callback_query_handler(restart_handler, state="*", text="restart")
    dp.register_message_handler(get_first_poly, state=FSMpolynome.expect_poly_one)
    dp.register_message_handler(get_second_poly, state=FSMpolynome.expect_poly_two)
    dp.register_callback_query_handler(use_calculator, state="*", text="1")
    dp.register_callback_query_handler(use_calculator, state="*", text="2")
    dp.register_callback_query_handler(use_calculator, state="*", text="3")
    dp.register_callback_query_handler(use_calculator, state="*", text="4")
    dp.register_callback_query_handler(use_calculator, state="*", text="5")
    dp.register_callback_query_handler(use_calculator, state="*", text="6")
    dp.register_callback_query_handler(use_calculator, state="*", text="7")
    dp.register_callback_query_handler(use_calculator, state="*", text="8")
    dp.register_callback_query_handler(use_calculator, state="*", text="9")
    dp.register_callback_query_handler(use_calculator, state="*", text="0")
    dp.register_callback_query_handler(use_calculator, state="*", text="+")
    dp.register_callback_query_handler(use_calculator, state="*", text="-")
    dp.register_callback_query_handler(use_calculator, state="*", text="x")
    dp.register_callback_query_handler(use_calculator, state="*", text="indeces")
    dp.register_callback_query_handler(use_calculator, state="*", text="send")
    dp.register_callback_query_handler(use_calculator, state="*", text="¹")
    dp.register_callback_query_handler(use_calculator, state="*", text="²")
    dp.register_callback_query_handler(use_calculator, state="*", text="³")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁴")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁵")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁶")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁷")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁸")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁹")
    dp.register_callback_query_handler(use_calculator, state="*", text="⁰")
    dp.register_callback_query_handler(use_calculator, state="*", text="digits")
