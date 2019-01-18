import matplotlib.pyplot as plt
import numpy as np

# 柱状图
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.bar(X, +Y1, facecolor='#0086ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#cccccc', edgecolor='white')


for x, y in zip(X, Y1):
    """ha: horizontal alignment"""
    plt.text(x + 0.01, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    """ha: horizontal alignment"""
    plt.text(x + 0.01, -y - 0.05, '-%.2f' % y, ha='center', va='top')
plt.show()
