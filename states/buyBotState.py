from aiogram.dispatcher.filters.state import StatesGroup, State


class BuyBot(StatesGroup):
    platform = State()
    deadlines = State()
    task = State()
    sum = State()
