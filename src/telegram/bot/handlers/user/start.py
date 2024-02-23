from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.text_decorations import html_decoration

from src.telegram.bot.pages import Page

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message):
    await message.answer(
        Page(
            title='Session service',
            desc='Part of {} services'.format(
                html_decoration.link('Cryptobox Parser', 'https://t.me/binance_box_channel')
            )
        ).build_text(),
        disable_web_page_preview=True,
    )
