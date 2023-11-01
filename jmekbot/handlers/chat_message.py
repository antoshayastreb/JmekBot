import random
from aiogram import Router
from aiogram import F
from aiogram.filters import and_f, or_f
from aiogram.types import Message

from jmekbot.filters.reply import ReplyFilter
from jmekbot.filters.mention import MentionFilter
from jmekbot.responses import Responses

router = Router()

@router.message(
    and_f(
        (F.text.strip().len() < 30),
        or_f(
            (F.text.strip().lower() == 'да'),
            (F.text.func(lambda text: text.strip().split()[-1].lower() == "да"))
        )
    )
)
async def da_reply(message: Message):
    if random.random() < 0.1:
        await message.reply('Пизда')

@router.message(
    and_f(
        F.text,
        or_f(
            ReplyFilter(),
            MentionFilter()
        )
    )
)
async def default_reply_to_message(message: Message):
    text = message.text.strip().lower()
    if text in Responses:
        response = random.choice(Responses[text])
        await message.reply(response)