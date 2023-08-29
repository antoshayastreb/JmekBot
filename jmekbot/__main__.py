from aiogram import Dispatcher
from aiogram.utils import executor
from jmekbot.loader import dp
from loguru import logger

from jmekbot.commands import set_default_commands

async def startup(dp: Dispatcher) -> None:
    await set_default_commands(dp)
    logger.info('bot started')

async def shutdown(dp: Dispatcher) -> None:
    logger.info('bot finished')

if __name__ == '__main__':
    logger.add(
        'logs/debug.log',
        level='DEBUG',
        format='{time} | {level} | {module}:{function}:{line} | {message}',
        rotation='30 KB',
        compression='zip',
    )

    executor.start_polling(dp, skip_updates=True, on_startup=startup, on_shutdown=shutdown)