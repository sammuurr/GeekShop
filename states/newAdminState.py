from aiogram.dispatcher.filters.state import StatesGroup, State


class NewAdmin(StatesGroup):
    adminId = State()
