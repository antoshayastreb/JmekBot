import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

from jmekbot.middlewares import LoggingMiddleware

load_dotenv()

loop = asyncio.get_event_loop()
token = os.getenv("BOT_TOKEN")
bot = Bot(token=token, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot, loop=loop, storage=storage)

dp.middleware.setup(LoggingMiddleware())