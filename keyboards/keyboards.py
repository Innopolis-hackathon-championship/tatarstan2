from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

home_button = InlineKeyboardButton(
    text='На главную',
    callback_data='home_button_pressed'
)

make_an_order_button = InlineKeyboardButton(
    text='Меню',
    callback_data='make_an_order_button_pressed'
)

balance_button = InlineKeyboardButton(
    text='Баланс',
    callback_data='balance_button_pressed'
)

feedback_button = InlineKeyboardButton(
    text='Отзывы',
    callback_data='feedback_button_pressed'
)

leave_feedback_button = InlineKeyboardButton(
    text='Оставить отзыв',
    callback_data='leave_feedback_button_pressed'
)


get_feedback_button = InlineKeyboardButton(
    text='Читать отзывы',
    callback_data='get_feedback_button_pressed'
)


kb_main_builder = InlineKeyboardBuilder()
kb_main_builder.row(make_an_order_button, width=1)
kb_main_builder.row(*[balance_button, feedback_button], width=2)


kb_feedback_builder = InlineKeyboardBuilder()
kb_feedback_builder.row(*[leave_feedback_button, get_feedback_button], width=2)
kb_feedback_builder.row(home_button, width=1)

kb_balance_builder = InlineKeyboardBuilder()
kb_balance_builder.row(home_button, width=1)


def create_menu() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    # for(проходимся по бд с едой){
    #     if(число еды > 0){
    #         buttons.append(InlineKeyboardButton(кнопка))
    #     }
    # }

    kb_builder.row(*buttons)

    return kb_builder.as_markup()
