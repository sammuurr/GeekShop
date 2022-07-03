from typing import Coroutine
from aiogram import Dispatcher, types
from config import bot
from keyboards.reply_keyboards.back import cancleButtons

from states.buyBotState import BuyBot


async def buy_bot(message: types.Message) -> Coroutine:
    await BuyBot.platform.set()
    return await bot.send_message(
        message.from_user.id,
        f"<b>{message.from_user.first_name}</b>, введите платформу "
        "на котором, хотите увидеть бота. Например - телграмм",
        reply_markup=cancleButtons,
    )


def register_handlers_buy_bot(dp: Dispatcher) -> None:
    dp.register_message_handler(
        buy_bot, lambda m: m.text and m.text == "💻 Заказать бота"
    )
