from database.interaction_with_db import validation
from aiogram.filters import Filter
from aiogram.types import Message


class IsAllowed(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, message: Message) -> bool:
        return await validation(message.from_user.id)
