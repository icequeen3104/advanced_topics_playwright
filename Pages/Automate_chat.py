from Pages.base import BasePage

class AutomateChatPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.chat = page.locator("//div[@jsname='hSRGPd']/following-sibling::div[text()='Chat']")
        self.iframe = page.frame_locator("#gtn-roster-iframe-id")
        self.person_to_chat = iframe.locator("//span[text()=' Suggested contact, ']/preceding-sibling::span[text()='Parna Bhattacharya']")
        self.message = person_to_chat.locator("//div[@jsname='AAsgyb']//child::div[text()='History is on']")

    def goto_chat(self):
        self.chat.click()
        self.page.wait_for_url("https://mail.google.com/mail/u/0/?tab=rm&ogbl#chat/home")

    def to_chat_with(self):
        self.person_to_chat.click()
        self.page.wait_for_url("https://mail.google.com/mail/u/0/?tab=rm&ogbl#chat/dm/--Z1ayAAAAE")

    def type_your_message(self, message):
        self.message.type(message)

