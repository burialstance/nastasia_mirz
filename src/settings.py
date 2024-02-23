import logging
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

logging.basicConfig(level=logging.INFO)

SRC_DIR = Path(__file__).parent
ENV_FILE = SRC_DIR.parent.joinpath('.env')


class _BaseEnvSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        extra='ignore'
    )


class AppSettings(_BaseEnvSettings):
    DEBUG: bool = True
    TITLE: str = 'Nastasia service'
    VERSION: str = '0.0.1'
    DESC: str = ''


class TelegramSettings(_BaseEnvSettings):
    TOKEN: str

    model_config = SettingsConfigDict(
        env_prefix='TELEGRAM_'
    )


class DatabaseSettings(_BaseEnvSettings):
    model_config = SettingsConfigDict(env_prefix='DB_')

    URL: str = f'sqlite+aiosqlite:///{SRC_DIR.parent.joinpath("db.sqlite")}'
    ECHO: bool = True


class AccountSettings(_BaseEnvSettings):
    model_config = SettingsConfigDict(env_prefix='ACCOUNT_')

    EMAIL: str
    PASSWORD: str


app = AppSettings(_env_prefix='APP_')
