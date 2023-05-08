from aiogram import Dispatcher
from .is_hello import IsHello
from .group_chat import IsGroup
from .chat_subscriber import IsSubscriber

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsHello)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsSubscriber)
