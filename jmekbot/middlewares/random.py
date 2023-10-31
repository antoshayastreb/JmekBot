from typing import Any, Awaitable, Callable, Dict
import logging
import random
from aiogram import BaseMiddleware
from aiogram.types import Message

class RandomMiddleware(BaseMiddleware):
    '''Случайное срабатывание обработчика'''
    def __init__(self, chance: float = 0.4) -> None:
        self.random_chance = chance

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        roll = random.random()
        logging.debug(f'Chance of handling was {roll}')
        if roll < self.random_chance:
            return await handler(event, data)