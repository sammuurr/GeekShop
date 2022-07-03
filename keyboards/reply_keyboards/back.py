from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttonBack = KeyboardButton("⬅ Назад")
cancleButtons = ReplyKeyboardMarkup(resize_keyboard=True)
cancleButtons.add(buttonBack)
