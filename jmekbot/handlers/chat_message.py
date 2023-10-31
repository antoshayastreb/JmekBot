from aiogram import Router
from aiogram import F
from aiogram.types import Message

from jmekbot.middlewares.random import RandomMiddleware

router = Router()
router.message.middleware(RandomMiddleware())

@router.message(F.text.len() < 30)
@router.message(F.text.lower() == 'да')
@router.message(F.text.endswith('да') & (F.text.lower() != 'пизда') & F.text.lower().endswith('пизда'))
async def ends_with_da(message: Message):
    await message.reply('Пизда')