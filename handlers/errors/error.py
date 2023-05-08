from aiogram import types
from loader import dp

@dp.message_handler()
async def error(message: types.Message):
    await message.answer(f"Такой команды нет :{message.text}")
