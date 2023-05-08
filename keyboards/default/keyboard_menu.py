from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Кнопка 1"),
            KeyboardButton(text="Кнопка 2")
        ],
        [
            KeyboardButton(text="Кнопка 3"),
            KeyboardButton(text="Кнопка 4")
        ],
        [
            KeyboardButton(text="Скрыть меню")
        ]
    ],
    resize_keyboard= True,
    one_time_keyboard= True
)
