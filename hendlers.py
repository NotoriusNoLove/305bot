from dispatcher import dp
from aiogram import F
from way import *
from middleware import *


def register_handlers():
    dp.message.register(begin, F.text == "/start")
    dp.message.register(cancel, F.text == "Удалить последнее")
    dp.message.register(delete, F.text == "Обнулить")
    dp.message.register(other, F.text)
    dp.callback_query.middleware(RegisterCheck())
    dp.message.middleware(RegisterCheck())
