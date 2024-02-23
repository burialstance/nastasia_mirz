from typing import Optional

from src.telegram.bot.misc import icons
from .base import Page


class WarningPage(Page):
    icon: Optional[str] = icons.warning
    content: Optional[str] = 'Warning'


class ForbiddenPage(Page):
    icon: Optional[str] = icons.forbidden
    content: Optional[str] = 'Forbidden'
