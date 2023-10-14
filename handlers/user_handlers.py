from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from database.interaction_with_db import get_balance, get_product_name
from filters.get_access import IsAllowed
from keyboards.user_keyboards import kb_main_builder, kb_feedback_builder, kb_balance_builder
from lexicon.lexicon_ru import LEXICON_RU

router_user: Router = Router()


@router_user.message(CommandStart(), IsAllowed())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())


@router_user.callback_query(F.data == 'feedback_button_pressed', IsAllowed())
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text='тут будет текст для фидбэка', reply_markup=kb_feedback_builder.as_markup())


@router_user.message(Command('balance'), IsAllowed())
async def process_balance_command(message: Message):
    balance = await get_balance(message.from_user.id)
    await message.answer(text=f"Ваш текущий баланс: {balance[0]}")


@router_user.message(Command('buy'), IsAllowed())
async def process_balance_command(message: Message):
    arguments = message.text.split()
    res = await get_product_name(arguments[1])
    print(res)
    if res[0]:
        await message.answer(text=f"{res[1]} добавлен в корзину")
    else:
        await message.answer(text=res[1])


@router_user.callback_query(F.data == 'home_button_pressed', IsAllowed())
async def feedback_button_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=kb_main_builder.as_markup())
