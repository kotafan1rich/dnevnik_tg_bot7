from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/get_marks_1')
b2 = KeyboardButton('/get_marks_2')
b3 = KeyboardButton('/get_marks_3')
b4 = KeyboardButton('/get_marks_4')
b5 = KeyboardButton('/get_marks_5')
b7 = KeyboardButton('/help')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5).add(b7)
