from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, callback_query
# from keyboards.keyboards import
from lexicon.lexicon_ru import LEXICON_RU

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router_user: Router = Router()


@router_user.message(CommandStart())
async def begin(message: Message):
    markup = InlineKeyboardMarkup()
    but_1f = InlineKeyboardButton("Регистрация", callback_data="reg")
    markup.add(but_1f)
    await message.answer(text=LEXICON_RU['/start'], reply_markup=markup)


@router_user.callback_query_handler(lambda c: c.data == "reg")  # править
async def butt_erection(call: callback_query):
    markup = InlineKeyboardMarkup()
    # регистрация через телефон, потом валидация через куаркод
    # def some_func_1(qr-code):
    #       ... отправляет айдишник и телефон в базу данных, пока хз зачем - надо обсудить
    # если успешно
    menu_butt = InlineKeyboardButton("Меню", callback_data='show_menu')

    markup.add(menu_butt)
    await bot.send_message(call.message.chat.id, "Вы успешно зарегистрированы",
                           reply_markup=markup)


@router_user.callback_query_handler(lambda c: c.data == "show_menu")  # править
async def butt_erection(call: callback_query):
    markup = InlineKeyboardMarkup()
    # обращение к дб меню, вытаскивание оттуда данных:
    # priduct_sp = []
    # for i in db:
    #     id = db[0]
    #     name = db[1]
    #     price = db[2]
    #     number = db[3]
    #     функция из кода реналя
    #     product_sp.append([id, name, price, number))
    #     markup.add(InlineKeyboardButton(name, callback_data=str(id))) #надо подумать, как
    #     генерить функцию-ответ на запрос с любым id
    #
    # some_func_2(product_sp) # не забыть про то, что не всегда надо генерить новое меню - оптимизировать
    await bot.send_message(call.message.chat.id, "Вы успешно зарегистрированы",
                           reply_markup=markup)







@router_user.message(Command(commands=['feedback']))
async def process_help_command(message: Message):
    # leave_feedback(id, text)
    await message.answer(text=LEXICON_RU['/help'])




# @router_user.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text=LEXICON_RU['/start'])
#
#
# @router_user.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer(text=LEXICON_RU['/help'])
#
