from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states import Mailing
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api import quick_commands as commands
from data.config import admins

@dp.message_handler(text="/mailing", chat_id=admins)
async def start_mailing(message: types.Message):
    await message.answer(f"Введите текст рассылки")
    await Mailing.text.set()

@dp.message_handler(state=Mailing.text)
async def mailing_text(message: types.Message, state: FSMContext):
    answer= message.text
    markup= InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Добавить фотографию", callback_data="add_photo"),
                                         InlineKeyboardButton(text="Далее", callback_data="next"),
                                         InlineKeyboardButton(text="Отменить", callback_data="quit")
                                     ]
                                 ])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await Mailing.state1.set()

@dp.callback_query_handler(text="next", state=Mailing.state1)
async def next(call: types.CallbackQuery, state: FSMContext):
    users= await commands.select_all_users()
    data= await state.get_data()
    text= data.get("text")
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_message(chat_id=user.user_id,text=text)
        except Exception:
            pass
    await call.message.answer("Рассылка выполнена")

@dp.callback_query_handler(text="add_photo", state=Mailing.state1)
async def add_photo(call: types.CallbackQuery):
    await call.message.answer("Пришлите фото")
    await Mailing.photo.set()

@dp.message_handler(state=Mailing.photo, content_types= types.ContentType.PHOTO)
async def mailing_photo(message: types.Message, state: FSMContext):
    photo_file_id= message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data= await state.get_data()
    text= data.get("text")
    photo= data.get("photo")
    markup= InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Далее", callback_data="next"),
                                         InlineKeyboardButton(text="Отменить", callback_data="quit")
                                     ]
                                 ])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)

@dp.callback_query_handler(text="next", state=Mailing.photo)
async def next(call: types.CallbackQuery, state: FSMContext):
    users= await commands.select_all_users()
    data= await state.get_data()
    text= data.get("text")
    photo= data.get("photo")
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_photo(chat_id=user.user_id, photo=photo, caption=text)
        except Exception:
            pass
    await call.message.answer("рассылка выполнена")

@dp.message_handler(state=Mailing.photo)
async def no_photo(message: types.Message):
    markup= InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Отменить", callback_data="quit")
                                     ]
                                 ])
    await message.answer("Пришли мне фотографию", reply_markup=markup)

@dp.callback_query_handler(text="quit", state=[Mailing.text, Mailing.photo, Mailing.state1])
async def quit(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer("Рассылка отменена")
