import numpy as np

# 1-将列表放入numpy
data = [1, 2, 3]
a = np.array(data)
# print(a)
# [1 2 3]

# 2-创建二维矩阵
data = [[1, 2, 3], [4, 5, 6]]
a = np.array(data)
# print(a)
# [[1 2 3]
#  [4 5 6]]

# 3-输出arr的数据类型
data = [1, 2, 3]
a = np.array(data)
# print(a.dtype)
# int64

# 4-打印8*4矩阵
a = np.empty([8, 4])
# print(a)

# 5-打印3 * 4 * 5矩阵
a = np.empty([3, 4, 5])
# print(a)

# 6-打印2*4矩阵
a = np.empty([2, 4])
# for i in range(2):
#     print(a)

# 7-二维矩阵
a = np.array([[1, 2]])
# print(a.shape)
# (1, 2)

# 8-输出矩阵，指定数据类型
a = np.array([2, 2], dtype='int32')
# print(a)

# 9-控制矩阵的形状 8 * 4
a = np.arange(32).reshape(8, 4)
# print(a)

# 10-将1-2分成3份
a = np.linspace(1, 2, 3)
# print(a)
# [1.  1.5 2. ]

# 11-输出单位矩阵
a = np.eye(9)
# print(a)

# 12-输出全为0的一维矩阵
a = np.zeros([3])
# print(a)
# [0. 0. 0.]

# 13-输出均为0-4维矩阵
a = np.zeros([2, 2, 2, 2])
# print(a)

# 14-随机矩阵 3 * 4
a = np.random.random([3, 4]).reshape(2, 6)
# print(a)


# 索引和切片
a = np.arange(10)
# 1 - 2
# print(a[1:3])
# print(a)

# a[0:10] = 1
# print(a)

# a = np.arange(10).reshape(5, 2)
# b = np.copy(a)
# print(b)

# 二维数组切片

a = np.arange(1, 10).reshape(3, 3)
# 输出第1行
# print(a[:1])
# 输出1行以后的所有行
# print(a[1:])
# [[4 5 6]
#  [7 8 9]]
# 输出第一行第一个
# print(a[:1, :1])
# [[1]]
# 输出所有行的2，3列
# print(a[:, 1:])
# [[2 3]
#  [5 6]
#  [8 9]]

# 转置和相乘
a = np.arange(9).reshape([3, 3]).T
# print(a)
# print(np.array([1, 2, 3]).dot(np.array([[3], [2], [1]])))
a = np.arange(16).reshape([2, 2, 4])
# print(a)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]]
#
#  [[ 8  9 10 11]
#   [12 13 14 15]]]

# d = np.transpose(a, [1, 0, 2])
# print(d)


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# print(np.hstack([a, b]))
# [[1 2 5 6]
#  [3 4 7 8]]
# print(np.vstack([a, b]))
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# 取指数函数
# print(np.exp([3, 1]))


points = np.arange(-5, 5, 1)
# print(points)
# [-5 -4 -3 -2 -1  0  1  2  3  4]
# xs, ys = np.meshgrid(points, points)
# print(xs)
# print(ys)

# where字句
a = np.random.random(9).reshape(3, 3)
# print(a)
# print(np.where(a > 0, 1, -1))

a = [1, 2, 3, 4]
# 矩阵的逆
# print(np.invert(a))
# [-2 -3 -4 -5]


a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# 横向累计和
# print(np.cumsum(a, 1))
# 纵向累积和
# print(np.cumsum(a, 0))

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
# print(steps)
walk = np.cumsum(steps)
# print(walk)