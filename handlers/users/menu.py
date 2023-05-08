from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.default import kb_menu
from loader import dp

@dp.message_handler(Command("menu"))
async def keyboard_menu(message: types.Message):
    await message.answer(f"Сделайте свой выбор", reply_markup=kb_menu)

