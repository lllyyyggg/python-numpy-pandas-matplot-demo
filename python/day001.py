# 下面实现数字的一些算法


# Numbers

# 17 / 3  # 除法
# 17 // 3  # 除法取整

# 5 ** 2  # 幂

# tax = 12.5 / 10
# price = 100.50
# price * tax

# 12.5625   这值会赋值给 _

# price + _
# round(_, 2)   保留两位小数


# String

# s = 'Hello\nworld'      # \n表示换行
# print(s)

# Hello
# world

# print("""\
# hello
# world
# """)

# 打印多行
# hello
# world

# print(3 * 'hello' + 'world')

# 打印三次
# hellohellohelloworld

# print('hello' 'world')

# 连起来
# helloworld

# text = ('Hello world,'
#         'welcome to the world of unreal!!!')

# print(text)

# 打印全部，将长字符串进行分行
# Hello world,welcome to the world of unreal!!!

# prefix = 'Py'
# print(prefix + 'thon')

# Python


# word = 'Python'


# print(word[0])
# print(word[5])

# P
# n

# print(word[-1])
# print(word[-6])
# 从后往前
# n
# P

# print(word[0:2])
# print(word[0:6])

# 打印子串
# Py
# Python

# print(word[0:])

# 打印全部
# Python


# print(word[:2] + word[2:])
# 打印全部
# Python


# 这样来记住索引
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

# print(word[0: 42])
# print(word[42:])
# 打印所有，超出的部分不打印
# Python
# ''

# word[0] = 'J'

# 字符串是不可变的类型
# 'str' object does not support item assignment


# print('J' + word[1:])

# 重新生成字符串
# Jython


# s = 'supercalifragilisticexpialidocious'
# print(len(s))
# 打印字符串长度
# 34

# https://docs.python.org/3.6/library/stdtypes.html#str.center  String.methods
# https://docs.python.org/3.6/library/string.html#formatstrings String.format

# Lists

# String和Lists都是sequence类型

# squares = [1, 4, 9, 16, 'hello']
# print(squares)
# [1, 4, 9, 16, 'hello']

# print(squares[0])
# 1

# squares = [1, 4, 9, 16, 25]
# print(squares + [36, 49])
# [1, 4, 9, 16, 25, 36, 49]

# squares[0] = 'hello'
# print(squares)
# List是可变类型
# ['hello', 4, 9, 16, 25]

# 添加内容
# squares.append(1000)
# print(squares)
# [1, 4, 9, 16, 25, 1000]

# squares[1: 3] = [2, 3]
# 区域替换
# print(squares)
# [1, 2, 3, 16, 25]

# n = [1, 2, 3]
# x = [squares, n]
# print(x)
# 可嵌套
# [[1, 4, 9, 16, 25], [1, 2, 3]]

# 开始编程
# a, b = 0, 1
#
# while b < 10:
#     print(b)
#     a, b = b, a + b
# 循环打印
# 1
# 1
# 2
# 3
# 5
# 8

# i = 256 * 256
# print('The result is', i)
# The result is 65536


# a, b = 0, 1
# while b < 1000:
#     print(b, end=',')
#     a, b = b, a + b
# 打印斐波那契数列，用,隔开
# 1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

# if

# x = int(input('Please input an integer: '))
# print(x)

# 标准输入
# Please input an integer: 1
# 1

# if x < 0:
#     x = 0
#     print('Negative number was changed to zero!!!')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print("Single")
# else:
#     print('More')

# 打印内容
# Please input an integer: 1
# 1
# Single

# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
# 打印字符串和字符串长度
# cat 3
# window 6
# defenestrate 12


# for w in words[:]:
#     if len(w) > 6:
#         words.insert(0, w)
# print(words)

# 迭代时打印集合
# ['defenestrate', 'cat', 'window', 'defenestrate']

# range

# for i in range(5):
#     print(i)

# 0
# 1
# 2
# 3
# 4

# range(5, 10)
# 类似于5-10
# range(0, 10, 3)
# 打印0-10隔3打一次
# 0 3 6 9
# range(-10, -100, -30)
# -10 -40 -70

# a = ['Mary', 'Tom', 'Jimmy']
# for i in range(len(a)):
#     print(i, a[i])

# 0 Mary
# 1 Tom
# 2 Jimmy


# print(list(range(5)))
# [0, 1, 2, 3, 4]

# break and continue, and else


# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n / x)
#             break
#     else:
#         print(n, 'is a prime number')
# else是用来检测是否有break的，属于内层的for
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2.0
# 5 is a prime number
# 6 equals 2 * 3.0
# 7 is a prime number
# 8 equals 2 * 4.0
# 9 equals 3 * 3.0

# for num in range(2, 10):
#     if num % 2 == 0:
#         print("Found an even number : ", num)
#         continue
#     print("Found a number", num)

# continue
# Found an even number :  2
# Found a number 3
# Found an even number :  4
# Found a number 5
# Found an even number :  6
# Found a number 7
# Found an even number :  8
# Found a number 9


# pass

# pass不做任何事情，当你需要同步等待的时候，就用这个。

# while True:
#     pass

# Functions

# def add(x, y):
#     """Print the sum"""
#     print(x + y)


# add(1, 2)
#
# f = add
# f(2, 3)
# 3
# 5


# def add(x, y):
#     """Print the sum"""
#     return x + y
#
#
# print(add(1, 2))


# 待返回值的函数
# 3

# 默认参数

# def ask_ok(prompt, retries=4):
#     print(prompt, retries)

# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()

# 默认参数不会随着外界的变化而变化

# def f(a, L=[]):
#     L.append(a)
#     return L


# print(f(1))
# print(f(2))
# print(f(3))

# [1]
# [1, 2]
# [1, 2, 3]

# 关键字参数

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# 关键字参数
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# 以下调用会报错
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument


# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger",
#            "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch

# def concat(*args, sep="/"):
#     return sep.join(args)
# print(concat("earth", "mars", "venus"))
# earth/mars/venus

# 拆开参数列表
# print(list(range(3, 6)))

# args = [3, 6]
# print(list(range(*args)))

# [3, 4, 5]
# [3, 4, 5]

# 如果是复杂的参数，我们用字典来进行分离

# def parrot(voltage, state='a stiff', action='voom'):
#     print()
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# lambda表达式

# def make_increment(n):
#     return lambda x: x + n
# f = make_increment(42)
# print(f(1))
# 43

# 传入一个简单的lambda的小函数作为参数
# pairs = [1, 2, 5, 4]
# pairs.sort(key=lambda pair: pair)
# print(pairs)

# document字符串
# def f():
#     """This is document String"""
#     pass
#
#
# print(f.__doc__)

# This is document String


# Function Annotations


















