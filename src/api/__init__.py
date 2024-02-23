from fastapi import APIRouter, FastAPI

from . import v1, healthcheck

router = APIRouter()

router.include_router(healthcheck.router, prefix='/healthcheck')
router.include_router(v1.router, prefix='/v1')


def register(app: FastAPI):
    app.include_router(router, prefix='/api')
