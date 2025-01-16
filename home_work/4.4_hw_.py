# Задача 4 (программа с классом Car)
import random

class Car:

    year: list = [2010,2011,2012,2013,2014]
    type: list = ['седан', 'универсал', 'кабриолет', 'хэтчбек', 'пикап']
    color: list = ['рыжий', 'белый', 'красный', 'черный', 'синий']

    def start_engine(self):
        return ('Автомобиль заведен')

    def stop_engine(self):
        return ('Автомобиль заглушен')

    def car_year(self):
        self.year = random.choice(Car.year)
        return self.year

    def car_type(self):
        self.type = random.choice(Car.type)
        return self.type

    def car_color(self):
        self.color = random.choice(Car.color)
        return self.color

car1 = Car()
print(car1.start_engine())
print(car1.stop_engine())
for i in range(1,6):
    print(f'Автомобиль {i}: {car1.car_year()} г.в., тип - {car1.car_type()}, цвет - {car1.car_color()}')
