from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        if not self.page.url == url:
            await self.page.goto(url)
