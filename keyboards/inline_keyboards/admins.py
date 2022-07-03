from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# --- admin panel ---
add_admin_button = InlineKeyboardButton(
    "Добавить админа", callback_data="admin_add_admin"
)
del_admin_button = InlineKeyboardButton(
    "Удалить админа", callback_data="admin_del_admin"
)
back_button = InlineKeyboardButton("Назад", callback_data="admin_back")

admin_panel_keyboard = InlineKeyboardMarkup().add(add_admin_button, del_admin_button)
