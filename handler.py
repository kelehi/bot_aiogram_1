import requests
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import *
import requests

router = Router()

inline_keyboard_2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Каталог", callback_data="catalog")]])


@router.message(Command('help'))
async def start_bot(message: Message):
    await message.answer("bot")


# @router.message()
# async def start_(message: Message):
#     return_request = ""
#     try:
#         return_request = str(requests.get(str(message.text)).status_code)
#     except BaseException as e:
#         return_request = str(e)
#     finally:
#         await message.answer(return_request)


@router.callback_query(F.data == 'catalog')
async def get_bot(callback: CallbackQuery):
    print(1)
    await callback.message.answer("get")


@router.message(F.text == 'профиль')
async def get_bot(message: Message):
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{message.from_user.first_name}_{message.from_user.id}", url=f"http://127.0.0.1:8000/bot_test/{message.from_user.first_name}_{message.from_user.id}")]])
    t = requests.get(f"http://127.0.0.1:8000/bot_test/{message.from_user.first_name}_{message.from_user.id}")
    await message.answer(f"{message.from_user.first_name}_{message.from_user.id}_{t.status_code}", reply_markup=inline_keyboard)
    await message.answer(f"{t.json()}")


# @router.message(F.text == 'профиль')
# async def get_bot(message: Message):
#     await message.edit_text(f"{message.from_user.first_name}_{message.from_user.id}", reply_markup=inline_keyboard)


def function():
    keyboard_bulder = InlineKeyboardBuilder()
    c = ["status_code", "json", "url"]
    for i in c:
        keyboard_bulder.add(InlineKeyboardButton(text=i, url='https://ya.ru'))
    return keyboard_bulder.adjust(2).as_markup()


