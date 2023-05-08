from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_hide= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/menu")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
