import os

from aiogram import Dispatcher
from aiogram.utils import executor
from jmekbot.loader import dp
from loguru import logger

from jmekbot.commands import set_default_commands
#from jmekbot.background import keep_alive

async def startup(dp: Dispatcher) -> None:
    await set_default_commands(dp)
    logger.info('bot started')

async def shutdown(dp: Dispatcher) -> None:
    logger.info('bot finished')

def _get_log_level(env_value: any):
    if not isinstance(env_value, str):
        return 'INFO'
    env_value = env_value.lower()
    if env_value == 'debug':
        return 'DEBUG'
    elif env_value == 'warning':
        return 'WARNING'
    else:
        return 'INFO'

if __name__ == '__main__':
    log_level = _get_log_level(os.getenv('LOG_LEVEL'))
    logger.add(
        'logs/debug.log',
        level=log_level,
        format='{time} | {level} | {module}:{function}:{line} | {message}',
        rotation='30 KB',
        compression='zip',
    )
    #keep_alive()
    executor.start_polling(dp, skip_updates=True, on_startup=startup, on_shutdown=shutdown)