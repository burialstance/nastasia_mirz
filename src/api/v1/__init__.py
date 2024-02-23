from fastapi import APIRouter, FastAPI

from . import browser

router = APIRouter()
router.include_router(browser.router, prefix='/browser')
