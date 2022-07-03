from aiogram import Dispatcher, types
from keyboards.inline_keyboards.admins import admin_panel_keyboard
from database.UserManager import getUsers


async def process_admin_command(message: types.Message) -> None:
    """This function is logic for the /admin command

    :param message:
    """
    admins = getUsers(is_admins=True)

    if message.from_user.id in admins:
        await message.answer(
            "Открыл <b>панель администратора</b>", reply_markup=admin_panel_keyboard
        )
    else:
        await message.answer(
            "Отказано в доступе к команде /admin , у вас нет прав администратора"
        )


def register_handlers_admin(dp: Dispatcher) -> None:
    """This function registers handlers for the /admin command

    :param: dp
    """

    dp.register_message_handler(process_admin_command, commands=["admin"])
