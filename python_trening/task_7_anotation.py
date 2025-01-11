a: int = 5
b: str = 'строка'
c: list = [1,2]
def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s

print(indent('123', 10))

def ln_str(s: str = '') -> int:
    return len(s)

print(ln_str('Hello, world!'))

def ln_lst(a: list, b: list) -> int:
    return max(len(a), len(b))
print(ln_lst([1,2,3], [4,5,6,7,8]))

def func_lst(x: list, y) -> list:
    x.append(y)
    return x
print(func_lst([1,2,3], [5,6,7]))

def summa_lst(x: list) -> int:
    sum = 0
    for i in x:
        sum = sum + i
    return sum
print(summa_lst([1,2,3,4,5]))

