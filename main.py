from aiogram import *
import asyncio
import logging
from aiogram.filters import CommandStart, Command
from config import TOKEN
from aiogram.types import Message
from handler import router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher()
keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='профиль')], [KeyboardButton(text='каталог'), KeyboardButton(text='акции')]], input_field_placeholder='Выберите функцию', resize_keyboard=True)


@dp.message(CommandStart())
async def start_bot(message: Message):
    dp.include_router(router)
    await message.answer("Привет!", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())