from typing import Optional, Literal

from dependency_injector import containers, providers
from playwright.async_api import async_playwright, PlaywrightContextManager, BrowserType, Browser

from src.browser.services.auth import AuthenticateService
from src.settings import AccountSettings


async def warmup_browser(
        browser: Browser,
        email: str,
        password: str
):
    page = await browser.new_page()
    auth = AuthenticateService(page=page)
    await auth.login(email=email, password=password)


async def start_browser(
        browser_type: Literal['firefox', 'chromium', 'webkit'] = 'firefox',
        headless: bool = False
):
    async with async_playwright() as playwright:
        browser: Optional[BrowserType] = getattr(playwright, browser_type, None)
        if not isinstance(browser, BrowserType):
            raise Exception(f'unknown browser_type={browser_type}')

        instance: Browser = await browser.launch(headless=headless)
        yield instance


class BrowserContainer(containers.DeclarativeContainer):
    # wiring_config = containers.WiringConfiguration(modules=[])
    browser = providers.Resource(start_browser)

    account_settings = providers.Singleton(AccountSettings)
    warmup_browser_task = providers.Resource(
        warmup_browser,
        browser=browser,
        email=account_settings.provided.EMAIL,
        password=account_settings.provided.PASSWORD
    )
