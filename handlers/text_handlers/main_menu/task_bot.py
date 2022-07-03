from typing import Coroutine
from aiogram import Dispatcher, types
from config import bot


async def process_task_bot(message: types.Message) -> Coroutine:
    print(2)
    return await bot.send_message(
        message.from_user.id,
        "К сожалению это функция не работает, находится в процессе разработки",
    )


def register_handlers_task_bot(dp: Dispatcher) -> None:
    dp.register_message_handler(
        process_task_bot, lambda m: m.text and m.text == "📲 Арендовать бота"
    )
