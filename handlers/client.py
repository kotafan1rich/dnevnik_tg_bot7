from aiogram import types, Dispatcher
from create_bot import bot
from handlers import other
from keyboards import kb_client
from keyboards import kb_login_password
from create_bot import dp
from db import Database
import os

db = Database('db_dnevnik_tg_bot.db')

help = '''
После запуска бота введите:
/login <логин гос-услуг>
/password <пароль гос-услуг>
для получения своего среднего балла нажмите на соответствующие кнопки (5 = год)
Все вопросы и отзывы сюда --> https://t.me/Gohdot.
'''


async def get_start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)

    await bot.send_message(message.chat.id, help, reply_markup=kb_client)


async def get_login_handler(message: types.Message):
    await bot.send_message(message.chat.id, 'Ведите логин от гос услуг', reply_markup=kb_login_password)

    @dp.message_handler()
    async def get_login(message_login):
        print(0)
        if message_login.text == 'Отмена':
            await bot.send_message(message.chat.id, 'Отменено', reply_markup=kb_client)
        else:
            if len(message.text.split()) > 2:
                res = 'Логин не должен содержать пробелов'
            else:
                login = message_login.text
                db.set_login(login=login, user_id=message_login.from_user.id)
                res = f'Ваш логин {login} был добавлен'
                try:
                    os.remove(f'cookies/cookies{message.chat.id}')
                except FileNotFoundError:
                    pass
            await bot.send_message(message_login.chat.id, res, reply_markup=kb_client)


async def get_password_hadler(message: types.Message):
    await bot.send_message(message.chat.id, 'Введите пароль от гос услуг', reply_markup=kb_login_password)

    @dp.message_handler()
    async def get_password(message_password: types.Message):
        print(1)
        if message_password.text == 'Отмена':
            await bot.send_message(message.chat.id, 'Отменено', reply_markup=kb_client)
        else:
            password = message_password.text
            db.set_password(password=password, user_id=message_password.from_user.id)
            await bot.send_message(message.chat.id, 'Ваш пароль был добавлен', reply_markup=kb_client)
            try:
                os.remove(f'cookies/cookies{message.chat.id}')
            except FileNotFoundError:
                pass


async def get_marks_1(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'Подождите...')
        quater = int(message.text[0])
        if quater > 5:
            res = 'четверть длжна быть меньше или равна 5, чтобы получить результат'
            await bot.send_message(message.chat.id, res)
        else:
            res = other.get_m_result(quater, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, res)
    except AttributeError:
        await bot.send_message(message.chat.id, 'Ошибка... Оценки не найдены, попробуйте ещё раз')


async def get_marks_2(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'Подождите...')
        quater = int(message.text[0])
        if quater > 5:
            res = 'четверть длжна быть меньше или равна 5, чтобы получить результат'
            await bot.send_message(message.chat.id, res)
        else:
            res = other.get_m_result(quater, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, res)
    except AttributeError:
        await bot.send_message(message.chat.id, 'Ошибка... Оценки не найдены, попробуйте ещё раз')


async def get_marks_3(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'Подождите...')
        quater = int(message.text[0])
        if quater > 5:
            res = 'четверть длжна быть меньше или равна 5, чтобы получить результат'
            await bot.send_message(message.chat.id, res)
        else:
            res = other.get_m_result(quater, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, res)
    except AttributeError:
        await bot.send_message(message.chat.id, 'Ошибка... Оценки не найдены, попробуйте ещё раз')


async def get_marks_4(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'Подождите...')
        quater = int(message.text[0])
        if quater > 5:
            res = 'четверть длжна быть меньше или равна 5, чтобы получить результат'
            await bot.send_message(message.chat.id, res)
        else:
            res = other.get_m_result(quater, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, res)
    except AttributeError:
        await bot.send_message(message.chat.id, 'Ошибка... Оценки не найдены, попробуйте ещё раз')


async def get_marks_5(message: types.Message):
    try:
        await bot.send_message(message.chat.id, 'Подождите...')
        quater = 5
        if quater > 5:
            res = 'четверть длжна быть меньше или равна 5, чтобы получить результат'
            await bot.send_message(message.chat.id, res)
        else:
            res = other.get_m_result(quater, user_id=message.from_user.id)
            await bot.send_message(message.chat.id, res)
    except AttributeError:
        await bot.send_message(message.chat.id, 'Ошибка... Оценки не найдены, попробуйте ещё раз')


async def get_help(message: types.Message):
    await bot.send_message(message.chat.id, help)


def register_handlers_client(disp: Dispatcher):
    disp.register_message_handler(get_start, commands='start')
    disp.register_message_handler(get_help, text=['help'])
    disp.register_message_handler(get_marks_1, text=['1 четврть'])
    disp.register_message_handler(get_marks_2, text=['2 четврть'])
    disp.register_message_handler(get_marks_3, text=['3 четврть'])
    disp.register_message_handler(get_marks_4, text=['4 четврть'])
    disp.register_message_handler(get_marks_5, text=['год'])
    disp.register_message_handler(get_login_handler, text=['login'])
    disp.register_message_handler(get_password_hadler, text=['password'])
