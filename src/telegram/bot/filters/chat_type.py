from typing import Sequence, List
from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_types: str | Sequence[str]):
        self.chat_types = [chat_types] if isinstance(chat_types, str) else chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types
