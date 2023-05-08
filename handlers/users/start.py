from aiogram import types
from loader import dp
from filters import IsHello
from utils.misc import rate_limit

#@rate_limit(limit=5, key="/start")
#@dp.message_handler(text="/start")
#async def command_start(message: types.Message):
    #await message.answer(f"Привет {message.from_user.full_name} \n"
                         #f"Твой айди: {message.from_user.id}")

@dp.message_handler(IsHello())
async def hello(message: types.Message):
    await message.answer("Hello")
