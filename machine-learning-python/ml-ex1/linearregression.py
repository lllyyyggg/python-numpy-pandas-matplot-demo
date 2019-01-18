import numpy as np

data = np.loadtxt('house.txt', delimiter=',')
row, col = data.shape
ones = np.ones((row, 1))
X = np.hstack((ones, data[:, 0: col - 1]))
y = data[:, col - 1:]
x_row, x_col = X.shape


theta = np.ones((x_col, 1))

alpha = 0.02
times = 1000


# compute cost
def computeCost(_X, _y, _theta):
    m = len(_y)
    diff = (_X @ _theta) - _y
    _cost = (1 / (2 * m)) * (diff.T @ diff)
    return _cost


print(computeCost(X, y, theta))


# 梯度下降
def gradient_descent(_theta, _alpha, _times):
    i, m = 0, len(y)
    while i < _times:
        diff = X@_theta - y
        _theta = _theta - _alpha * 1 / m * (X.T @ diff)
        i = i + 1
    return _theta


theta = gradient_descent(theta, alpha, times)
cost = computeCost(X, y, theta)
# print(theta)
# print(cost)
# print(X.dot(theta))
