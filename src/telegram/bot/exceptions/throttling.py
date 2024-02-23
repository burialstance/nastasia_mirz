from src.telegram.bot.exceptions.base import BaseAppException


class ThrottlingException(BaseAppException):
    title = 'Dont spam'
    desc = 'can u be slowest?'
