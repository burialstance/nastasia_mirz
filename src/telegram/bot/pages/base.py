from typing import Optional, List

from aiogram import types, Bot
from pydantic import BaseModel, Field
from aiogram.utils.text_decorations import html_decoration


class Page(BaseModel):
    title: Optional[str] = Field(None)
    icon: Optional[str] = Field(None)
    content: Optional[str] = Field(None)
    desc: Optional[str] = Field(None)

    reply_markup: Optional[types.InlineKeyboardMarkup] = Field(None)

    def build_text(self, disable_decoration: bool = False) -> str:
        rows: List[str] = []

        if self.title:
            title = self.title if disable_decoration else html_decoration.bold(self.title)
            rows.append(' '.join(filter(None, [self.icon, title])))

        if self.content:
            rows.extend(['', self.content])

        if self.desc:
            desc = self.desc if disable_decoration else html_decoration.italic(self.desc)
            rows.extend(['', desc])

        return '\n'.join(rows)

    @classmethod
    async def create(cls, **kwargs):
        raise NotImplementedError

    async def send(self, chat_id: int, bot: Bot, disable_decoration: bool = False) -> types.Message:
        return await bot.send_message(
            chat_id=chat_id,
            text=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )

    async def answer(self, message: types.Message, disable_decoration: bool = False) -> types.Message:
        return await message.answer(
            text=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )

    async def edit(self, message: types.Message, disable_decoration: bool = False) -> types.Message:
        return await message.edit_text(
            text=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )


class ImagePage(Page):
    image: bytes
    filename: Optional[str] = Field(None)

    async def send(self, chat_id: int, bot: Bot, disable_decoration: bool = False) -> types.Message:
        return await bot.send_photo(
            chat_id=chat_id,
            photo=types.BufferedInputFile(self.image, filename=self.filename),
            caption=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )

    async def answer(self, message: types.Message, disable_decoration: bool = False) -> types.Message:
        return await message.answer_photo(
            photo=types.BufferedInputFile(self.image, filename=self.filename),
            caption=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )

    async def edit(self, message: types.Message, disable_decoration: bool = False) -> types.Message:
        return await message.edit_caption(
            caption=self.build_text(disable_decoration=disable_decoration),
            reply_markup=self.reply_markup
        )
