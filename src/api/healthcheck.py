from fastapi import APIRouter

from src import settings

router = APIRouter()


@router.get('')
async def healthcheck():
    return settings.app.model_dump(include={
        'TITLE',
        'VERSION',
        'DESC'
    })
