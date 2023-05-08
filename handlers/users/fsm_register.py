from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import register

@dp.message_handler(Command("register"))
async def register_(message: types.Message):
    await message.answer("Вы начали регистрацию \nВведите имя")
    await register.test1.set()

@dp.message_handler(state=register.test1)
async def state1(message: types.Message, state= FSMContext):
    answer=message.text
    await state.update_data(test1=answer)
    await message.answer("Сколько вам лет?")
    await register.test2.set()

@dp.message_handler(state=register.test2)
async def state2(message: types.Message, state=FSMContext):
    answer=message.text
    await state.update_data(test2=answer)
    data= await state.get_data()
    name= data.get("test1")
    years= data.get("test2")
    await message.answer(f"Регистрация завершена\n"
                         f"Ваше имя {name}\n"
                         f"Ваш возраст {years}")

    await state.finish()
