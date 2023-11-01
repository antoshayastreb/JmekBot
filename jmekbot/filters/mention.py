from aiogram.filters import BaseFilter
from aiogram.types import Message

class MentionFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.entities:
            return any(entity.type == "mention" for entity in message.entities)
        return False