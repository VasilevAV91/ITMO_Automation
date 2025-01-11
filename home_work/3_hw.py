# Задача 2 Наибольшее число
def max_number(x: int, y:int):
    print(max(x,y))
max_number(-100,2)

# Задача 3 Числа с разницей 135
def func(x: int, y: int):
    if abs(x - y) == 135:
        print('Yes')
    else:
        print('No')
func(-271,-136)

# Задача 4 Сезон года
def season(x: int):
    if x == 1 or x == 2 or x == 12:
        print('Зима')
    elif x in range(3,6):
        print('Весна')
    elif x in range(6,9):
        print('Лето')
    elif x in range(9,12):
        print('Осень')
    else:
        print('Введите корректный номер месяца')
season(5)

#Задача 5 Числа больше 10
def func1(x: int, y: int, z: int):
    if x > 10 and y > 10 and z > 10:
        print('Yes')
    else:
        print('No')
func1(11,12, 13)

#Задача 6 Количество положительных чисел в списке
def func2(lst: list):
    res = 0
    for i in lst:
        if i > 0:
            res += 1
    return res
print(func2([1,2,3,4]))

#Задача 7 Количество дней
def day_count(a: int, b: int):
    return a * 12 * 29 + b * 29
print(day_count(1,10))