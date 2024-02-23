from dependency_injector import containers, providers

from src.admin.containers import AdminContainer
from src.db.containers import DatabaseContainer
from src.telegram.containers import TelegramContainer
from src.browser.containers import BrowserContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        'src.api.v1.browser'

    ])

    app = providers.Dependency()

    db = providers.Container(DatabaseContainer)
    admin = providers.Container(AdminContainer, app=app, db=db.database)
    telegram = providers.Container(TelegramContainer)
    browser = providers.Container(BrowserContainer)
