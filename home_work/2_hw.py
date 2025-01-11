#Задача 1
def task_1() -> tuple:
    a: int = 1
    b: float = 2.2
    c: str = 'Hello, World!'
    d: list = [1,2,3,4]
    e: bool = True
    return type(a), type(b), type(c), type(d), type(e)
print(task_1())

#Задача 2
def task_2() -> list:
    a = [1,2,3,5,8,13,21]
    return a[:3]
print(task_2(), 'Последовательность Фибоначчи')

#Задача 3
def task_3(x: int) -> int:
    return x * x
print(task_3(22))
