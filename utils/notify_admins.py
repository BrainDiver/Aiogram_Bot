import logging
from aiogram import Dispatcher
from data.config import admins

async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text="Бот запущен и готов к работе"
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as error:
            logging.exception(error)

async def on_shutdown_notify(dp:Dispatcher):
    for admin in admins:
        try:
            text="Бот выключен"
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as error:
            logging.exception(error)
