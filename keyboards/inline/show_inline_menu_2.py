from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu2= InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Инлайн кнопка 2", callback_data="Инлайн кнопка 2"),
            InlineKeyboardButton(text="Ссылка 2", url="https://youtube.com")
        ],
        [
            InlineKeyboardButton(text="Закрыть инлайн меню", callback_data="Закрыть инлайн меню")
        ]
    ]
)
