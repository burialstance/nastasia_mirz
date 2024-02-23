from dependency_injector import containers, providers
from fastapi import FastAPI
from sqladmin import Admin

from src.admin.views import register_admin_views
from src.db.database import Database


class AdminContainer(containers.DeclarativeContainer):
    app = providers.Dependency(FastAPI)
    db = providers.Dependency(Database)

    admin = providers.Singleton(
        Admin,
        title='Admin',
        app=app.provided,
        engine=db.provided.engine
    )
    register_views = providers.Resource(register_admin_views, admin=admin)
