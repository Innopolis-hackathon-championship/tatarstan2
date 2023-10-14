from unittest.mock import call

from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from database.interaction_with_db import get_balance
from filters.get_access import IsAllowed
from keyboards.user_keyboards import kb_main_builder, kb_feedback_builder, kb_balance_builder
from lexicon.lexicon_ru import LEXICON_RU

router_user: Router = Router()


@router_user.message(CommandStart(), IsAllowed())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())


@router_user.callback_query(F.data == 'feedback_button_pressed')
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text='тут будет текст для фидбэка', reply_markup=kb_feedback_builder.as_markup())


@router_user.callback_query(F.data == 'balance_button_pressed', lambda call: True)
async def feedback_button_pressed(callback: CallbackQuery):
    bill = await get_balance(call.from_user.id)
    print(type(callback.message.from_user.id), call.from_user.id)
    await callback.message.edit_text(text=f'Ваш баланс составляет {bill}',
                                     reply_markup=kb_balance_builder.as_markup())


@router_user.callback_query(F.data == 'home_button_pressed')
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())

# @router_user.callback_query_handler(lambda c: c.data == "reg")  # править
# async def butt_erection(call: callback_query):
#     markup = InlineKeyboardMarkup()
#     # регистрация через телефон, потом валидация через куаркод
#     # def some_func_1(qr-code):
#     #       ... отправляет айдишник и телефон в базу данных, пока хз зачем - надо обсудить
#     # если успешно`
#     menu_butt = InlineKeyboardButton("Меню", callback_data='show_menu')
#
#     markup.add(menu_butt)
#     await bot.send_message(call.message.chat.id, "Вы успешно зарегистрированы",
#                            reply_markup=markup)
#
#
# @router_user.callback_query_handler(lambda c: c.data == "show_menu")  # править
# async def butt_erection(call: callback_query):
#     markup = InlineKeyboardMarkup()
#     # обращение к дб меню, вытаскивание оттуда данных:
#     # priduct_sp = []
#     # for i in db:
#     #     id = db[0]
#     #     name = db[1]
#     #     price = db[2]
#     #     number = db[3]
#     #     функция из кода реналя
#     #     product_sp.append([id, name, price, number))
#     #     markup.add(InlineKeyboardButton(name, callback_data=str(id))) #надо подумать, как
#     #     генерить функцию-ответ на запрос с любым id
#     #
#     # some_func_2(product_sp) # не забыть про то, что не всегда надо генерить новое меню - оптимизировать
#     await bot.send_message(call.message.chat.id, "Вы успешно зарегистрированы",
#                            reply_markup=markup)
#
#
#
#
# @router_user.message(Command(commands=['get_feedback']))
# async def process_help_command(message: Message):
#     # from interaction with db import get_feedback
#     # text = get_feedback()
#     # for i in text:
#     #     вывести i и две кнопки: вперёд и назад, надо понимать, что было сзади, и что будет спереди
#     await message.answer(text=LEXICON_RU['/feedback'])
#
#
#
#
# @router_user.message(Command(commands=['feedback']))
# async def process_help_command(message: Message):
#     text = message.get_args()
#     # from interaction with db import leave_feedback
#     # leave_feedback(text)
#     await message.answer(text=LEXICON_RU['/feedback'])
#
#
#
#
# # @router_user.message(CommandStart())
# # async def process_start_command(message: Message):
# #     await message.answer(text=LEXICON_RU['/start'])
# #
# #
# # @router_user.message(Command(commands=['help']))
# # async def process_help_command(message: Message):
# #     await message.answer(text=LEXICON_RU['/help'])
# #
