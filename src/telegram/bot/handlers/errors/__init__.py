from aiogram import Dispatcher, Router

from . import throttling
from . import base

errors_router = Router()

errors_router.include_router(throttling.router)
errors_router.include_router(base.router)  # must be last routed


def register(dp: Dispatcher):
    dp.include_router(errors_router)
