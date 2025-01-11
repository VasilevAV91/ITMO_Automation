from tests.test_one import test_list

a = [5,10,15,29,25,30,35,40]

print('a[2] = ', a[2])

print('a[0:3] = ', a[0:3])

b = [11,12,13]
b[2] = 4
print(b)

test_lst = ['один', 'два', 'три', 'четыре', 'пять']

for elem in test_lst:
    print(elem)

print(len(test_lst))

test_lst.append('шесть')
print(test_lst)