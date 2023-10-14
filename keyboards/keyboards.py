from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

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
    callback_data='live_feedback_button_pressed'
)


get_feedback_button = InlineKeyboardButton(
    text='Читать отзывы',
    callback_data='get_feedback_button_pressed'
)

kb_feedback = InlineKeyboardMarkup(
    inline_keyboard=[[leave_feedback_button],
                     [get_feedback_button]]
)

kb_main_builder = InlineKeyboardBuilder()
kb_main_builder.row(make_an_order_button)
kb_main_builder.row(balance_button, feedback_button)


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


def create_inline_kb(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=width)

    return kb_builder.as_markup()
