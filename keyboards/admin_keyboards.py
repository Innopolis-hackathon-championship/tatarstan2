from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


new_button = InlineKeyboardButton(
    text='Добавить товар',
    callback_data='new_button_pressed'
)

restart_button = InlineKeyboardButton(
    text='Сбросить',
    callback_data='restart_button_pressed'
)

kb_new_item = InlineKeyboardBuilder()
kb_new_item.row(*[new_button, restart_button], width=2)
