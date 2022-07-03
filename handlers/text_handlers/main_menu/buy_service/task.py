from typing import Coroutine
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot
from keyboards.reply_keyboards.back import cancleButtons

from states.buyServiceState import BuyService


async def task(message: types.Message, state: FSMContext) -> Coroutine:
    await BuyService.next()
    await message.answer(f"ТехЗадание - <i>{message.text}</i>")

    async with state.proxy() as data:
        data["task"] = message.text

    return await bot.send_message(
        message.from_user.id,
        f"<b>{message.from_user.first_name}</b>, напишите бюджет, "
        "который готовы выделить этому проекту",
        reply_markup=cancleButtons,
    )


def register_handlers_buy_service_task(dp: Dispatcher) -> None:
    dp.register_message_handler(task, state=BuyService.task)
