from aiogram import Router, Bot
from aiogram import types
from aiogram.filters.exception import ExceptionTypeFilter

from src.telegram.bot.exceptions.throttling import ThrottlingException
from src.telegram.bot.pages import WarningPage

router = Router()


@router.error(ExceptionTypeFilter(ThrottlingException))
async def on_throttling_exception(error: types.ErrorEvent):
    warning_page = WarningPage.model_validate(error.exception, from_attributes=True)

    event = error.update.event
    match type(event):
        case types.Message:
            await event.answer(text=warning_page.build_text())
        case types.CallbackQuery:
            await event.answer(warning_page.build_text(disable_decoration=True), show_alert=True)
        case _:
            await event.bot.send_message(error.update.message.from_user.id, warning_page.build_text())
