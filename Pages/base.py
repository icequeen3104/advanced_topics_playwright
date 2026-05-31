from playwright.sync_api import Page
class BasePage:
    def __int__(self, page: Page):
        self.page = page