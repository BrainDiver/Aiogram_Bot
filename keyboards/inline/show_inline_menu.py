from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu= InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Инлайн кнопка 1", callback_data="Инлайн кнопка 1"),
            InlineKeyboardButton(text="Ссылка 1", url="https://google.com")
        ],
        [
            InlineKeyboardButton(text="alert", callback_data="alert")
        ]
    ]
)
