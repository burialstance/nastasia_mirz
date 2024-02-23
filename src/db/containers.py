from dependency_injector import providers, containers

from src.settings import DatabaseSettings
from src.db.database import Database


class DatabaseContainer(containers.DeclarativeContainer):
    settings = providers.Singleton(DatabaseSettings)
    database = providers.Singleton(
        Database,
        db_url=settings.provided.URL,
        echo=settings.provided.ECHO
    )
