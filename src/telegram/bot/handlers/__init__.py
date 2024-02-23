from aiogram import Dispatcher, Router

from . import user
from . import errors
# from . import chats

root_router = Router()
root_router.include_router(errors.errors_router)

root_router.include_router(user.router)
# root_router.include_router(chats.router)


def register(dp: Dispatcher):
    dp.include_router(root_router)
