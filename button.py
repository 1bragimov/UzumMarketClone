from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
phones = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Iphone️")],
    ], resize_keyboard=True
)

server = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardMarkup(text="Iphone", url="https://uzum.uz/ru/category/smartfony-iphoneios-15272")]
    ]
)

