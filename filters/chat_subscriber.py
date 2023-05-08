from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot
from data import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        for chat_id in config.chat_id:
            sub= await bot.get_chat_member(chat_id=config.chat_id, user_id= message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                return True
            else:
                markup= InlineKeyboardMarkup(row_width=2, 
                                             keyboard=[
                                                 [InlineKeyboardButton(text= "Чат", url="https://t.me/+aoZ6IAvVb89mZTY6")]
                                             ])
                await dp.bot.send_message(chat_id= message.from_user.id, text= "Подпишитесь на наш телеграм чат и повторите попытку",reply_markup=markup) #text=f"Подпишитесь на телеграмм чат: https://t.me/+aoZ6IAvVb89mZTY6")
                return False
