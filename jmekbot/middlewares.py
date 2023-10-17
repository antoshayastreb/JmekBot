import random
from loguru import logger
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

class LoggingMiddleware(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        logger.debug(f"Received message in chat {message.chat.id} from user {message.from_user.id}: {message.text}")