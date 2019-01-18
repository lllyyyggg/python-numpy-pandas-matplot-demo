# Data Structures


# Lists

# words = ['Python', 'JavaScript', 'Java']

# print(words)

# words.append('Ruby')
#
# print(words)

# ['Python', 'JavaScript', 'Java']
# ['Python', 'JavaScript', 'Java', 'Ruby']


# numbers = [1, 2, 3]

# numbers.extend(words)

# extend类似于复制
# print(numbers)

# numbers[3] = 'Scala'

# print(numbers)
# print(words)

# numbers.insert(2, 6)

# print(numbers)
# 打印所有的数字

# numbers.remove(7)
# 移除元素，如果元素不存在，那么就会报错
# print(numbers)

# number = numbers.pop(2)
# 移除并且返回元素
# print(numbers)
# print(number)

# [1, 2, 3]
# 6

# print(numbers)

# print(numbers.index(6, 3, len(numbers)))
# 如果不存在就会报错


# count3 = numbers.count(3)
# 打印3出现的次数
# print(count3)

# numbers.sort(key=lambda x: x, reverse=True)
# 进行排序
# print(numbers)

# newnumbers = numbers.copy()
# newnumbers[0] = 1000
# 复制元素
# print(newnumbers)
# print(numbers)

# List可以用作stack

# numbers = [1, 2, 3]

# print(numbers)
# print(numbers.pop())
# print(numbers.pop())
# print(numbers.pop())
# print(numbers)

# 后进先出
# [1, 2, 3]
# 3
# 2
# 1
# []

# 先进显出作为队列
# print(numbers.pop(0))
# print(numbers.pop(0))
# print(numbers.pop(0))
# print(numbers)
#
# 1
# 2
# 3
# []


# numbers = list(map(lambda x: x * 2, numbers))
# 通过lambda表达式进行数字的乘2操作

# numbers = [x ** 2 for x in numbers]
# 可以通过更加简短的形式来进行数组元素的操作。
# print(numbers)


# print([(x, y) for x in range(3) for y in [3, 1, 4] if x != y])
# 使用List Generator生成List
# x属于[1,2,3] y属于[3,1,4] 并且 x != y

# print([x * 2 for x in [1, 2, 3]])
# print([x for x in [-1,2,3] if x > 0])
# print([abs(x) for x in [-1, -2, -3]])

# 去除字符串的空格
# print(' hello world    '.strip())

# vec = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# 将多为数组变为一维数组
# print([num for ele in vec for num in ele])


# List的嵌套

# matrix = [
#     [1, 3, 5, 7],
#     [2, 4, 6, 8],
#     [-1, -3, -5, -7]
# ]

# print(matrix)

# 3 * 4 数组转变成为 4 * 3数组
# print([[row[i] for row in matrix] for i in range(4)])
# print(matrix)
# 矩阵的转制
# [[1, 2, -1], [3, 4, -3], [5, 6, -5], [7, 8, -7]]

# del语句

# a = [1, 2, 3, 4, 5, 6]

# 删除a[0]
# del a[0]
# 删除所有元素
# del a[0: len(a)]
# 删除整个数组
# del a
# print(a)

# 元组和序列

# 元组

# t = 12, 34, 56
# 这是一个三元组
# print(t)
# print(t[0])

# 元组是不可变的
# 元组是可以嵌套的

# nt = 78, t
# 嵌套的元组
# print(nt)

# 元组和List的区别就是，元组是不可变的，List是可变的。
# List中的元素一般都是同类型的。

# t = 'hello',
# print(t)

# t = (1, 2, 3)

# x, y, z = t
# 元组的反向赋值
# print(x, y, z)


# Set集合
# set是另外一种集合类型，无序无重复元素。
# set支持union、intersection、 difference和symmetric difference

# basket = {'apple', 'orange', 'apple', 'pear'}
# print(basket)

# print('orange' in basket)
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(b)
# print(a | b)
# print(a & b)
# print(a ^ b)

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# 字典 字典类似于JavaScript中的对象
# person = {'name': 'lanyage', 'age': 18}
# print(person)
# print(person['name'])
# del person['age']
# print(person)
# print(list(person.keys()))
# print(sorted(person.keys()))

# 将元组的列表转变为字典
# print(dict([('name', 'lanyage'), ('age', 18)]))

# print({x: x ** 2 for x in (1, 2, 4)})
# {1: 1, 2: 4, 4: 16}

# 将参数转变为dict
# print(dict(sape = 4399))
# {'sape': 4399}


# Loop技术

# for k,v in person.items():
#     print(k, v)
# name lanyage
# age 18

# for i, v in enumerate([1, 2, 3]):
#     print(i, v)

# 0 1
# 1 2
# 2 3


# questions = ['name', 'quest', 'favorite color']
#
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0} ? It is {1}.'.format(q, a))

# What is your name ? It is lancelot.
# What is your quest ? It is the holy grail.
# What is your favorite color ? It is blue.


# for i in reversed(range(1, 10, 2)):
#     print(i)

# 逆序打印List
# 9
# 7
# 5
# 3
# 1

# basket = ['apple', 'orange', 'apple', 'pear','orange', 'banana']

# set也可以排序？？？ WTF
# for f in sorted(set(basket)):
#     print(f)


# import math
# raw_data = [56.2, float('NaN'), 51.7]
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

# 两者是一样的效果
# print([x for x in raw_data if not math.isnan(x)])
# print(filtered_data)

# 类型的比较
# print([1, 2, 3] < [1, 2, 2])
# print([1, 2, 3] == [1.0, 2, 3])


# 模块Modules

# — fibo.py
# - import fibo

# 获取模块的名称
# print(fibo.__name__)

# from fibo import fibo, fibo2
# or
# from fibo import *
# from fibo import fibo as fibonacci

# 执行python脚本

# python fibo.py

# 还可以传参
# python fibo.py 100

# if __name__ == "__main__":
#     import sys
#     fibo(int(sys.argv[1]))

# import语句不会让引进的模块代码跑起来

# 模块搜索路径
# 1. build-in module
# 2. file named fibo.py

# 编译后的python文件

# 为了加快加载模块的速度，python会缓存编译过的版本在__pycache__目录中的module.version.pyc
# __pycache__/fibo.cpython-33.pyc

# 有两种情况下不检查缓存。
# 1. 总是重新编译不存储结果的模块
# 2. 没有源模块的模块

# -o用来减少编译模块的体量

# 通用的模块

# import sys

# print(sys.ps1)

# sys.path是个string的列表，决定解释器的模块搜索路径。
# print(sys.path)

# print(dir(fibo)) ['__name__', 'fib', 'fib2'] print(dir(sys)) 打印模块定义的名字 ['__displayhook__', '__doc__',
# '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__',
# '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe', '_git',
# '_home', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names',
#  'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
# 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks',
#  'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
# 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount',
# 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern',
# 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache',
# 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', 'setdlopenflags',
# 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info',
# 'version', 'version_info', 'warnoptions']


# 如果没有参数，那么dir()列出的是当前文件下定义的变量。
# a = [1, 2, 3]
# print(dir())

# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
# '__spec__', 'a']


# dir(o)不会列出所有内建的函数和变量。如果你想列出那些，可以使用如下

# import builtins
# print(dir(builtins))

# Packages是一个模块化程序的一个方法

# import sound.effect.echo
# 等价于sound/effects/echo/py
# 这种情况下你必须加上全包名.
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# 替代的方式可以这样
# from sound.effects import echo
# echo.echofilter(...)

# 还可以import自己感兴趣的方法
# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

# 从Package中导入*
# 这样是很不好的做法，因为可能会消耗太多的时间。
# 解决的办法就是: 如果__init__.py带啊吗定义了一个叫做__all__的集合
# 那么你import的内容就是__all__里面的内容。

# __all__ = ["echo", "surround", "reverse"]
# 那么 from sound.effects import *
# 将只会引入上面的那几个模块。

# 如果没有定义上面的__all__那么就可以考虑下面这种方式进行导入
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *
# 这种方式当__all__存在的情况下也是可以的。

# import * 在生产代码上都被视为不好的代码，因此不要这样。

# sound.filters.vocoder想引用echo
# 可以使用绝对路径 from sound.effects import echo.
# 也可以使用相对路径 from module import name

# from . import echo
# from .. import formats
# from ..filtes import equalizer

# 相对引入基于当前模块的名称。因为main module的名字永远是 __main__.如果
# 一个模块想被使用为主模块，那么一直使用绝对路径。





