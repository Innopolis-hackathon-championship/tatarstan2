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
