# class Input:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# search = Input('Поиск', 'input#search')
#
# print(search.text + ':', search.loc)
#
# class Button:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# home = Button('Домой', 'button#home')
# print(home.text + ':', home.loc)
#
# class Title:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# title = Title('Заголовок', 'title#title')
# print(title.text + ':', title.loc)
#
# class Link:
#
#     def __init__(self, text, loc):
#         self.text = text
#         self.loc = loc
#
# link = Link('Ссылка', 'link#link')
# print(link.text + ':', link.loc)

from task_9_checks import Checks

class Input(Checks):

    def __init__(self,text, loc):
        super().__init__(loc)
        self.text = text

search = Input('Поиск', 'input#search')
print(search.check_text())

class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

home = Button('Домой', 'button#home')
print(home.check_text())

class Title(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

title = Title('Заголовок', 'title#title')
print(title.check_text())

class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text

link = Link('Ссылка', 'link#link')
print(link.check_text())

