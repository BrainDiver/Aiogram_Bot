from loader import dp
from aiogram import types
from states import Balance
from utils.db_api import quick_commands as commands
from aiogram.dispatcher import FSMContext

@dp.message_handler(text="/balance")
async def balance(message: types.Message):
    user= await commands.select_user(message.from_user.id)
    await message.answer(f"Ваш баланс {user.balance}")

@dp.message_handler(text="/change_balance")
async def change_balance(message: types.Message):
    await message.answer("Введите сумму пополнения")
    await Balance.amount.set()

@dp.message_handler(state=Balance.amount)
async def change_balance(message:types.Message, state: FSMContext):
    answer= message.text
    check_balance= await commands.check_balance(user_id=message.from_user.id, amount=answer)
    if check_balance== "no money":
        await message.answer("Нету денег")
        await state.finish()
    elif check_balance:
        await message.answer("Баланс успешно изменен")
        await state.finish()
    elif not check_balance:
        await message.answer("Некоректное число")
        await state.finish
    else:
        await message.answer("Ошибка используйте команду /start")
        await state.finish
