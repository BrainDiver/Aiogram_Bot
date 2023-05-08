from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

class IsHello(BoundFilter):
    async def check(self, message:types.Message):
        list=["Привет", "привет"]
        return message.text in list
