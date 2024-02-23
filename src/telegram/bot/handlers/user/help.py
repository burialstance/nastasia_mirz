from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.text_decorations import html_decoration

from src.telegram.bot.misc.commands import HELP_CMD
from src.telegram.bot.pages import Page


router = Router()


@router.message(Command(commands=[HELP_CMD]))
async def on_help(message: types.Message):
    await message.answer(
        Page(
            title='Session service',
            desc='Part of {} services'.format(
                html_decoration.link('Cryptobox Parser', 'https://t.me/binance_box_channel')
            )
        ).build_text(),
        disable_web_page_preview=True,
    )
