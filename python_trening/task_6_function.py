def func(x, y):
    return x + y

print(func(1,2))
print(func('I a', 'm tester'))

def func1(a,b,c = 2, d = 3):
    return a+b+c+d

print(func1(1,1, 1, 1))
print(func1(2,2))
print(func1(1,1, 1))

def range_arg(a,b,c,d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1','2','3','4'))
print(range_arg('1','2',d='3',c='4'))

def first_elem(a=(1,2,3,4)):
    return a[0]
print(first_elem())

def square(radius, pi=3.14159):
    return pi * radius ** 2
print(square(2))
