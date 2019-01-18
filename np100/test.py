def multiply(_x, y):
    return _x / y


def multiplyWithNoAppendix(_x, y):
    return x // y


def power(_x, y):
    return _x ** y


# 四舍五入
def getAccurateDecimal(_x):
    return round(_x, 3)


PI = 3.141596

# print(getAccurateDecimal(PI))
# print(pow(2, 3))
# print(multiplyWithNoAppendix(1, 3))
# print(multiply(1, 3))

s0 = "HelloWorld"
s1 = "Hello\nWorld"
s2 = """Hello
World"""

# print("s0:", s0)
# print("s1:", s1)
# print("s2:", s2)
# print("s0 == s2?", s0 == s2)
# print("s1 == s2?", s1 == s2)
# print(s0 * 3)
# print('Hello',
#       'World')

# print('Hello '+'World')
# print(s0.index('H'))
# print((s0 * 3).count('He'))
# print(s0[0])


# 字符串的切片
# print("[0:10] ->", s0[0:len(s0)])
# print("[-10:10] ->", s0[-len(s0): len(s0)])
# print("[:10] ->", s0[:len(s0)])
# print("[0:] ->", s0[0:])

s3 = "Python"

# 列表, 存储的都是同样类型的数据
# list1 = []
# list1 = [x * 2 for x in range(10)]
# list1 = [c for c in 'hello']
list1 = list([4, 2, 3])

# del(list1[len(list1) - 1])
# print(list1[:len(list1)])
# print(list1[0:len(list1):2])
# del (list1[0:len(list1):2])
# list1.append(6)
# list1.clear()
# list1.extend([7, 8])
# list1 *= 2
# print(list1.pop())
# list1.remove(7)
# list1.reverse()
# print(list1)

students = [
    {
        "name": "lanyage",
        "age": 18
    },
    {
        "name": "shufang",
        "age": 19
    }
]


def sort(_list, _key, _reverse):
    _list.sort(key=_key, reverse=_reverse)
    return _list


# print(sort(list1, lambda x: x, True))
# print(sort(students, lambda student: student["name"], False))


def appendX(_list, _x):
    _list.append(_x)
    return _list


def removeX(_list, _x):
    _list.remove(_x)
    return _list


def get(_list, _index):
    return _list[_index]


def pop(_list, _index):
    return _list.pop(_index)


def reverseList(_list):
    _list.reverse()
    return _list


# print(appendX(list1, 1))
# print(appendX(list1, 2))
# print(appendX(list1, 3))
# print(get(list1, -1))
# print(pop(list1, 0))
# print(list1)
# print(list1 * 2)
# print(reverseList(list1))
# print(list1)

# tup = ("name", "lanyage")
# print(tup[0])

# print(list(range(10)))
# print(tuple(range(0, 10, 2)))
# print(list(tuple(range(10))))


s = str(b'hello world', encoding="utf-8")


# print(s.capitalize())
# print(s.count('o'))
# print(s.endswith("world"))
# print(s.expandtabs(4))
# print("hello" in s)
# print(s)
# print("hello {0}! My name is {1}".format("world", "Lanyage"))
# print("123".isalnum())
# print("123".isdigit())
# print("123".join("345"))
# print('hello'.title())
# print('123'.zfill(6))

# for i in range(len(list1)):
#     print(i, list1[i])

# print(pow(2, 3))
# print(min(1, 2, 3, key=lambda x: x))


# 闭包和柯里化
def add(_x):
    def adder(_y):
        return _x + _y

    return adder


x = add(1)(2)


# print(x)


# 偏函数
def f(_f, args):
    return _f(*args)


def add(_x, _y):
    return _x + _y


x_y = list([1, 2])
# print(f(add, x_y))

# print(list(map(lambda _x: _x * 2, list1)))
# print(list(filter(lambda _x: _x == 2, list1)))
# print([(x, y)for x in range(3) for y in [4, 5, 6] if x < y])

list2 = [
    [1, 2, 3],
    [4, 5, 6]
]
# print([_x for arr in list2 for _x in arr])

tup2 = 1, 2, 3
tup3 = tup2, 4
# print(tup2)
# print(tup3)

tup4, n = tup3
# print(tup4)
# print(n)

set1 = set((1, 2, 3, 3, 4))
set2 = set((3, 4, 5, 6))
# print(set1)
# print(set2)
# print(set1 | set2)
# print(set1 & set2)
# print(set1 ^ set2)


for student in students:
    for k, v in student.items():
        # print(k, "->", v)
        pass

for i, item in enumerate((1, 2, 3)):
    # print(i, item)
    pass

integers = [3, 2, 1]
integers2 = reversed(integers)
for i in integers2:
    # print(i)
    pass
# print(integers)


# sorted(integers)
# reversed(integers)


import math

# print(math.sqrt(4))


for x in range(1, 11):
    # print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x ** 3))
    pass
# print(round(math.pi, 3))
# print("{0:.3f}".format(math.pi))


f = open("/Users/lanyage/git/learning-python3/day003/students.txt")
s = f.readlines()
# print(s)
s = f.readline()
# print(s)
s = f.readline()
# print(s)


import json

jsn = json.dumps([1, 2, 3])


# print(jsn)


class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


d = Dog("Fido")
# print(d.kind)
# print(d.getName())


import numpy as np

# a = np.arange(15).reshape(3, 5)
# print(a)
# x, y = a.shape
# print(x, y)

# print(a.ndim)
# print(type(a))

a = np.array((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
), dtype=np.int64)


# print(a)
# b = np.zeros((3, 4))
# b = np.ones((3, 4))
# b = np.empty((3, 4))
# print(b)

# print(np.arange(0, 2, 0.3))
# print(np.linspace(0, 10, 9))

# import math
# print(np.sin(math.pi / 2))
# print(a)


# print(a@(a))
# print(a)

# print(a)
# print(np.sum(a, axis=1))
# print(np.sum(a))
# print(np.max(a))
# print(a.max())
# print(a.sum(axis=0))

# print(a ** 2)

# print(np.exp(a))


# a2 = np.arange(10) ** 3
# print(a2)
# print(a2[:6])
# print(a2[:6:2])
#
# a2[:6:2] = -1000
# print(a2)


# print(a[::])
# print(a[0, 0])
# print(a.size)

# print(a)
# print(np.transpose(a))

def f(row, col):
    return row + col


a3 = np.fromfunction(f, (5, 4), dtype=int)
# print(a3)


# print(a3.flat)


a4 = a3.ravel().reshape(a3.size, 1)
# print(a4)
# print(a4.T)
# print(a3)
# print(a3.T)


a5 = np.array((1, 2, 3))
a6 = np.array((4, 5, 6))
# print(np.vstack((a5, a6)))
# print(np.hstack((a5, a6)).reshape(1, a5.size + a6.size))

a7 = a6.copy()
a7[0] = -1
# print(a6)
# print(a7)

print(a6.reshape(1, a6.size).shape)

































