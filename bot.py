import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from core.config import Config, load_config
from handlers import user_handlers, admin_handlers
from lexicon.lexicon_ru import LEXICON_MENU_COMMANDS_RU

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    dp.include_router(user_handlers.router_user)
    # dp.include_router(_handlers.router_admin)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


async def set_main_menu(bot: Bot):
    print(LEXICON_MENU_COMMANDS_RU.items())
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_MENU_COMMANDS_RU.items()
    ]
    await bot.set_my_commands(main_menu_commands)


if __name__ == '__main__':
    asyncio.run(main())
