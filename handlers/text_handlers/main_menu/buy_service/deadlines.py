from typing import Coroutine
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot
from keyboards.reply_keyboards.back import cancleButtons

from states.buyServiceState import BuyService


async def deadline(message: types.Message, state: FSMContext) -> Coroutine:
    await BuyService.next()
    await message.answer(f"Cроки - <i>{message.text}</i>")

    async with state.proxy() as data:
        data["deadline"] = message.text

    return await bot.send_message(
        message.from_user.id,
        f"<b>{message.from_user.first_name}</b>, отправьте техническое "
        "задание. Отправить можно ссылку или текстом. Детально опишите, что вам нужно и где вам нужно",
        reply_markup=cancleButtons,
    )


def register_handlers_buy_service_deadline(dp: Dispatcher) -> None:
    dp.register_message_handler(deadline, state=BuyService.deadlines)
