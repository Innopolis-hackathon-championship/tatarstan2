from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.admin_keyboards import kb_new_item
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
    fill_count = State()


@router_admin.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text='Чтобы добавить товар, нажмите на кнопку',
        reply_markup=kb_new_item.as_markup()
    )


@router_admin.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text='Отменять нечего. Вы вне машины состояний\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )


@router_admin.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text='Вы вышли из машины состояний\n\n'
             'Чтобы снова перейти к заполнению анкеты - '
             'отправьте команду /fillform'
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


@router_admin.message(StateFilter(FSMFillForm.fill_name))
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text='Введите стоиость товара')
    await state.set_state(FSMFillForm.fill_cost)


@router_admin.message(StateFilter(FSMFillForm.fill_cost), lambda x: x.text.isdigit())
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(cost=message.text)
    await message.answer(text='Введите количсетво товара')
    await state.set_state(FSMFillForm.fill_count)


@router_admin.message(StateFilter(FSMFillForm.fill_cost))
async def warning_not_age(message: Message):
    await message.answer(
        text='Цена введена некоректно, пожалуйста введите ее заново'
    )


@router_admin.message(StateFilter(FSMFillForm.fill_count), F.isdigit())
async def process_age_sent(message: Message, state: FSMContext):
    await state.update_data(count=message.text)
    await message.answer(text='Товар был добавлен')
    await state.clear()


@router_admin.message(StateFilter(FSMFillForm.fill_count))
async def warning_not_age(message: Message):
    await message.answer(
        text='Количество товара введено некоректно, пожалуйста повторите ввод'
    )
