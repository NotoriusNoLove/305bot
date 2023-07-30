import pickle
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from decimal import Decimal

global count, last
count = 0
last = ""


chat_id = {}
try:
    chat_id = pickle.load(open('test_file', 'rb'))
except:
    print("chat_id_list не найден")


async def begin(message: Message):
    global count, last
    chat_id[message.chat.id] = 0
    last = ""
    await message.answer(
        f'Привет я бот который будет прибавлять! сейчас число = {count}',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='+30'),
                    KeyboardButton(text='+5')
                ],
                [
                    KeyboardButton(text='+6'),
                    KeyboardButton(text='+4'),
                    KeyboardButton(text='+3')
                ],
                [
                    KeyboardButton(text='Удалить последнее'),
                    KeyboardButton(text='Обнулить')
                ]
            ],
            resize_keyboard=True
        )
    )


async def other(message: Message):
    global count, last
    try:
        text = Decimal(message.text.replace(',', '.'))
    except:
        await message.answer("invalid conver ','")
        return

    try:
        if last == text:
            chat_id[message.chat.id] += text
        else:
            last = f"-{text}"
    except:
        print(f"chat_id = {chat_id}, last = {last}")
        await message.answer("invalid number")
        last = '+0'
        return
    await message.answer(f"Число изменено на {message.text}! текущее число = {chat_id[message.chat.id]}")


async def cancel(message: Message):
    global count, last
    count = eval(f"{Decimal(str(count))}{last}")
    chat_id[message.chat.id] = eval(
        f"{Decimal(str(chat_id[message.chat.id]))}{last}")
    await message.answer(f"Число изменено на {last}! текущее число = {chat_id[message.chat.id]}")


async def delete(message: Message):
    global count, last
    chat_id[message.chat.id] = 0
    last = '+0'
    await message.answer(f"Текущее число = {chat_id[message.chat.id]}")
