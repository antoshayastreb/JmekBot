import logging
import random
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from jmekbot import responses
from jmekbot.services.anekdot import AnekdotRuScraper

router = Router(name='anekdots')

@router.message(Command('anekdot'))
async def anekdot(message: Message):
    try:
        result = await AnekdotRuScraper.get_anekdots()
        if result:
            await message.reply(random.choice(result))
        else:
            await message.reply(random.choice(responses.AnekdotsEmpty))
    except Exception as ex:
        logging.error(f'Error on anekdot command: {ex}')
        message.reply(random.choice(responses.Error))