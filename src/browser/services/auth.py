from playwright.async_api import Page

from src.browser.pages.auth import AuthenticatePage


class AuthenticateService:
    def __init__(self, page: Page):
        self.page = page
        self.controller = AuthenticatePage(self.page)

    async def login(
            self,
            email: str,
            password: str
    ):
        await self.controller.login(
            email=email,
            password=password
        )
