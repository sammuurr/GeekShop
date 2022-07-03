from typing import Coroutine
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot, admin_chat
from handlers.text_handlers.backButton import process_finish_state
from keyboards.reply_keyboards.back import cancleButtons

from states.buyServiceState import BuyService


async def sum(message: types.Message, state: FSMContext) -> Coroutine:
    async with state.proxy() as data:
        message_text = f"Сфера - <i>{data['platform']}</i>\nСроки - <i>{data['deadline']}</i>\nБюджет - <b>{message.text}</b>\n\nТехническое задание - <i>{data['task']}</i>"
        await message.answer(message_text)
        await bot.send_message(
            admin_chat,
            f"<b><a href='{message.from_user.url}'>{message.from_user.full_name}</a"
            f"></b>, хочет купить услуги. \n\n" + message_text,
        )

    await bot.send_message(
        message.from_user.id, f"Заказ создан, ожидайте ответа", reply_markup=cancleButtons
    )
    return await process_finish_state(message, state)


def register_handlers_buy_service_sum(dp: Dispatcher) -> None:
    dp.register_message_handler(sum, state=BuyService.sum)
