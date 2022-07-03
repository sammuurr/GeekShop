import asyncio
from threading import Thread

from aiogram.utils import executor

from config import dp, bot, admin_chat
from handlers.command_handlers.start import register_handlers_start
from handlers.command_handlers.admin import register_handlers_admin
from handlers.inline_handlers.admin_menu.admin_menu_admins import (
    register_handlers_admin_menu_admins,
)
from handlers.text_handlers.backButton import register_handlers_back_button
from handlers.text_handlers.main_menu.about_me import register_handlers_about_me
from handlers.text_handlers.main_menu.buyBot.buy_bot import register_handlers_buy_bot
from handlers.text_handlers.main_menu.buyBot.deadlines import (
    register_handlers_buy_bot_deadline,
)
from handlers.text_handlers.main_menu.buyBot.platform import (
    register_handlers_buy_bot_platform,
)
from handlers.text_handlers.main_menu.buyBot.sum import register_handlers_buy_bot_sum
from handlers.text_handlers.main_menu.buyBot.task import register_handlers_buy_bot_task
from handlers.text_handlers.main_menu.buy_service.buy_bot import register_handlers_buy_service
from handlers.text_handlers.main_menu.buy_service.deadlines import register_handlers_buy_service_deadline
from handlers.text_handlers.main_menu.buy_service.platform import register_handlers_buy_service_platform
from handlers.text_handlers.main_menu.buy_service.sum import register_handlers_buy_service_sum
from handlers.text_handlers.main_menu.buy_service.task import register_handlers_buy_service_task
from handlers.text_handlers.main_menu.question import register_handlers_question
from handlers.text_handlers.main_menu.task_bot import register_handlers_task_bot

# command handlers


Thread(target=register_handlers_start, args=(dp,)).start()
Thread(target=register_handlers_admin, args=(dp,)).start()

# text handlers
Thread(target=register_handlers_back_button, args=(dp,)).start()
Thread(target=register_handlers_buy_bot, args=(dp,)).start()
Thread(target=register_handlers_buy_bot_platform, args=(dp,)).start()
Thread(target=register_handlers_buy_bot_deadline, args=(dp,)).start()
Thread(target=register_handlers_buy_bot_sum, args=(dp,)).start()
Thread(target=register_handlers_buy_bot_task, args=(dp,)).start()
Thread(target=register_handlers_task_bot, args=(dp,)).start()
Thread(target=register_handlers_about_me, args=(dp,)).start()

Thread(target=register_handlers_buy_service, args=(dp,)).start()
Thread(target=register_handlers_buy_service_deadline, args=(dp,)).start()
Thread(target=register_handlers_buy_service_platform, args=(dp,)).start()
Thread(target=register_handlers_buy_service_sum, args=(dp,)).start()
Thread(target=register_handlers_buy_service_task, args=(dp,)).start()

# inline button handlers
Thread(target=register_handlers_admin_menu_admins, args=(dp,)).start()

# Last handler
Thread(target=register_handlers_question, args=(dp,)).start()


def stop_bot():
    bot.send_message(
        admin_chat,
        "@all\n\nБот отключился, срочно поднимите бота"
    )


if __name__ == "__main__":
    executor.start_polling(dp)
    dp.stop_polling(stop_bot)