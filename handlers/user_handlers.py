from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from database.interaction_with_db import get_balance, get_product_name, get_last_10_messages, add_message, get_korz
from database.interaction_with_db import del_korz, insert_into_korz
from filters.get_access import IsAllowed
from keyboards.user_keyboards import kb_main_builder, kb_feedback_builder
from lexicon.lexicon_ru import LEXICON_RU

router_user: Router = Router()
router_user.message.filter(IsAllowed())


@router_user.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())


@router_user.callback_query(F.data == 'make_an_order_button_pressed')
async def menu_button_pressed(callback: CallbackQuery):
    # ../database/res_menu.jpg
    photo = FSInputFile('../database/res_menu.jpg')
    await callback.message.answer_photo(photo, caption="Актуальное меню. Для заказа напишите /buy arg,\n"
                                                       "где arg - это номер товара.")


@router_user.callback_query(F.data == 'feedback_button_pressed')
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text='Оставьте отзыв о заказе или почитайте мнение других',
                                     reply_markup=kb_feedback_builder.as_markup())


@router_user.message(Command('balance'))
async def process_balance_command(message: Message):
    balance = await get_balance(message.from_user.id)
    await message.answer(text=f"Ваш текущий баланс: {balance[0]}")


@router_user.message(Command('buy'))
async def process_balance_command(message: Message):
    arguments = message.text.split()
    res = await get_product_name(arguments[1])
    print(res)
    if res[0]:
        await message.answer(text=f"{res[1]} добавлен в корзину")
        await insert_into_korz(message.from_user.id, res[1])
    else:
        await message.answer(text=res[1])



@router_user.callback_query(F.data == 'home_button_pressed')
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())


@router_user.callback_query(F.data == 'leave_feedback_button_pressed')
async def process_message(callback: CallbackQuery):
    await add_message(callback.message.text)
    await callback.message.answer(f"Ваш отзыв был сохранен")


@router_user.callback_query(F.data == 'get_feedback_button_pressed')
async def cmd_last_10_messages(callback: CallbackQuery):
    messages = await get_last_10_messages()
    await callback.message.edit_text(text='\n'.join(messages))
