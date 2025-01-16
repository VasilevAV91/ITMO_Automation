# class Page:
#
#     def __init__(self, url):
#         self.url = url
#
#     def get(self):
#         print(self.url)
#
# home = Page('https://cbr.ru/')
# home.get()


class Soda:

    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print('Обычная газировка')

drink1 = Soda('')
drink2 = Soda('Вишня')

drink1.show_my_drink()
drink2.show_my_drink()
