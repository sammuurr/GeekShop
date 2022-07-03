from typing import Coroutine

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config import bot, admin_chat
from handlers.text_handlers.backButton import process_finish_state
from keyboards.reply_keyboards.back import cancleButtons
from states.questionState import Question


async def process_question(message: types.Message) -> Coroutine:
    await Question.question.set()
    return await bot.send_message(
        message.from_user.id,
        "Введите сообщение/вопрос/предложения для нашей команды тех. поддержки.",
        reply_markup=cancleButtons,
    )


async def process_question_quest(
    message: types.Message, state: FSMContext
) -> Coroutine:
    await message.forward(
        admin_chat,
    )
    await bot.send_message(
        message.from_user.id, "Ваше обращение создано, ответим в ближайшее время"
    )
    return await process_finish_state(message, state)


async def process_question_request(message: types.Message, state: FSMContext):
    try:
        if str(message.chat.id) == str(admin_chat):
            await bot.send_message(
                message.reply_to_message.forward_from.id,
                "Ответ на ваше обращение: \n\n" + message.text,
            )
    except:
        pass


def register_handlers_question(dp: Dispatcher) -> None:
    dp.register_message_handler(
        process_question, lambda m: m.text and m.text == "📩 Написать нам"
    )
    dp.register_message_handler(process_question_quest, state=Question.question)
    dp.register_message_handler(process_question_request)
