from aiogram.filters import Filter
from aiogram.types import Message
from environs import Env

env = Env()
env.read_env()
ADMIN_ID = env('ADMIN')


class IsAdmin(Filter):
    async def __call__(self, message: Message, *args, **kwargs):
        return message.from_user.id == ADMIN_ID
