from pprint import pprint
from typing import Optional

from aiogram import Router
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION, LEAVE_TRANSITION
from aiogram.types import ChatMemberUpdated
from dependency_injector.wiring import inject, Provide

from src.containers import Container
from src.telegram.application.services.chat import TelegramChatService
from src.telegram.application.services.user import TelegramUserService
from src.telegram.domain.models.chat import TelegramChatCreate
from src.telegram.domain.models.user import TelegramUserCreate

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION or LEAVE_TRANSITION))
@inject
async def on_chat_member_update(
        event: ChatMemberUpdated,
        chat_service: TelegramChatService = Provide[Container.telegram.chat_service],
        user_service: TelegramUserService = Provide[Container.telegram.user_service],

):
    chat, _ = await chat_service.get_or_create(
        chat_id=event.chat.id,
        entity=TelegramChatCreate.model_validate(event.chat)
    )
    user, _ = await user_service.get_or_create(
        user_id=event.from_user.id,
        entity=TelegramUserCreate.model_validate(event.from_user)
    )
