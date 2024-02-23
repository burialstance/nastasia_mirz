import io
from typing import Literal

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException
from playwright.async_api import Browser
from starlette.responses import StreamingResponse

from src.containers import AppContainer

router = APIRouter()


@router.post('/install')
@inject
async def install_browser(
        browser_type: Literal['firefox', 'chromium'],
):
    raise HTTPException(500, 'NotImplemented')


@router.get('/{tab}/screenshot')
@inject
async def get_tab_screenshot(
        tab: int = 0,
        browser: Browser = Depends(Provide[AppContainer.browser.browser]),
):
    if tab > len(browser.contexts[0].pages):
        raise HTTPException(404, 'tab not found')

    screenshot = await browser.contexts[0].pages[tab].screenshot(type='png')
    return StreamingResponse(io.BytesIO(screenshot), media_type='/'.join(['image', 'png']))
