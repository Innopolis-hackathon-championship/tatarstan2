from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.admin_keyboards import kb_admin_main, kb_confirmation
import sqlite3

# from keyboards.keyboards import
# from lexicon.lexicon_ru import LEXICON_RU, BUTTONS

router_admin: Router = Router()

db = sqlite3.connect('users_id.sqlite')

c = db.cursor()


def create_menu():
    db = sqlite3.connect('menu.sqlite')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE products (
                    product_id integer,
                    name text,
                    price int,
                    number int)""")
    db.commit()
    db.close()


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_cost = State()
    fill_break = State()


@router_admin.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите требующееся действие',
        reply_markup=kb_admin_main.as_markup()
    )


@router_admin.callback_query(F.data == 'add_item_button_pressed', StateFilter(default_state))
async def feedback_button_pressed(callback: CallbackQuery, message: Message, state: FSMContext):
    await message.answer(text='Введите название товара')
    await state.set_state(FSMFillForm.fill_name)


@router_admin.message(StateFilter(FSMFillForm.fill_name))
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Введите стоимость товара')
    await state.set_state(FSMFillForm.fill_cost)


@router_admin.message(StateFilter(FSMFillForm.fill_cost))
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await message.answer(text='Введите количество товара')
    await state.set_state(FSMFillForm.fill_count) # !!!!!!!!!!!!!!!


@router_admin.message(StateFilter(FSMFillForm.fill_count))
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(count=message.text)
    await message.answer(text='Вы уверены')
    await state.set_state(FSMFillForm.fill_break)
