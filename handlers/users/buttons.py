from aiogram import types
from keyboards.default import kb_hide
from loader import dp

@dp.message_handler(text="Кнопка 1")
async def test_buttons(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}")

@dp.message_handler(text="Кнопка 2")
async def test_buttons(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}")

@dp.message_handler(text="Кнопка 3")
async def test_buttons(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}")

@dp.message_handler(text="Кнопка 4")
async def test_buttons(message: types.Message):
    await message.answer(f"Вы выбрали {message.text}")

@dp.message_handler(text="Скрыть меню")
async def test_buttons(message: types.Message):
    await message.answer(text="Сделано",reply_markup=kb_hide)
