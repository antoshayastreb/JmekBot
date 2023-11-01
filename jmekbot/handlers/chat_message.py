from aiogram import Router
from aiogram import F
from aiogram.filters import and_f, or_f, invert_f
from aiogram.types import Message

from jmekbot.middlewares.random import RandomMiddleware

router = Router()
router.message.middleware(RandomMiddleware(0.1))

@router.message(
    and_f(
        (F.text.strip().len() < 30),
        # (F.text.lower() != 'пизда'),
        # invert_f(F.text.contains('пизда')),
        or_f(
            (F.text.strip().lower() == 'да'),
            #F.text.endswith('да')
            (F.text.func(lambda text: text.strip().split()[-1].lower() == "да"))
        )
    )
)
async def ends_with_da(message: Message):
    await message.reply('Пизда')