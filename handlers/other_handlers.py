from aiogram.dispatcher.router import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router_user: Router = Router()


@router_user.message()
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['access_denied'])
