from aiogram import types
from loader import dp, bot
from aiogram.types import CallbackQuery
from aiogram.dispatcher.filters import Command 
from keyboards.inline import ikb_menu, ikb_menu2

@dp.message_handler(Command("inline_menu"))
async def inline_menu(message: types.Message): 
    await message.answer(text= "Инлайн кнопки ниже", reply_markup= ikb_menu)

@dp.callback_query_handler(text="Инлайн кнопка 1")
async def change_button(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

@dp.callback_query_handler(text="alert")
async def change_button(call: CallbackQuery):
    await call.answer(text="Alert", show_alert=True)

@dp.callback_query_handler(text="Инлайн кнопка 2")
async def change_button(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu)

@dp.callback_query_handler(text="Закрыть инлайн меню")
async def change_button(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
