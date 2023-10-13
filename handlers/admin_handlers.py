from aiogram import F
from aiogram.dispatcher.router import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
# from keyboards.keyboards import
# from lexicon.lexicon_ru import LEXICON_RU, BUTTONS

router_admin: Router = Router()


# @router_admin.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text=LEXICON_RU['/start'])
#
#
# @router_admin.message(Command(commands=['help']))
# async def process_help_command(message: Message):
#     await message.answer(text=LEXICON_RU['/help'])
