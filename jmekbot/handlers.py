import random
from aiogram import types

from jmekbot.loader import bot, dp
from jmekbot.responses import Responses, AnekdotsEmpty
from jmekbot.anekdot import AnekdotRuScraper

@dp.message_handler(commands=['anekdot'], commands_prefix='/')
async def handle_anekdot_command(message: types.Message) -> None:
    anekdots = await AnekdotRuScraper.get_anekdots()
    if anekdots:
        await message.reply(random.choice(anekdots))
    else:
        await message.reply(random.choice(AnekdotsEmpty))


@dp.message_handler(
    lambda message: message.chat.type == 'private',
    content_types=types.ContentType.TEXT
)
async def pm_text_handler(message: types.Message) -> None:
    """
    Обработчик личных сообщений
    """
    text = message.text.lower()
    if text in Responses:
        response = random.choice(Responses[text])
        await bot.send_message(message.chat.id, response)

@dp.message_handler(
    lambda message: message.chat.type == 'group',
    content_types=types.ContentType.TEXT
)
async def group_text_handler(message: types.Message) -> None:
    """
    Обработчик групповых сообщений
    """
    me = await bot.get_me()
    text = message.text.lower()
    text = text.replace(me.mention, '').strip()
    if text in Responses:
        response = random.choice(Responses[text])
        await message.reply(response)