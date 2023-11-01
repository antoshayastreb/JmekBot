from aiogram.filters import BaseFilter
from aiogram.types import Message

class ReplyFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.reply_to_message:
            return True
        return False