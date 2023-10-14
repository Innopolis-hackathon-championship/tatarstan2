from aiogram.dispatcher.router import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router_other: Router = Router()


@router_other.message()
async def unregistered_users_handler(message: Message):
    await message.answer(text=LEXICON_RU['access_denied'])
