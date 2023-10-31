import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from jmekbot.handlers import (
    anekdot,
    chat_message
)

from jmekbot.commands import (
    anekdot_command
)

def _get_log_level(env_value: any):
    if not isinstance(env_value, str):
        return logging.INFO
    env_value = env_value.lower()
    if env_value == 'debug':
        return logging.DEBUG
    elif env_value == 'warning':
        return logging.WARN
    else:
        return logging.INFO

async def _set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            anekdot_command
        ]
    )

async def _on_startup(dp: Dispatcher):
    dp.include_routers(
        anekdot.router,
        chat_message.router
    )

async def _configure_bot():
    token = os.getenv("BOT_TOKEN")
    log_level = _get_log_level(os.getenv("LOG_LEVEL"))
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s',
        stream=sys.stdout
    )
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    await _set_commands(bot)
    await _on_startup(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

def start_bot():
    asyncio.run(_configure_bot())