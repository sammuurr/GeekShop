from typing import Coroutine

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot
from keyboards.reply_keyboards.main_menu import main_menu_keyboards


async def process_finish_state(message: types.Message, state: FSMContext) -> Coroutine:
    await state.finish()
    return await bot.send_message(
        message.from_user.id,
        "<b>Приветствуем</b> вас в пространстве IT технологий!"
        "Мы команда профессиональных программистов  💻<b>Geek Shop</b>💻\n\n",
        reply_markup=main_menu_keyboards,
    )


def register_handlers_back_button(dp: Dispatcher) -> None:
    """This function registers handlers to handle text

    :param: dp
    """

    dp.register_message_handler(
        process_finish_state, lambda m: m.text and m.text == "⬅ Назад", state="*"
    )
