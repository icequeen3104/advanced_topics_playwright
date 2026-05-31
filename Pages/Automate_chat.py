from Pages.base import BasePage
from playwright.sync_api import expect


class AutomateChatPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page.chat = self.page.locator("//div[@jsname='hSRGPd']/following-sibling::div[text()='Chat']")
        self.page.outer_iframe = self.page.frame_locator("#gtn-roster-iframe-id")
        self.page.person_to_chat = self.page.outer_iframe.locator("//span[text()=' Suggested contact, ']/preceding-sibling::span[text()='Parna Bhattacharya']")
        self.page.message = self.page.person_to_chat.locator("//div[@jsname='AAsgyb']//child::div[text()='History is on']")

    def goto_chat(self):
        self.chat.click()
        self.page.wait_for_url("https://mail.google.com/mail/u/0/?tab=rm&ogbl#chat/home")

    def to_chat_with(self):
        self.person_to_chat.click()
        self.page.wait_for_url("https://mail.google.com/mail/u/0/?tab=rm&ogbl#chat/dm/--Z1ayAAAAE")

    def type_your_message(self, message):
        expect(self.message).to_be_visible(timeout=50000)
        self.message.type(message)

