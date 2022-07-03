from aiogram import Dispatcher, types

from config import bot
from database.UserManager import createUser
from keyboards.reply_keyboards.main_menu import main_menu_keyboards


async def process_start_command(message: types.Message) -> None:
    """This function is logic for the /start command handler

    :param: message
    """
    createUser(message.from_user.id, message.from_user.full_name)
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
        reply_markup=main_menu_keyboards,
    )


def register_handlers_start(dp: Dispatcher) -> None:
    """This function registers handlers to handle /start command"""

    dp.register_message_handler(process_start_command, commands=["start"])
