from aiogram.dispatcher.filters.state import StatesGroup, State


class BuyService(StatesGroup):
    platform = State()
    deadlines = State()
    task = State()
    sum = State()
