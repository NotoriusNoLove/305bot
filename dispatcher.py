from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.fsm.strategy import FSMStrategy
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())
