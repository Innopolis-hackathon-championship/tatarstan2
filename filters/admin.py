from handlers.user_handlers import ADMIN_LIST
from aiogram.filters import Filter
from aiogram.types import Message


class IsAdmin(Filter):
    async def __call__(self, message: Message, *args, **kwargs):
        return message.from_user.id in ADMIN_LIST
