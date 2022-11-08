from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5439011304:AAGF_03sJSmc8GR7gkUhjG_3SEvadUPz3oI' # '5463053983:AAHe8kj5ahBXqRfuF-XuzJn4qZr0bqyjNtM'
storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
