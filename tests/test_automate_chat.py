from Pages.Automate_chat import AutomateChatPage

class test_Validate_Chat_Automation(page):
    page.goto("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    automate_chat = AutomateChatPage(page)
    automate_chat.goto_chat()
    automate_chat.to_chat_with()
    automate_chat.type_your_message('Hello!!')
