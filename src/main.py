from contextlib import asynccontextmanager

from loguru_logging_intercept import setup_loguru_logging_intercept
from fastapi import FastAPI

from src import settings, api
from src.containers import AppContainer


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    container: AppContainer = getattr(app.state, 'container')

    await container.db().database().create_database()
    container.admin().init_resources()
    await container.telegram().init_resources()
    # await container.browser().init_resources()

    yield
    await container.telegram().shutdown_resources()
    # await container.browser().shutdown_resources()


def create_app() -> FastAPI:
    setup_loguru_logging_intercept()
    _app = FastAPI(
        debug=settings.app.DEBUG,
        title=settings.app.TITLE,
        version=settings.app.VERSION,
        description=settings.app.DESC,
        lifespan=app_lifespan
    )
    _app.state.container = AppContainer(app=_app)

    api.register(_app)
    return _app


app = create_app()
