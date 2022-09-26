from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('1 четврть')
b2 = KeyboardButton('2 четврть')
b3 = KeyboardButton('3 четврть')
b4 = KeyboardButton('4 четврть')
b5 = KeyboardButton('год')
b7 = KeyboardButton('help')
b8 = KeyboardButton('password')
b9 = KeyboardButton('login')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5).row(b9, b8).add(b7)
