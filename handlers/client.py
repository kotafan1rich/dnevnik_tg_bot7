from aiogram import types, Dispatcher
from create_bot import bot
from handlers import other
from keyboards import kb_client
from create_bot import dp
from db import Database

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


@dp.message_handler(commands=['login'])
async def get_login(message: types.Message):
    if len(message.text.split()) > 2:
        res = 'Логин не должен содержать пробелов'
    else:
        login = message.text.split()[1]
        db.set_login(login=login, user_id=message.from_user.id)
        res = f'Ваш логин {login} был добавлен'
    await bot.send_message(message.chat.id, res)


@dp.message_handler(commands=['password'])
async def get_password(message: types.Message):
    password = message.text.split()[1]
    await db.set_password(password=password, user_id=message.from_user.id)
    await bot.send_message(message.chat.id, f'Ваш пароль {password} был добавлен')


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
        await bot.send_message(message.chat.id, 'Ошибка... оценки не найдены, попробуйте ещё раз')


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
        await bot.send_message(message.chat.id, 'Ошибка... оценки не найдены, попробуйте ещё раз')


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
        await bot.send_message(message.chat.id, 'Ошибка... оценки не найдены, попробуйте ещё раз')


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
        await bot.send_message(message.chat.id, 'Ошибка... оценки не найдены, попробуйте ещё раз')


async def get_marks_5(message: types.Message):
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
        await bot.send_message(message.chat.id, 'Ошибка... оценки не найдены, попробуйте ещё раз')


async def get_help(message: types.Message):
    await bot.send_message(message.chat.id, help)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_start, commands='start')
    dp.register_message_handler(get_help, text=['help'])
    dp.register_message_handler(get_marks_1, text=['1 четврть'])
    dp.register_message_handler(get_marks_2, text=['2 четврть'])
    dp.register_message_handler(get_marks_3, text=['3 четврть'])
    dp.register_message_handler(get_marks_4, text=['4 четврть'])
    dp.register_message_handler(get_marks_5, text=['5 четврть'])
