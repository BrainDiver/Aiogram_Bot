from aiogram.dispatcher.filters.state import StatesGroup, State

class Mailing(StatesGroup):
    text= State()
    state1= State()
    photo= State()
