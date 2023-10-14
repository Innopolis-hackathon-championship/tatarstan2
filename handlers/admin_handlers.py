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
                    price int)""")
    db.commit()
    db.close()


class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_cost = State()
    fill_break = State()


new_name = ''
new_cost = 0


@router_admin.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text='Выберите требующееся действие',
        reply_markup=kb_admin_main.as_markup()
    )


@router_admin.callback_query(F.data == 'add_item_button_pressed', StateFilter(default_state))
async def add_new_item(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Введите название товара')
    await state.set_state(FSMFillForm.fill_name)


@router_admin.message(StateFilter(FSMFillForm.fill_name))
async def process_name_sent(message: Message, state: FSMContext):
    global new_name
    new_name = message.text
    await state.update_data(name=new_name)
    await message.answer(text='Введите стоимость товара')
    await state.set_state(FSMFillForm.fill_cost)


@router_admin.message(StateFilter(FSMFillForm.fill_cost))
async def confirmation_of_adding(message: Message, state: FSMContext):
    global new_cost
    new_cost = int(message.text)
    await state.update_data(cost=str(new_cost))
    await message.answer(text='Вы уверены, что хотите добавить это товар?', reply_markup=kb_confirmation.as_markup())
    await state.set_state(FSMFillForm.fill_break)


@router_admin.callback_query(F.data == 'confirmed', StateFilter(FSMFillForm.fill_break))
async def append_item_(callback: CallbackQuery, state: FSMContext):
    print('Sucsess')
    global new_name, new_cost
    await callback.message.edit_text(text=f'Товар был добавлен')
    c.execute("INSERT INTO products VALUES (?, ?)", (new_name, new_cost))
    await state.clear()


@router_admin.callback_query(F.data == 'canceled', StateFilter(FSMFillForm.fill_break))
async def skip_item(callback: CallbackQuery, state: FSMContext):
    print('fsaf')
    await callback.message.edit_text(text=f'Товар не был добавлен')
    await state.clear()
