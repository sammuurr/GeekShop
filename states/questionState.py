from aiogram.dispatcher.filters.state import StatesGroup, State


class Question(StatesGroup):
    question = State()
