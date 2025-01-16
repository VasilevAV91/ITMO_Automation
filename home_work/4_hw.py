# Задача 1 (Площадь и периметр прямоугольника)
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def rectangle_square(self):
        return self.width * self.height

    def rectangle_perimetr(self):
        return (self.height + self.width) * 2

rec1 = Rectangle(2,5)
rec2 = Rectangle(9,8)
rec3 = Rectangle(25,13)

print(f'Площадь rec1 = {rec1.rectangle_square()}, периметр rec1 = {rec1.rectangle_perimetr()}')
print(f'Площадь rec2 = {rec2.rectangle_square()}, периметр rec2 = {rec2.rectangle_perimetr()}')
print(f'Площадь rec3 = {rec3.rectangle_square()}, периметр rec3 = {rec3.rectangle_perimetr()}')

print('\n')

# Задача 2 (Калькулятор)
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

x = Math(5,8)
x.addition()
x.multiplication()
x.division()
x.subtraction()

print('\n')

# Задача 3
class Button:

    type: str = 'Кнопка'

    def __init__(self, text, loc=''):
        self.text = text
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'

tb = Button('Text Box')
cb = Button('Check Box')
rb = Button('Radio Button')
wt = Button('Web Tables')
b = Button('Buttons')
l = Button('Links')
bli = Button('Broken Links - Images')
ud = Button('Upload and Download')
dp = Button('Dynamic Properties')

print(tb.text)
print(tb.click(),'\n')

print(cb.text)
print(cb.click(),'\n')

print(rb.text)
print(rb.click(),'\n')

print(wt.text)
print(wt.click(),'\n')

print(b.text)
print(b.click(),'\n')

print(l.text)
print(l.click(),'\n')

print(bli.text)
print(bli.click(),'\n')

print(ud.text)
print(ud.click(),'\n')

print(dp.text)
print(dp.click())


