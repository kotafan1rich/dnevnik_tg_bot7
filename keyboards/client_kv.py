from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('1 четверть')
b2 = KeyboardButton('2 четверть')
b3 = KeyboardButton('3 четверть')
b4 = KeyboardButton('4 четверть')
b5 = KeyboardButton('Год')
b7 = KeyboardButton('help')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5).add(b7)
