from typing import Coroutine

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from config import bot
from keyboards.reply_keyboards.back import cancleButtons
from states.newAdminState import NewAdmin
from states.deleteAdminState import DeleteAdmin
from database.UserManager import setUserForAdmin, getUsers


async def process_add_newadmin(message: types.CallbackQuery) -> Coroutine:
    await bot.send_message(
        message.from_user.id,
        "Введите <b>ID</b> админа, которого хотите добавить. Его можно получить тут @getmyid_bot",
        reply_markup=cancleButtons,
    )
    return await NewAdmin.adminId.set()


async def enter_add_newadmin(message: types.Message, state: FSMContext) -> Message:
    try:
        int(message.text)
    except Exception as exp:
        return await message.answer(
            "Введите <b>ID</b> админа. <b>ID</b> состоит из цифр"
        )
    isAdded = setUserForAdmin(message.text, admin=True)

    if isAdded:
        try:
            await state.finish()
            print(message.text)
            await bot.send_message(
                chat_id=int(message.text), text="✅ Вам добавили права администратора"
            )
            await bot.send_message(
                chat_id=int(message.text), text="Теперь вам доступно команда /admin"
            )
            await message.answer("✅ <b>Админ успешно добавлен</b> ✅")
            for admin in getUsers(is_admins=True)[0]:
                await bot.send_message(
                    admin,
                    f"<b><a href='{message.from_user.url}'>{message.from_user.full_name}</a></b> добавил нового администратора ID={message.text}",
                )
            return await message.answer(
                "Я отправил уведомление новому администратору и другим администраторам"
            )
        except Exception as exp:
            print(exp)
            await state.finish()
            await message.answer(
                "Данный пользователь не пользуется ботом, возможно вы ошиблись или попросите написать в боте команду "
                "/start "
            )
            for admin in getUsers(is_admins=True)[0]:
                await bot.send_message(
                    admin,
                    f"<b><a href='{message.from_user.url}'>{message.from_user.full_name}</a></b> пытался добавить нового администратора ID={message.text}",
                )

    else:
        await state.finish()
        return await message.answer(
            "Что-то пошло не так, я не смог добавить данного пользователя в администраторы"
        )


async def process_delete_admin(message: types.CallbackQuery) -> Coroutine:
    await bot.send_message(
        message.from_user.id,
        "Введите <b>ID</b> админа, которого хотите удалить. Его можно получить тут @getmyid_bot",
        reply_markup=cancleButtons,
    )
    return await DeleteAdmin.adminId.set()


async def enter_delete_admin(message: types.Message, state: FSMContext) -> Message:
    try:
        int(message.text)
    except:
        return await message.answer(
            "Введите <b>ID</b> админа. <b>ID</b> состоит из цифр"
        )
    isAdded = setUserForAdmin(message.text, admin=False)

    if isAdded:

        try:
            print(message.text)
            await bot.send_message(
                chat_id=message.text,
                text="❌ У вас больше нет прав администратора",
            )
            await bot.send_message(
                chat_id=message.text,
                text=f"<b><a href='{message.from_user.url}'>{message.from_user.full_name}</a></b> - удалил вас из "
                f"администраторов",
            )
            await message.answer("✅ <b>Админ успешно удален</b> ✅")
            for admin in getUsers(is_admins=True)[0]:
                await bot.send_message(
                    admin,
                    f"<b><a href='{message.from_user.url}'>{message.from_user.full_name}</a></b> удалил "
                    f"администратора ID={message.text}",
                )
            return await message.answer(
                "Я отправил уведомление бывшему администратору и другим администраторам"
            )
        except:
            await state.finish()
            return await message.answer("Данный пользователь не пользовался ботом")
    else:
        await state.finish()
        return await message.answer(
            "Что-то пошло не так, возможно данного администратора не существует"
        )


def register_handlers_admin_menu_admins(dp: Dispatcher) -> None:
    """This function registers handlers to handle text

    :param: dp
    """
    dp.register_callback_query_handler(
        process_add_newadmin, lambda c: c.data == "admin_add_admin"
    )
    dp.register_message_handler(enter_add_newadmin, state=NewAdmin.adminId)

    dp.register_callback_query_handler(
        process_delete_admin, lambda c: c.data == "admin_del_admin"
    )
    dp.register_message_handler(enter_delete_admin, state=DeleteAdmin.adminId)
