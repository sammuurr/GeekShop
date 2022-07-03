from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

about_we = KeyboardButton("❔ О нас")
arenda_bot = KeyboardButton("📲 Арендовать бота")
shop_bot = KeyboardButton("💻 Заказать бота")
shop_usluga = KeyboardButton("🖥 Заказать другую услугу")
call_we = KeyboardButton("📩 Написать нам")

main_menu_keyboards = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_keyboards.row(arenda_bot)
main_menu_keyboards.row(shop_bot, shop_usluga)
main_menu_keyboards.row(about_we, call_we)
