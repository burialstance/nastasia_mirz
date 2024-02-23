from aiogram import Bot, types

from . import icons


HELP_CMD = 'help'

BOT_COMMANDS = {
    HELP_CMD: ' '.join([icons.white_quest, 'Help'])
}


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[types.BotCommand(command=c, description=d) for c, d in BOT_COMMANDS.items()],
        scope=types.BotCommandScopeAllPrivateChats()
    )
