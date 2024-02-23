import asyncio

from dependency_injector import containers, providers

from aiogram import Bot, Dispatcher

from src.settings import TelegramSettings
from src.telegram.bot.misc.commands import set_bot_commands


async def pooling_task(dispatcher: Dispatcher, bot: Bot):
    await set_bot_commands(bot)

    # inject TelegramContainer intro handlers may cause circular imports
    from src.telegram.bot import handlers
    handlers.register(dispatcher)

    # pooling blocks loop func -> spawn new task
    asyncio.create_task(dispatcher.start_polling(
        bot,
        handle_signals=False
    ))
    yield
    await dispatcher.stop_polling()


class TelegramContainer(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(modules=[])

    settings = providers.Singleton(TelegramSettings)
    dispatcher = providers.Singleton(Dispatcher)
    bot = providers.Singleton(
        Bot,
        token=settings.provided.TOKEN,
        parse_mode='HTML'
    )

    start_pooling_task = providers.Resource(
        pooling_task,
        dispatcher=dispatcher,
        bot=bot
    )


