from typing import Coroutine
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot
from keyboards.reply_keyboards.back import cancleButtons

from states.buyBotState import BuyBot


async def platform(message: types.Message, state: FSMContext) -> Coroutine:
    await BuyBot.next()
    await message.answer(f"Платформа - <i>{message.text}</i>")

    async with state.proxy() as data:
        data["platform"] = message.text

    return await bot.send_message(
        message.from_user.id,
        f"<b>{message.from_user.first_name}</b>, введите сроки. "
        "Например, до 5 сентября или в течении 2 недель",
        reply_markup=cancleButtons,
    )


def register_handlers_buy_bot_platform(dp: Dispatcher) -> None:
    dp.register_message_handler(platform, state=BuyBot.platform)
