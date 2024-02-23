from playwright.async_api import Page
from playwright._impl._errors import TimeoutError
from loguru import logger


class OneTrustBanner:
    BANNER_SDK_LOCATOR = 'id=onetrust-banner-sdk'
    ACCEPT_COOKIE_BTN_LOCATOR = 'id=onetrust-accept-btn-handler'
    REJECT_COOKIE_BTN_LOCATOR = 'id=onetrust-reject-all-handler'

    def __init__(self, page: Page, timeout: float = 30000.0):
        self.page = page
        self.timeout = timeout
        self.banner = self.page.locator(self.BANNER_SDK_LOCATOR)
        self.accept_cookie_btn = self.banner.locator(self.ACCEPT_COOKIE_BTN_LOCATOR)
        self.reject_cookie_btn = self.banner.locator(self.REJECT_COOKIE_BTN_LOCATOR)

    async def close_banner(self) -> bool:
        logger.info('[onetrust] wait for banner')
        try:
            await self.banner.wait_for(timeout=self.timeout, state='visible')
            await self.accept_cookie_btn.click()
            logger.success('[onetrust] accept-cookie btn clicked')
            return True
        except TimeoutError:
            logger.warning('[onetrust] popup-locator not found')
            return False
