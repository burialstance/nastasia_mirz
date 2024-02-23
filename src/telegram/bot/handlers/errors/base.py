from aiogram import Router, Bot
from aiogram import types
from aiogram.filters.exception import ExceptionTypeFilter

from src.telegram.bot.exceptions.base import BaseAppException
from src.telegram.bot.misc import icons
from src.telegram.bot.pages import WarningPage

router = Router()


@router.error(ExceptionTypeFilter(BaseAppException))
async def on_base_app_exception(error: types.ErrorEvent):
    exception: BaseAppException = getattr(error, 'exception')

    warning_page = WarningPage(
        icon=icons.red_excl,
        title=exception.title,
        content=exception.content,
        desc=exception.desc
    )

    event = error.update.event
    match type(event):
        case types.Message:
            message = event
            await message.answer(text=warning_page.build_text())
        case types.CallbackQuery:
            callback = event
            await callback.answer()
            await callback.message.answer(warning_page.build_text())
        case _:
            await event.bot.send_message(error.update.message.from_user.id, warning_page.build_text())
