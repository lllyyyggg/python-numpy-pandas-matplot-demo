# 两个格式化输出的方法
# 1. string concatenation
# 2. string.format()


# s = 'Hello World.'
# print(s)
# print(str(s))
# print(repr(s))
# print(str(1 / 7))
# Hello World.
# Hello World.
# 'Hello World.'

# hello = 'hello, world\n'
# print(repr(hello))
# 'hello, world\n'

# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x ** 3).rjust(4))

# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x ** 3))
# rjust()表示的是右对齐
# 可以等价于下面这种写法
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125
#  6  36  216
#  7  49  343
#  8  64  512
#  9  81  729
# 10 100 1000

# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))
# 00012
# -003.14
# 3.14159265359

# print('We are {}'.format('family'))
# We are family
# print('We are {0}'.format('family'))
# We are family

# print('The story is {adj}'.format(adj='WONDERFUL'))
# The story is WONDERFUL

# print('Hello {!r}'.format('world'))
# Hello 'world'

# import math
# print('The value of Pi is approximately {0:.3f}'.format(math.pi))
# The value of Pi is approximately 3.142

# table = {'Lanyage': 2995, 'Daimengxiao': 3451}
# for name, phone in table.items():
#     print('{0:18} ==> {1:10d}'.format(name, phone))

# 或者直接使用字典进行操作

# table = {'Sjoerd':4127, 'Jack':4098, 'Dcad': 8223}
# print('Jack: {0[Jack]:d}; Sjoerd:{0[Sjoerd]:d}; Dcad:{0[Dcad]:d}'.format(table))
# Jack: 4098; Sjoerd:4127; Dcad:8223
# print('Jack:{Jack:d}; Sjoerd:{Sjoerd:d}; Dcad:{Dcad:d}'.format(**table))
# Jack:4098; Sjoerd:4127; Dcad:8223

# import math
# print('The value of pi is approximately %5.3f'%math.pi)
# The value of pi is approximately 3.142

# with open('/Users/lanyage/git/learning-python3/day003/students.txt') as f:
#     for line in f:
#         print(line, end='')
# f.close()

# lanyage 18
# daimengxiao 18
# shufang 18

# with open('/Users/lanyage/git/learning-python3/day003/students.txt', 'w') as f:
#     f.write(str(('Tom', 8)))
# f.close()
# 写文件

# f = open('/Users/lanyage/git/learning-python3/day003/students.txt', 'rb+')
# f.write(b"helloworld")
# f.seek(5)
# print(f.read(1))

# import json

# jsn = json.dumps([1, 'Hello', 'NewYear'])
# print(jsn)
# [1, "Hello", "NewYear"]

# json.dump({'name': 'hello'}, f)
# x = json.load(f)
# print(x)


# Errors and Exceptions
# print(1 / 0)

# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print('Oops! That was no valid number.')

# except (RuntimeError, TypeError, NameError):
#     pass:
# 声明多个异常

# 抛出异常
# raise NameError('HiThere')

# 用户自定义异常

# class Error(Exception):
#     pass
#
#
# class InputError(Error):
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message

# 清理工作

# try:
#     raise KeyboardInterrupt
# finally:
#     print('good bye')
# Traceback (most recent call last):
# good bye
#   File "/Users/lanyage/git/learning-python3/day003/day003.py", line 135, in <module>
#     raise KeyboardInterrupt
# KeyboardInterrupt


# Python中的class

# class MyClass:
#     """A simple example class"""
#     i = 12345
#
#     def __init__(self):
#         print('Initializing...')
#         self.data = [1, 2, 3]
#
#     def f(self):
#         return 'hello world'
#
# c = MyClass()
# print(c.i)
# print(c.f())
# print(c.data)
# 12345
# hello world

# __init__函数用来实例化对象

# 添加新的属性
# c.couter = 1
# print(c.couter)


# class Dog:
#     kind = 'canine'
#
#     def __init__(self, name):
#         self.name = name


# d = Dog('Fido')
# e = Dog('Buddy')

# print(d.name)
# print(e.name)

# 如果是类中有引用形式的变量，那么是错误的
# def __init__(self, name):
#         self.name = name
#         self.tricks = []


# 继承
# class DerivedClassName(BaseClassName):

# 多继承
# class DerivedClassName(modname.BaseClassName):

# class A:
#     pass
# class B(A):
#     pass
# b = B()
# print(issubclass(B, A))
# print(isinstance(b, A))
# print(isinstance(b, B))
# 通过isinstance和issubclass来检查是否为某个类的实例或是否是某个类的子类

# 迭代器

# it = iter([1, 2, 3])


# print(next(it))
# print(next(it))
# print(next(it))

# class Reverse:
#     """Iterator for looping over a sequence backwards"""
#
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]


# rev = Reverse('hello')
# it = iter(rev)
# print(next(it))

# Generators是另外一种用于生成迭代器的方式

# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield (data[index])
#
#
# for char in reverse([1, 2, 3]):
#     print(char)
# 3
# 2
# 1

# print(sum(i * i for i in [1, 2, 3]))
# print(zip([1, 2, 3], [4, 5, 6]))

# range, zip都是Generator


# 常用标准库

# import os
# print(os.getcwd())
# os.system('cat students.txt')
# print(dir(os))

# import shutil

# print(shutil.copyfile('students.txt', 'students2.txt'))
# print(shutil.move('a','b'))

# import glob
# print(glob.glob('*.py'))


# import sys
# print(sys.argv)
# print(sys.stderr.write('Warning!'))

# 正则表达式

# import re
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# import random
# print(random.randrange(6))

# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# from urllib.request import urlopen
#
# with urlopen('http://xxx.xxx') as response:
#     for line in response:
#         print(line)

# 日期库

# from datetime import date
# now = date.today()
# print(now)
# 2019-01-02

# birthday = date(1999,9,9)
# print(birthday)


# 数据压缩

# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
#
# t = zlib.compress(s)
# print(len(t))
#
# ss = zlib.decompress(t)
# print(ss)
# print(len(ss))
#
# sss = zlib.crc32(s)
# print(sss)

# from timeit import Timer
#
# def hell0(name):
#     print('hello,', name)

# 输出格式化

# import reprlib
# print(reprlib.repr(set('abcde')))
# {'a', 'b', 'c', 'd', 'e'}

# import pprint
# t = [[1,2,3],[2,3,4]]
# pprint.pprint(t, width=20)

# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""
# print(textwrap.fill(doc, width=30))


# import locale

# from string import Template
# t = Template('${hello} folks')
# print(t.substitute(hello='Hey'))

# 多线程
# import threading, zipfile

# import threading
# import zipfile
#
#
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
#
#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)
#
#
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')
#
# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')


# 日志

# import logging
#
#
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')


# 弱引用


import weakref, gc


# class A:
#     def __init__(self, value):
#         self.value = value
#
#     def __repr__(self):
#         return str(self.value)


# a = A(10)
# d = weakref.WeakKeyDictionary()

# d['primary'] = a
# print(d['primary'])

# del a

# print(gc.collect())


# 和List配合的工具

# from array import array
#
# a = array('H', [1,2,3,4])
# print(a)
# print(sum(a))
# print(a[0:3])

# from collections import deque
#
# d = deque(['task1', 'task2', 'task3'])
# d.append('task4')
#
# print('handling', d.popleft())
# print(d)

# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)

# 建堆
# from heapq import heapify, heappop, heappush
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# heapify(data)
# heappush(data, -5)
# print([heappop(data) for i in range(3)])

# 浮点型计算

# from decimal import *
# round(Decimal('0.70') * Decimal('1.05'), 2)
# print(Decimal('0.74'))


# python库
# numpy scipy matplotlib scikit-learn pandas
# python3.6 -m pip install scipy

