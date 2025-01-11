# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение.

num = 3
# num = -5
# num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')
else:
    print('НЕТ')

# num_float = 3.4
# num_float = 0
num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def kurs(z):
    if z == 1 or z == 2 or z == 3 or z == 4:
        print('Вы бакалавр')
    elif z in range(5, 7):
        print('Вы магистр')
    elif 7 <= z <= 9:
        print('Вы аспирант')
    else:
        print('Введите корректныый год обучения')
kurs(7)

def func(x):
    if x > 100 or x < -100:
        print('-')
    else:
        print('+')
func(-1000)
