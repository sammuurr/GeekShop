from typing import Coroutine

from aiogram import Dispatcher, types
from config import bot


async def process_about_me(message: types.Message) -> Coroutine:
    await bot.send_message(
        message.from_user.id,
        "<b>Приветствуем</b> вас в пространстве IT технологий!"
        "Мы команда профессиональных программистов  💻<b>Geek Shop</b>💻\n\n"
        "<i>Если вам нужно:</i>\n"
        "☑️Разработка бота на Python\n"
        "☑️Доработка скрипта на Python, PHP, JS, Swift;\n"
        "☑️Разработка парсеров;\n"
        "☑️Автоматизация бизнеса;\n"
        "☑️Разработка приложения для бизнеса.\n\n"
        "                       <b><i>Вы по адресу!</i></b>\n\n"
        "<i>Потому что мы:</i>\n"
        "✔️Выведем ваш бизнес на качественно новый уровень;\n"
        "✔️Найдем решение вашего вопроса;\n"
        "✔️Поможем с настройкой и автоматизацией новых систем;\n"
        "✔️Возьмем на аутсорсинг;\n"
        "✔️Освободим ваше время и избавим от рутины.\n",
    )
    await message.answer(
        "Наши ссылки: \n\n"
        "Телеграмм канал - <b><i><a href='https://t.me/+anaOpsr-QTA3ZWUy'>ссылка</a></i></b>\n"
        "Канал с отзывами - <b><i><a href='https://t.me/+195G2W6NzpZmZGEy'>ссылка</a></i></b>\n"
        "Канал с нашими работами - <b><i><a href='https://t.me/+9NmdZIoGfZ5mNjQy'>ссылка</a></i></b>\n",
        disable_web_page_preview=True,
    )


def register_handlers_about_me(dp: Dispatcher) -> None:
    dp.register_message_handler(
        process_about_me, lambda m: m.text and m.text == "❔ О нас"
    )
