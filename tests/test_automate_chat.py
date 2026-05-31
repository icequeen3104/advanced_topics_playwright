from Pages.Automate_chat import AutomateChatPage

def test_Validate_Chat_Automation(page):
    page.goto("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
    breakpoint()
    ac = AutomateChatPage(page)
    ac.goto_chat()
    ac.to_chat_with()
    ac.type_your_message('hello!!')
