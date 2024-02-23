import logging

from loguru import logger

from playwright.async_api import Page

from src.browser.pages.base import BasePage
from src.browser.utils.onetrust import OneTrustBanner


class AuthenticatePage(BasePage):
    AUTH_URL: str = 'https://visa.vfsglobal.com/rus/ru/fra/login'

    def __init__(self, page: Page):
        super().__init__(page=page)

        self.email_field = self.page.locator('//*[@id="mat-input-0"]')
        self.password_field = self.page.locator('//*[@id="mat-input-1"]')
        self.login_btn = self.page.locator(
            '//html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button'
        )

        self.captcha_container = self.page.locator(
            'iframe[title=\"Widget containing a Cloudflare security challenge\"]'
        )

    async def pass_cloudflare(self):
        await self.page.frame_locator(
            'iframe[title=\"Widget containing a Cloudflare security challenge\"]'
        ).get_by_text('Verify you are human').click()

    async def login(
            self,
            email: str,
            password: str
    ):
        logger.info(f'navigate to {self.AUTH_URL}')
        await self.goto(self.AUTH_URL)
        await OneTrustBanner(self.page).close_banner()

        logger.info('[cloudflare] wait for element')
        await self.captcha_container.wait_for(timeout=60_000, state='visible')
        logger.info('[cloudflare] try to approve')
        await self.pass_cloudflare()
        logger.success('[cloudflare] they trust us :)')

        await self.email_field.type(email)
        await self.password_field.type(password)

        async with self.page.expect_event('response') as event:
            await self.login_btn.click()
            print(type(await event.value), await event.value)
        # await self.page.wait_for_url('**/dashboard')
        logger.success(f'success logged as {email}')
