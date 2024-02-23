from aiogram import Router, types, filters


from src.telegram.bot.filters.chat_type import ChatTypeFilter

from . import start
from . import help

router = Router()
router.message.filter(ChatTypeFilter('private'))

router.include_router(start.router)
router.include_router(help.router)
