from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


add_item_button = InlineKeyboardButton(
    text='Добавить товар',
    callback_data='add_item_button_pressed'
)

confirm_button = InlineKeyboardButton(
    text='Подтвердить✅',
    callback_data='confirmed'
)

cancel_button = InlineKeyboardButton(
    text='Сбросить❌',
    callback_data='canceled'
)

kb_admin_main = InlineKeyboardBuilder()
kb_admin_main.row(add_item_button)


kb_confirmation = InlineKeyboardBuilder()
kb_confirmation.row(*[confirm_button, cancel_button], width=2)
