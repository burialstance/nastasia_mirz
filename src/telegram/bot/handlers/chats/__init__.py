from aiogram import Router, types

from src.telegram.infrastructure.bot.filters.chat_type import ChatTypeFilter
from . import events


router = Router()
router.message.filter(ChatTypeFilter(['channel', 'group', 'supergroup']))

router.include_router(events.router)